# -*- encoding: utf-8 -*-
from odoo import models, fields


class TriBois(models.Model):
    _name = 'tri.bois'
    _description = 'Lot de bois triés'

    NumLot = fields.Char(string='NumLot')
    Section = fields.Char(string='Section')
    Fournisseur = fields.Char(string='Fournisseur')
    name3 = fields.Char(string='name3')
    name4 = fields.Char(string='name4')
    # description = fields.Text(string='Description')
    # lot_ids = fields.One2many('tri.bois.lot', 'tri_bois_id', string='Lots de Bois')
    # state = fields.Selection([
    #     ('draft', 'Brouillon'),
    #     ('confirmed', 'Confirmé'),
    #     ('done', 'Terminé'),
    #     ('cancelled', 'Annulé')
    # ], default='draft', string='État')