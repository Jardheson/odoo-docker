from odoo import models, fields

class UnidadeOrganizacionalModel(models.Model):
    _name = 'unidade.organizacional.model'
    _description = 'Unidade Organizacional Model'

    name = fields.Char(
        string='Nome',
        required=True
    )

    codigo = fields.Char(
        string='Código',
        required=True
    )
