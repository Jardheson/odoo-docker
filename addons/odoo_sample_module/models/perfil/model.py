from odoo import models, fields

class PerfilModel(models.Model):
    _name = 'perfil.model'
    _description = 'Perfil Model'

    name = fields.Char(string='Name', required=True)

    data = fields.Date(
        string='Data'
    )

    valor = fields.Float(
        string='Valor do Pagamento'
    )

    numero_inteiro = fields.Integer(
        string='Número Inteiro'
    )

    state = fields.Selection(
        string='Tipo',
        selection=[
            ('tipo1', 'Tipo 1'),
            ('tipo2', 'Tipo 2')
        ]
    )
    

  