from openerp import models,fields

class ResPartner(models.Model) :
    _inherit = 'res.partner'
    pic = fields.Char()
    pic_position = fields.Char(string="Position")
    customer_from = fields.Selection([("Mandiri", "Mandiri"), ("Manajemen", "Manajemen")],
                              string="From")
    status = fields.Selection([("Prospek Client","Prospek Client"),("Existing Client","Existing Client")],string="Status")
    group_status = fields.Selection([('Cold', 'Cold'),
                                     ('Hot', 'Hot'),
                                     ('Not Qualifed', 'Not Qualifed'),
                                     ('Warm','Warm')],
                                    string="Group Status")
    phone_ext = fields.Char(string="Phone Extension")