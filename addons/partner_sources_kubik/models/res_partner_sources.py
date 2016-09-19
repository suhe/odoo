from openerp import fields,models

class ResPartnerSources(models.Model):
    _name = 'res.partner.sources'
    _order = 'source asc'
    source = fields.Char(string="Source",required=True)