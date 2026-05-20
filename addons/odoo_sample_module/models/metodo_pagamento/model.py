from odoo import models, fields

class MetodoPagamentoModel(models.Model):

    _name = 'app.odoo_sample_module.metodo_pagamento'

    name = fields.Char(
        string='Nome'
    )
