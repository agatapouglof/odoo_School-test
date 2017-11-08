# -*- coding: utf-8 -*-
from openerp import models, fields ,api
class Note(models.Model):
    _name = 'daniel_school.note'
    _rec_name = 'nom'
    filiere_in_note_id  = fields.Many2one('daniel_school.filiere',string='filiere')
    matiere_in_note_id  = fields.Many2one('daniel_school.matiere',string='matiere')
    # etudiant_in_note_id = fields.Char(string="etudiants de la filiere")
    etudiant_in_note_id = fields.Many2one('daniel_school.etudiant',string='etudiant')
    select_etudiant_in_filiere = fields.Char(string='select_etudiant')
    nom = fields.Char(string='Nom De La note', help="Entrez le nom de la matiere",required=True)
    valeur = fields.Integer('Note')
    # description = fields.Char(string='Description matiere', help="Description de la note",required=True)
    # filiere_in_matiere_id = fields.Many2many('daniel_school.filiere', ondelete='set null', string="Fielere", index=True)


        #  return {'values':{'etudiant_in_note_id':students}}
        #   Obj = self.env['daniel_school.etudiant'].browse(1)
        #   get_etudiant = Obj
        #   self.etudiant_in_note_id = get_etudiant
    #   return {'values':{'etudiant_in_note_id':'','matiere_in_note_id':''}}

    # @api.depends('filiere_in_note_id')
    # def select_etudiant(self):
    #     for record in self:
    #         if record.filiere_in_note_id
    #         record.total = record.value + record.value * record.tax
