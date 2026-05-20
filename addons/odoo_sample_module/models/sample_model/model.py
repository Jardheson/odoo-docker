from odoo import api, models, fields

from datetime import datetime


class SampleModelModel(models.Model):

    _name = 'app.odoo_sample_module.sample_model'
    _inherit = ['mail.thread']

    @api.model
    def default_get(self, fields) -> dict:
        result = super(SampleModelModel, self).default_get(fields)
        result.update(dict(
            company_id=self.env.user.company_id.id,
            user_id=self.env.user.id
        ))
        return result

    @api.model
    def _get_default_data(self):
        
        return datetime.now().date()

  

    name = fields.Char(
        string='Nome', 
        size=100, 
        required=True, 
        help='Informa o nome do registro'
    )

    descricao = fields.Char(
        string='Descrição'
    )

    data = fields.Date(
        string='Data',
        required=True,
        default=_get_default_data 
    )

    partner_id = fields.Many2one(
        string='Pessoa',
        comodel_name='res.partner',
        required=True
    )

    user_id = fields.Many2one(
        string='Usuário',
        comodel_name='res.users'
    )

    company_id = fields.Many2one(
        string='Empresa',
        comodel_name='res.company'
    )

    total = fields.Float(
        string='Valor Total',
        compute='_compute_total',
        store=True
    )

    numero_inteiro = fields.Integer(
        string='Número Inteiro',
        default=0
    )

    state = fields.Selection(
        string='Situação',
        selection=[ 
            ('pendente', 'Pendente'),
            ('concluido', 'Concluído'),
            ('cancelado', 'Cancelado'),
        ],
        help='''Indica o estado do registro:
            * Pendente: ...
            * Conclído: ...
            * Cancelado: ...
        ''',
        tracking=True 
    )

    sample_item_model_ids = fields.One2many(
        string='Modelo de Exemplo',
        comodel_name='app.odoo_sample_module.sample_item_model',
        inverse_name='sample_model_id'
    )
