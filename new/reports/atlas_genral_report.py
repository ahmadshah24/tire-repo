from odoo import models, api

class AtlasGenralReportAbstract(models.AbstractModel):
    _name = 'report.genral.atlas'

    @api.model
    def _get_report_values(self, docids, data=None):
        print("\n\n\n\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>", data.get('wizard_data'))
        return {
            'doc_ids': docids,
            'doc_model': 'atlas.general.report.wizard',
            'docs': self.env['atlas.general.report.wizard'].browse(docids),
        }