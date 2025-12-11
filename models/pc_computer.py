# -*- coding: utf-8 -*-
from odoo import models, fields, api

class PcComputer(models.Model):
    _name = 'pc.computer'
    _description = 'PC Computer'

    name = fields.Char(string='Nombre del PC', required=True)
    description = fields.Text(string='Descripción')
    owner = fields.Char(string='Propietario')
    assembly_date = fields.Date(string='Fecha de montaje')

    component_ids = fields.Many2many(
        'pc.component',
        'pc_computer_component_rel',
        'computer_id',
        'component_id',
        string='Componentes'
    )

    total_price = fields.Float(
        string='Precio total',
        compute='_compute_total_price',
        store=False,
    )

    @api.depends('component_ids.price')
    def _compute_total_price(self):
        for record in self:
            record.total_price = sum(record.component_ids.mapped('price'))
