# -*- coding: utf-8 -*-

from odoo import models,fields, api

class modelo(models.Model):
    _name = "todo_app"
    _description = "Lista de Tareas"

    name = fields.Char(string ="Nombre")
    #state = fields.Char(string ="Estado")
    description = fields.Char(string="Descripción")
    