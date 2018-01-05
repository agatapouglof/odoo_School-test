# -*- coding: utf-8 -*-
from openerp import models, fields ,api
from openerp.exceptions import ValidationError
import logging
_logger = logging.getLogger(__name__)
class Etudiant(models.Model):

    _name = 'daniel_school.etudiant'
    nom = fields.Char(string='Nom Etudiant', help="Entrez le nom de l\'etudiant",required=True)
    prenoms = fields.Char(string='Prenoms  Etudiant', help="Entrez le((s) prenoms(s) de l\'etudiant",required=True)
    _rec_name = 'nom'
    image = fields.Binary('Photo')
    sexe = fields.Selection((('M','Masculin'), ('F','Feminin')),'Sexe')
    age =  fields.Integer('Age')
    filiere_id = fields.Many2one('daniel_school.filiere',string='filiere',required=True)
    # is_done = fields.Boolean('Done?')
    # active = fields.Boolean('Active?', default=True)

    # contraintes sur les valeurs des champs a creer
    @api.constrains('nom')
    def _check_name_size(self):
        _logger.error('debug create nom')
        _logger.critical("Use _logger.critical for critical message ")
        _logger.debug('me debugging why not')
        if len(self.nom) < 5 :
            raise ValidationError('le nom doit avoir au moins 5 caracteres')
