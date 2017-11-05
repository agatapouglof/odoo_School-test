# -*- coding: utf-8 -*-
from openerp import models, fields
class Etudiant(models.Model):
    _name = 'daniel_school.etudiant'
    name = fields.Char(string='Nom Etudiant', help="Entrez le nom de l\'etudiant",required=True)
    is_done = fields.Boolean('Done?')
    active = fields.Boolean('Active?', default=True)
