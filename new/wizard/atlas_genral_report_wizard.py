# -*- coding: utf-8 -*-

from odoo import models, fields, api

class AtlasGeneralReportWizard(models.TransientModel):
    _name = 'atlas.genral.report.wizard'
    _description = 'atlas.genral.report.wizard.hello'
    _inherit = 'new.report.genralatlas' 
    

    start_date = fields.Date("Start Date")
    end_date = fields.Date("End Date")

    def print_atlas_general_report(self):
        data = {'start_date': self.start_date, 'end_date': self.end_date}
        report = self.env['new.report.genralatlas']._get_report_values(self.ids, data)
        return self.env.ref('new.action_atlas_genral_report').report_action(self, data=report)

# class AtlasGeneralReportWizard(models.TransientModel):
#     _name = 'atlas.genral.report.wizard'
#     _description = 'atlas.genral.report.wizard.hello'
#     _inherit = 'new.report.genralatlas'

#     start_date = fields.Date("Start Date")
#     end_date = fields.Date("End Date")

#     def print_atlas_general_report(self):
#         data = {'start_date': self.start_date, 'end_date': self.end_date}
#         report = self.env['new.report.genralatlas']._get_report_values(self.ids, data)
#         return self.env.ref('new.action_atlas_genral_report').report_action(self, data=report)



# class AtlasGeneralReportWizard(models.TransientModel):
#     _name = 'atlas.general.report.wizard'
#     _description = 'Atlas General Report Wizard'

#     start_date = fields.Date(string='Start Date')
#     end_date = fields.Date(string='End Date')

#     def print_atlas_general_report(self):
#         data = {'start_date': self.start_date, 'end_date': self.end_date}
#         return self.env.ref('atlas_general_report.action_atlas_general_report').report_action(self, data=data)