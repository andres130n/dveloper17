# -*- coding:utf-8 -*-

from odoo import fields, models, api


class Medico(models.Model):
    _name = "medico"

    name = fields.Char()
    cedula = fields.Char()
    correo = fields.Char()
    direccion = fields.Char()
    telefono = fields.Char()
    celular = fields.Char()
    


class MedicoDetalle(models.Model):
    _name = "medico.detalle"

    medico_id = fields.Many2one(
        comodel_name='medico',
        string='Medico',
    )

    fecha = fields.Datetime(string='Fecha aprobado', copy=False)
    tipo_beneficio = fields.Selection(selection=[
        ('ninguna', 'Ninguna'),
        ('comision', 'Comision'),
        ('descuento', 'Descuento'),
    ], default='ninguna', string='Tipo de Beneficio', copy=False)    
    comision = fields.Float(string='% Comision', default=0.0, digits=(16, 4))
    convenio = fields.Float(string='% Convenio', default=0.0, digits=(16, 4))
