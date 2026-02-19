from odoo import models, fields, api


class libro(models.Model):
    _name = 'biblioteca.libro'
    _description = 'biblioteca.libro'
    title = fields.Char()
    isbn = fields.Char()
    publishingDate = fields.Date()
    #autor = 

#    @api.depends('value')
#    def _value_pc(self):
#        for record in self:
#            record.value2 = float(record.value) / 100
