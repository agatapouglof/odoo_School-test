# -*- coding: utf-8 -*-

from openerp import models, fields ,api
import logging
_logger = logging.getLogger(__name__)
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


    # test onchange ------
    # @api.depends('filiere_in_note_id')
    @api.onchange('filiere_in_note_id') # if these fields are changed, call method
    def onchange_filiere(self, cr, uid, ids, filiere_in_note_id, context=None):

        print "on change"
        # print self.matiere_in_note_id.domain
        print filiere_in_note_id
        res = {'value': {'nom' : 'me'}}
        if filiere_in_note_id != False :

            cr.execute("select * from daniel_school_filiere where id=%s", (filiere_in_note_id,)) #  sql query
            fil = cr.dictfetchall()  #  execute and fetch sql query
            print fil
            students_ids = self.pool.get('daniel_school.etudiant').search(cr,uid,[('filiere_id' , '=' , filiere_in_note_id)]) # query with the orm
            matieres_ids = self.pool.get('daniel_school.matiere').search(cr,uid,[])
            matiere = self.pool.get('daniel_school.matiere').browse(cr,uid,matieres_ids)
            _logger.warning(matiere)
            students_values = self.pool.get('daniel_school.etudiant').browse(cr,uid,students_ids)

            _logger.critical('info sur les etudiants')
            _logger.info(students_values[0].filiere_id.matiere_in_filiere_id)
            # matieres_of_student = students_values[0].filiere_id.matiere_in_filiere_id[0].id
            matieres_of_student_ids = students_values[0].filiere_id.matiere_in_filiere_id.mapped('id')
            _logger.warning(matieres_of_student_ids)
            # matieres_ids = self.pool.get('daniel_school.matiere').search(cr,uid,[('filiere_id' , '=' , filiere_in_note_id)])
            # print matieres_ids
            if students_ids:
                print students_ids
                res = {
                'domain' : {'etudiant_in_note_id' : [('id' , 'in' , students_ids)] , 'matiere_in_note_id' : [('id' , 'in' , matieres_of_student_ids)] },
                'value': {'etudiant_in_note_id' : students_ids[0],'matiere_in_note_id' : matieres_of_student_ids[0]}
                 }
            else :
                res = {}

        return res
    #----- end test onchange
