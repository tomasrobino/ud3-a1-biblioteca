from odoo import models, fields, api
from odoo.exceptions import ValidationError


class prestamo(models.Model):
    _name = 'biblioteca.prestamo'
    _description = 'biblioteca.prestamo'
    readerName = fields.Char()
    lendingDate = fields.Date()
    returnDate = fields.Date()
    prestamoLength = fields.Integer(compute='_compute_prestamoLength')

    libro_id = fields.Many2one('biblioteca.libro', string='Libro')

    @api.constrains('returnDate')
    def _check_return_date(self):
        for record in self:
            if record.lendingDate >= record.returnDate:
                raise ValidationError("La fecha de devolucion debe ser posterior a la de prestamo")

    @api.depends("lendingDate", "returnDate")
    def _compute_prestamoLength(self):
        for record in self:
            if record.lendingDate and record.returnDate:
                record.prestamoLength = (record.returnDate - record.lendingDate).days
            else: record.prestamoLength = 0