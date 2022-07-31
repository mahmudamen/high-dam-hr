from odoo import fields, models, api
from odoo import tools

class ReportAccountMove(models.Model):
    _name = 'hr.report'
    _auto = False

    name = fields.Many2one('hr.employee',string='اسم الموظف')
    birthday = fields.Date(string="تاريخ الميلاد")
    hiring_date = fields.Date(string='تاريخ التعيين')
    start_date = fields.Date(string='بدء العمل')
    degree = fields.Many2one('hr.degree',string='المؤهل الدراسي')
    job_name = fields.Char(string='المسمي الوظيفي')
    qualitative_group = fields.Many2one('hr.qualitative.group', string='المجموعة النوعية')
    level_id = fields.Many2one('hr.level',string='المستوي الوظيفي')
    level_date_got = fields.Date(string='تاريخ الحصول عليها')
    military_status = fields.Many2one('hr.milirary', string='الموقف من التجنيد')
    partner_ids = fields.Many2many('hr.sufficiency.report', string='الدرجة ')



    def init(self):
        tools.drop_view_if_exists(self._cr, 'hr_report')
        self._cr.execute("""
        create or replace view hr_report as (
        SELECT 
        name ,birthday,hiring_date,start_date,degree,
        job_name,qualitative_group,level_id,level_date_got,
        military_status,partner_ids
        FROM hr_employee  """)