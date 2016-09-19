from openerp import models,fields

class ResPartner(models.Model) :
    _inherit = 'res.partner'
    pic = fields.Char()
    group_status = fields.Selection([('Cold', 'Cold'),
                                     ('Hot', 'Hot'),
                                     ('Not Qualifed', 'Not Qualifed'),
                                     ('Warm','Warm')],string="Group Status")