from odoo import models, api

class AtlasGenralReportAbstract(models.AbstractModel):
    _name = 'new.report.genralatlas'
    

    @api.model
    def _get_report_values(self, docids, data=None):
        return_records = self.env['return.return'].search([])
        costumer_records = self.env['costumerinfo.costumerinfo'].search([])
        product_records = self.env['atlas.product'].search([])
        
        report_data = {
            'return_records': return_records,
            'costumer_records': costumer_records,
            'product_records': product_records,
            'doc_ids': docids,
            'doc_model': 'atlas.general.report.wizard',
            'docs': self.env['atlas.general.report.wizard'].browse(docids),
        }

        report_template = 'new.report_genralatlas_template'
        return {
            'data': report_data,
            'template': report_template,
        }
