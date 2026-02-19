from odoo import models, fields, api
from odoo.exceptions import ValidationError


class prestamo(models.Model):
    _name = 'biblioteca.prestamo'
    _description = 'biblioteca.prestamo'
    readerName = fields.Char()
    lendingDate = fields.Date()
    returnDate = fields.Date()

    libro_id = fields.Many2one('biblioteca.libro', string='Libro')

    @api.constrains('returnDate')
    def _check_return_date(self):
        for record in self:
            if record.lendingDate >= record.returnDate:
                raise ValidationError("La fecha de devolucion debe ser posterior a la de prestamo")