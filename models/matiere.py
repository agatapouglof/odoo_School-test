# -*- coding: utf-8 -*-
from openerp import models, fields
class Matiere(models.Model):
    _name = 'daniel_school.matiere'
    _rec_name = 'nom'
    nom = fields.Char(string='Nom De La matiere', help="Entrez le nom de la matiere",required=True)
    description = fields.Char(string='Description matiere', help="Description de la matiere",required=True)
    # filiere_in_matiere_id = fields.Many2many('daniel_school.filiere', ondelete='set null', string="Fielere", index=True)
