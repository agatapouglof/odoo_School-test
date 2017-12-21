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

    # test onchange ------
    # @api.onchange('filiere_in_note_id') # if these fields are changed, call method
    # @api.depends('filiere_in_note_id')
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
            # matieres_ids = self.pool.get('daniel_school.matiere').search(cr,uid,[('filiere_id' , '=' , filiere_in_note_id)])
            # print matieres_ids
            if students_ids:
                print students_ids
                res = {
                'domain' : {'etudiant_in_note_id' : [('id' , 'in' , students_ids)] },
                'value': {'etudiant_in_note_id' : students_ids[0]}
                 }
            else :
                res = {}

        #     res = {'value': {'nom' : fil[0]['nom']}}
        #
        return res
    #----- end test onchange
