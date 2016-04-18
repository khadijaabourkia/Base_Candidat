# -*- coding: utf-8 -*-
##############################################################################
#    
# Module : base_candidat
# Créé le : 2013-06-06 par Thierry Godin
#
# Module permettant la création de vendeurs pour les points de vente
#
##############################################################################
import openerp
from openerp import netsvc, tools, pooler
from openerp.osv import fields, osv
from openerp.tools.translate import _
import time

class base_candidat(osv.osv):
    _name = 'base.candidat'
    _order = 'candidat_name asc'
    _inherit = ['mail.thread', 'ir.needaction_mixin']
    _columns = {
        'candidat_name': fields.char('Candidat', size=128, required=True),
        'active': fields.boolean('Active', help="If a candidat is not active, it will not be displayed in module"),
        'email': fields.char('Email', size=32),
		'mobile': fields.char('Mobile', size=32),
		'description': fields.text('Description'),
        'probability': fields.float('Probability'),
        'create_date': fields.datetime('Creation Date', readonly=True, select=True),
        'write_date': fields.datetime('Update Date', readonly=True),
        'categ_ids': fields.many2many('hr.applicant_category', string='Tags'),
        'date_closed': fields.datetime('Closed', readonly=True, select=True),
        'date_open': fields.datetime('Assigned', readonly=True, select=True),
        'date_last_stage_update': fields.datetime('Last Stage Update', select=True),
        'date_action': fields.date('Next Action Date'),
        'title_action': fields.char('Next Action', size=64),
        'priority': fields.selection(AVAILABLE_PRIORITIES, 'Appreciation'),
        'type_id': fields.many2one('hr.recruitment.degree', 'Degree'),
        'reference': fields.char('Referred By'),
        'source_id': fields.many2one('hr.recruitment.source', 'Source'),
        'color': fields.integer('Color Index'),
		'user_id': fields.many2one('res.users', 'Responsable'),
	}

    _defaults = {
        'candidat_name' : '',
        'active' : True,
        'priority': '0',
    }

    _sql_constraints = [
        ('uniq_name', 'unique(candidat_name)', "A candidate already exists with this name in this database."),
    ]

    def action_get_attachment_tree_view(self, cr, uid, ids, context=None):
        model, action_id = self.pool.get('ir.model.data').get_object_reference(cr, uid, 'base', 'action_attachment')
        action = self.pool.get(model).read(cr, uid, action_id, context=context)
        action['context'] = {'default_res_model': self._name, 'default_res_id': ids[0]}
        action['domain'] = str(['&', ('res_model', '=', self._name), ('res_id', 'in', ids)])
        return action



