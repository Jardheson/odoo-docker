from odoo import models, fields

class ContaModel(models.Model):
    _name = 'conta.model'
    _description = 'Conta Model'

    name = fields.Char(
        string='Nome',
        required=True
    )

    codigo = fields.Char(
        string='Código',
        required=True
    )

    
