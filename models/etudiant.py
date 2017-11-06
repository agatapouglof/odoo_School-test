# -*- coding: utf-8 -*-
from openerp import models, fields
class Etudiant(models.Model):
    _name = 'daniel_school.etudiant'
    nom = fields.Char(string='Nom Etudiant', help="Entrez le nom de l\'etudiant",required=True)
    prenoms = fields.Char(string='Prenoms  Etudiant', help="Entrez le((s) prenoms(s) de l\'etudiant",required=True)
    _rec_name = 'nom'
    image = fields.Binary('Photo')
    age =  fields.Integer('Age')
    filiere_id = fields.Many2one('daniel_school.filiere',string='filiere')
    # is_done = fields.Boolean('Done?')
    # active = fields.Boolean('Active?', default=True)
