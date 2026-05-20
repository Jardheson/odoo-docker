from odoo import models, fields

class PessoaModel(models.Model):
    _name = 'pessoa.model'
    _description = 'Pessoa Model'

    name = fields.Char(
        string='Nome',
        required=True
    )

    cpf = fields.Char(
        string='CPF',
        required=True
    )

    data_nascimento = fields.Date(
        string='Data de Nascimento'
    )
