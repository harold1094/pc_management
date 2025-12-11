# -*- coding: utf-8 -*-
from odoo import models, fields

class PcComponent(models.Model):
    _name = 'pc.component'
    _description = 'PC Component'

    name = fields.Char(string='Nombre', required=True)
    component_type = fields.Selection(
        [
            ('cpu', 'CPU'),
            ('gpu', 'GPU'),
            ('ram', 'RAM'),
            ('storage', 'Almacenamiento'),
            ('psu', 'Fuente de alimentación'),
            ('mb', 'Placa base'),
            ('case', 'Torre'),
            ('other', 'Otro'),
        ],
        string='Tipo',
        required=True,
        default='other',
    )
    brand = fields.Char(string='Marca')
    price = fields.Float(string='Precio')
    stock = fields.Integer(string='Stock')

    computer_ids = fields.Many2many(
        'pc.computer',
        'pc_computer_component_rel',
        'component_id',
        'computer_id',
        string='Ordenadores que lo usan',
    )
