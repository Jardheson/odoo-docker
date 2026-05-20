from odoo import models, fields

class CasaModel(models.Model):
    _name = 'casa.model'
    _description = 'Casa Model'

    name = fields.Char(
        string='Nome',
        required=True
    )
