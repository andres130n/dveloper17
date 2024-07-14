#-*- coding:utf-8 -*-

from odoo import fields, models, api 

class Presupuesto(models.Model):
    _name = "presupuesto"
    #_inherit = ['image.mixin']

    name = fields.Char(string='Pelicula')
    clasificacion = fields.Selection(selection=[
        ('G', 'G'), #Publico en General
        ('PG', 'PG'), # se requiere la compañia de un adulto 
        ('PG-13', 'PG-13'), # Mayores de 13 años 
        ('R', 'R'), # EN compañia de un adulto 
        ('NC-17', 'NC-17'), #Mayores de 18
    ], string='Clasificacion')
    fch_estreno = fields.Date(string='Fecha Estreno')
    puntuacion = fields.Integer(string='Puntuacion')
    active = fields.Boolean(string='Activo', default=True)
    director_id = fields.Many2one(
        comodel_name='res.partner',
        string='Director'
    )
    genero_ids = fields.Many2many(
        comodel_name='genero',
        string='Genero'
    )
    vista_general = fields.Text(string='Descripcion')
    link_trailes = fields.Char(string='Trailer')
    es_libro = fields.Boolean(string='Version Libro')
    libro = fields.Binary(string='libro')