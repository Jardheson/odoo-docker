from odoo import models, fields


class CentroResponsabilidade(models.Model):
    """Modelo para Centro de Responsabilidade."""

    _name = 'forecast.centro_responsabilidade'
    _description = 'Centro de Responsabilidade'
    _order = 'name'

    name = fields.Char(
        string='Nome',
        required=True,
        help='Nome do centro de responsabilidade'
    )

    codigo = fields.Char(
        string='Código',
        unique=True,
        required=True,
        help='Código único do centro de responsabilidade'
    )

    descricao = fields.Text(
        string='Descrição',
        help='Descrição do centro de responsabilidade'
    )

    ativo = fields.Boolean(
        string='Ativo',
        default=True,
        help='Indica se o centro de responsabilidade está ativo'
    )
