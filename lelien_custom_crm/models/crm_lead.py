from odoo import fields, models

class CrmLead(models.Model):
    _inherit = "crm.lead"

    contact_name = fields.Char('Contact Name', tracking=30, store=True)
    
    def _compute_contact_name(self):
        # Override the method computing contact_name
        # in order to not modify the contact_name when client changes
        return
