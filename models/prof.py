# -*- coding: utf-8 -*-
from openerp import models, fields
class Prof(models.Model):
    _name = 'daniel_school.prof'
    _rec_name = 'nom'
    nom = fields.Char(string='Nom Professeur', help="Entrez le nom du professeur",required=True)
    prenoms = fields.Char(string='prenoms Professeur', help="Entrez les prenoms du prof",required=True)
    image = fields.Binary('Photo')
