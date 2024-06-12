from odoo import fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    fond_de_tresorerie = fields.Monetary(string="Fond de trésorerie")
    nbr_etp = fields.Text(string="Nombre d'ETP")
    needs = fields.Text(string="Besoins et difficultés")
    nombre_salarie = fields.Text(string="Nombre de salarié.es")
    projects = fields.Text(string="Projets en cours")
    ressources = fields.Text(string="Ressources et Compétences")
    ancrage_activite = fields.Text(string="Description détaillée de l'activité")
    citizen_futur = fields.Text(string="Ce que je voudrais faire")
    citizen_now = fields.Text(string="Ce que je fais")
    commercial_partners = fields.Text(string="Ce que je fais")
    digital = fields.Boolean(string="Utilise le LIEN numérique")
    empreinte_futur = fields.Text(string="Ce que je voudrais faire")
    empreinte_now = fields.Text(string="Ce que je fais")
    exemption3prct = fields.Date(string="Date de fin d'exemption 3%")
    last_ancrage = fields.Date(string="Date de l'ancrage")
    legal_status = fields.Char(string="Statut Juridique")
    paper = fields.Boolean(string="Utilise le LIEN papier")
    reductions = fields.Boolean(string="Réduction")
    relocalisation_futur = fields.Text(string="Ce que je voudrais faire")
    relocalisation_now = fields.Text(string="Ce que je fais")
    social_futur = fields.Text(string="Ce que je voudrais faire")
    social_now = fields.Text(string="Ce que je fais")
    table_info = fields.Text(string="Tables d'info")

