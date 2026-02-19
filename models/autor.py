from odoo import models, fields, api


class autor(models.Model):
    _name = 'biblioteca.libro'
    _description = 'biblioteca.libro'
    name = fields.Char()
    nationality = fields.Char()
    birthDate = fields.Date()
    libros = fields.One2many('biblioteca.libro', 'autor_id', string='Libros')