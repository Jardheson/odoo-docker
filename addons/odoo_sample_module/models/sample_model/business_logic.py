from odoo import api, models, fields, tools, _
from odoo.exceptions import ValidationError


class SampleModelBusinessLogic(models.Model):

    _name = 'app.odoo_sample_module.sample_model'
    _inherit = ['app.odoo_sample_module.sample_model']

    @api.depends('sample_item_model_ids')
    def _compute_total(self):
        for record in self:
            record.total = sum([item.subtotal for item in record.sample_item_model_ids])

    @api.onchange('name')
    def _onchange_name(self):
        self.descricao = self.name

    @api.constrains('numero_inteiro')
    def _check_numero_inteiro(self):
        for record in self:
            if record.numero_inteiro <= 0:
                raise ValidationError('Número inteiro deve ser maior que zero!')

    def action_set_state_pendente(self):
        self.state = 'pendente'
        return True

    def action_set_state_concluido(self):
        self.state = 'concluido'
        return True

    def action_set_state_cancelado(self):
        self.state = 'cancelado'
        return True
