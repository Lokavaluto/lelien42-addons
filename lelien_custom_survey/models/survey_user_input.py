from odoo import fields, models

class SurveyUserInput(models.Model):
    _inherit = "survey.user_input"

    state = fields.Selection(selection_add=[("traited", "Traité")])
    