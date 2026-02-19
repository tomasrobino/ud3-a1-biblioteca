from odoo import models, fields, api


class autor(models.Model):
    _name = 'biblioteca.autor'
    _description = 'biblioteca.autor'
    name = fields.Char()
    nationality = fields.Char()
    birthDate = fields.Date()
    
    libros = fields.One2many('biblioteca.libro', 'autor_id', string='Libros')