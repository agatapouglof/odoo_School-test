# -*- coding: utf-8 -*-
from openerp import models, fields
class Filiere(models.Model):
    _name = 'daniel_school.filiere'
    _rec_name = 'nom'
    nom = fields.Char(string='Nom Filiere', help="Entrez le nom de la Filiere",required=True)
    description = fields.Text(string='Description Filiere', help="Entrez Une Description",required=True)
    matiere_in_filiere_id = fields.Many2many('daniel_school.matiere', string="Matieres")
