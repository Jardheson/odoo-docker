from odoo import models, fields, api


class ForecastItens(models.Model):
    """Modelo para Itens do Forecast - Itens de Previsão Orçamentária"""

    _name = 'forecast.itens'
    _description = 'Forecast Itens'
    _order = 'forecast_id, sequence'

    sequence = fields.Integer(
        string='Sequência',
        default=10,
        help='Ordem de exibição do item'
    )

    forecast_id = fields.Many2one(
        comodel_name='forecast.forecast',
        string='Forecast',
        required=True,
        ondelete='cascade',
        help='Forecast ao qual este item pertence'
    )

    perfil_id = fields.Many2one(
        comodel_name='perfil.model',
        string='Perfil',
        help='Perfil associado ao item'
    )

    pessoa_id = fields.Many2one(
        comodel_name='pessoa.model',
        string='Pessoa',
        help='Pessoa associada ao item'
    )

    name = fields.Char(
        string='Descrição',
        required=True,
        help='Descrição do item de forecast'
    )

    memoria_calculo = fields.Text(
        string='Memória de Cálculo',
        help='Documentação sobre como o valor foi calculado'
    )

    observacoes = fields.Text(
        string='Observações',
        help='Observações adicionais sobre o item'
    )

    casa_id = fields.Many2one(
        comodel_name='casa.model',
        string='Casa',
        help='Casa/Casa legislativa associada'
    )

    conta_id = fields.Many2one(
        comodel_name='conta.model',
        string='Conta',
        help='Conta contábil do item'
    )

    unidade_organizacional_id = fields.Many2one(
        comodel_name='unidade.organizacional.model',
        string='Unidade Organizacional',
        help='Unidade organizacional responsável'
    )

    centro_responsabilidade_id = fields.Many2one(
        comodel_name='forecast.centro_responsabilidade',
        string='Centro de Responsabilidade',
        help='Centro de responsabilidade do item'
    )

    cenario = fields.Selection(
        selection=[
            ('otimista', 'Otimista'),
            ('realista', 'Realista'),
            ('pessimista', 'Pessimista'),
        ],
        string='Cenário',
        help='Cenário de previsão'
    )

    state = fields.Selection(
        selection=[
            ('draft', 'Rascunho'),
            ('pending_review', 'Aguardando Revisão'),
            ('approved', 'Aprovado'),
            ('rejected', 'Rejeitado'),
        ],
        string='Status',
        default='draft',
        help='Status do item'
    )

    # Valores mensais
    valor_mes_01 = fields.Float(
        string='Valor Mês 01',
        default=0.0,
        help='Valor previsto para janeiro'
    )

    valor_mes_02 = fields.Float(
        string='Valor Mês 02',
        default=0.0,
        help='Valor previsto para fevereiro'
    )

    valor_mes_03 = fields.Float(
        string='Valor Mês 03',
        default=0.0,
        help='Valor previsto para março'
    )

    valor_mes_04 = fields.Float(
        string='Valor Mês 04',
        default=0.0,
        help='Valor previsto para abril'
    )

    valor_mes_05 = fields.Float(
        string='Valor Mês 05',
        default=0.0,
        help='Valor previsto para maio'
    )

    valor_mes_06 = fields.Float(
        string='Valor Mês 06',
        default=0.0,
        help='Valor previsto para junho'
    )

    valor_mes_07 = fields.Float(
        string='Valor Mês 07',
        default=0.0,
        help='Valor previsto para julho'
    )

    valor_mes_08 = fields.Float(
        string='Valor Mês 08',
        default=0.0,
        help='Valor previsto para agosto'
    )

    valor_mes_09 = fields.Float(
        string='Valor Mês 09',
        default=0.0,
        help='Valor previsto para setembro'
    )

    valor_mes_10 = fields.Float(
        string='Valor Mês 10',
        default=0.0,
        help='Valor previsto para outubro'
    )

    valor_mes_11 = fields.Float(
        string='Valor Mês 11',
        default=0.0,
        help='Valor previsto para novembro'
    )

    valor_mes_12 = fields.Float(
        string='Valor Mês 12',
        default=0.0,
        help='Valor previsto para dezembro'
    )

    total_ano = fields.Float(
        string='Total Ano',
        compute='_compute_total_ano',
        store=True,
        help='Total anual (soma de todos os meses)'
    )

    @api.depends('valor_mes_01', 'valor_mes_02', 'valor_mes_03', 'valor_mes_04',
                 'valor_mes_05', 'valor_mes_06', 'valor_mes_07', 'valor_mes_08',
                 'valor_mes_09', 'valor_mes_10', 'valor_mes_11', 'valor_mes_12')
    def _compute_total_ano(self):
        """Calcula o total anual somando todos os valores mensais"""
        for record in self:
            record.total_ano = sum([
                record.valor_mes_01, record.valor_mes_02, record.valor_mes_03,
                record.valor_mes_04, record.valor_mes_05, record.valor_mes_06,
                record.valor_mes_07, record.valor_mes_08, record.valor_mes_09,
                record.valor_mes_10, record.valor_mes_11, record.valor_mes_12,
            ])

    created_at = fields.Datetime(
        string='Criado em',
        default=lambda self: fields.Datetime.now(),
        readonly=True
    )

    updated_at = fields.Datetime(
        string='Atualizado em',
        default=lambda self: fields.Datetime.now(),
    )

    @api.model
    def create(self, vals):
        vals['updated_at'] = fields.Datetime.now()
        return super().create(vals)

    def write(self, vals):
        vals['updated_at'] = fields.Datetime.now()
        return super().write(vals)
