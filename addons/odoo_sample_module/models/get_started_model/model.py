from odoo import models, fields

class GetStartedModel(models.Model):

    _name = 'app.odoo_sample_module.get_started_model'

    name = fields.Char(
        string='Nome'
    )
