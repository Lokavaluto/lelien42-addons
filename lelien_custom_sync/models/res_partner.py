from odoo import models, api


class ResPartner(models.Model):
    _inherit = "res.partner"

    @api.model
    def _cron_sync_admin_and_public_data(self):
        contacts = self.env["res.partner"].search([])
        for contact in contacts:
            if contact.is_company and (
                (contact.is_main_profile and contact.public_profile_id)
                or (contact.is_public_profile and contact.contact_id)
            ):
                contact.sync_admin_and_public_data()
