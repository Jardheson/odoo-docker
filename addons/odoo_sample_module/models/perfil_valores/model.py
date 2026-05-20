from odoo import models, fields


class PerfilValores(models.Model):
    """Modelo para Perfil de Valores - Vigências e Valores de Edital"""

    _name = 'perfil.valores'
    _description = 'Perfil Valores'
    _order = 'ano_edital DESC, codigo'

    ano_edital = fields.Integer(
        string='Ano Edital',
        required=True,
        help='Ano do edital'
    )

    codigo = fields.Char(
        string='Código',
        required=True,
        help='Código identificador do perfil de valores'
    )

    valor = fields.Float(
        string='Valor',
        required=True,
        help='Valor do perfil'
    )

    vigencia_inicial = fields.Date(
        string='Vigência Inicial',
        required=True,
        help='Data inicial da vigência'
    )

    vigencia_final = fields.Date(
        string='Vigência Final',
        required=True,
        help='Data final da vigência'
    )

    ativo = fields.Boolean(
        string='Ativo?',
        default=True,
        help='Indica se o perfil de valores está ativo'
    )

    descricao = fields.Text(
        string='Descrição',
        help='Descrição adicional do perfil de valores'
    )
