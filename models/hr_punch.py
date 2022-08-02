from odoo import fields, models, api


class HrPunch(models.Model):
    _name = 'hr.punch'
    _inherit = 'mail.thread'
    _description = 'hr punch'

    emp_id = fields.Many2one('hr.employee', string="اسم الموظف", required=True)
    date = fields.Date(string='تاريخ')
    year = fields.Char(string='عن العام')
    national_id = fields.Char(string="الرقم القومي", store=True, related="emp_id.national_id")
    job_name = fields.Char(string='المسمي الوظيفي', store=True, related="emp_id.job_name")
    partner_id = fields.Many2one(related='emp_id.parent_id', store=True, string='المدير')
    department_id = fields.Many2one(related='emp_id.department_id', store=True, string='القسم')
    qualitative_group = fields.Many2one(related='emp_id.qualitative_group', store=True, string='المجموعة النوعية')
    hr_punch_line_ids = fields.One2many('hr.punch.line', 'punch_id')


class HrPunchLine(models.Model):
    _name = 'hr.punch.line'

    punch_id = fields.Many2one('hr.punch', string="الجزاءات")
    num_resolution = fields.Char('رقم القرار')
    date = fields.Date('تاريخ الجزاء')
    type = fields.Char(string='نوع الجزاء')
    field_name = fields.Binary(string="صورة القرار", attachment=True)
