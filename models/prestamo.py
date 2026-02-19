from odoo import models, fields, api


class prestamo(models.Model):
    _name = 'biblioteca.prestamo'
    _description = 'biblioteca.prestamo'
    readerName = fields.Char()
    lendingDate = fields.Date()
    returnDate = fields.Date()

    libro_id = fields.Many2one('biblioteca.libro', string='Libro')