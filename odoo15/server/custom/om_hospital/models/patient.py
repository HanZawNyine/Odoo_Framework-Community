# -*- coding: utf-8 -*-
from odoo import api, fields, models, _, tools,api


class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Hospital Patient"

    name = fields.Char(string='Name', required=True, translate=True, tracking=True)
    age = fields.Char(string='Age', required=True, translate=True, tracking=True)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ], required=True, default='other', tracking=True)
    note = fields.Text(string='Description', tracking=True)
    state = fields.Selection([('draft', 'Draft'), ('confirm', 'Confirmed'),
                              ('done', 'Done'), ('cancel', 'Cancel')],
                             default='draft', string="Status", tracking=True)
    responsible_id = fields.Many2one(comodel_name='res.partner', string='Responsible')

    def action_confirm(self):
        self.state = 'confirm'

    def action_done(self):
        self.state = 'done'

    def action_draft(self):
        self.state = 'draft'

    def action_cancel(self):
        self.state = 'cancel'

    @api.model
    def create(self, vals):
        # print("success override create method")
        if not vals.get("note"):
            vals["note"] = 'New Patient'
        res = super(HospitalPatient,self).create(vals)
        return res
