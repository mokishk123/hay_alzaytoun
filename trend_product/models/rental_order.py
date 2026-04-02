from odoo import models, fields

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    project_list_id = fields.Many2one(
        'project.project',
        string='Project',
        tracking=True,
    )

    is_real_estate_relative = fields.Boolean(
        string='Is Real Estate Relative',
        default=False,
        tracking=True,
    )
