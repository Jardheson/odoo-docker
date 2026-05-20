from odoo import models, fields, api


def validate_forecast_data(forecast_record):
 
    if forecast_record.ano < 1900 or forecast_record.ano > 2100:
        return False
    if not forecast_record.versao:
        return False
    return True


def calculate_forecast_metrics(forecast_record):

    metrics = {
        'ano': forecast_record.ano,
        'versao': forecast_record.versao,
        'cenario': forecast_record.cenario,
    }
    return metrics
