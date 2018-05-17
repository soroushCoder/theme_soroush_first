# -*- coding: utf-8 -*-
from odoo import fields, models
class ecommerceproduct(models.Model):
    _inherit = 'product.template'
    recommended_product =  fields.Boolean("recommended_product", default=True)
