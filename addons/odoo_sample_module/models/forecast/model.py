from odoo import models, fields, api


class Forecast(models.Model):

    _name = 'forecast.forecast'
    _description = 'Forecast - Previsão Orçamentária'
    _order = 'ano DESC, versao DESC'

    ano = fields.Integer(
        string='Ano',
        required=True,
        help='Ano da previsão'
    )

    versao = fields.Char(
        string='Versão',
        required=True,
        help='Versão da previsão (ex: v1.0, v1.1, etc)'
    )

    centro_responsabilidade_id = fields.Many2one(
        comodel_name='forecast.centro_responsabilidade',
        string='Centro de Responsabilidade',
        required=True,
        help='Centro de responsabilidade desta previsão'
    )

    cenario = fields.Selection(
        selection=[
            ('otimista', 'Otimista'),
            ('realista', 'Realista'),
            ('pessimista', 'Pessimista'),
        ],
        string='Cenário',
        required=True,
        default='realista',
        help='Cenário da previsão'
    )

    state = fields.Selection(
        selection=[
            ('draft', 'Rascunho'),
            ('pending_review', 'Aguardando Revisão'),
            ('approved', 'Aprovado'),
            ('rejected', 'Rejeitado'),
            ('published', 'Publicado'),
        ],
        string='Status',
        default='draft',
        required=True,
        help='Status da previsão'
    )

    created_at = fields.Datetime(
        string='Criado em',
        default=lambda self: fields.Datetime.now(),
        readonly=True
    )

    updated_at = fields.Datetime(
        string='Atualizado em',
        default=lambda self: fields.Datetime.now(),
    )

    descricao = fields.Text(
        string='Descrição',
        help='Descrição adicional da previsão'
    )

    @api.model
    def create(self, vals):
        vals['updated_at'] = fields.Datetime.now()
        return super().create(vals)

    def write(self, vals):
        vals['updated_at'] = fields.Datetime.now()
        return super().write(vals)