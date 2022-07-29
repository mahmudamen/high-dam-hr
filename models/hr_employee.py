from odoo.exceptions import Warning, UserError
from odoo import fields, models, api, _
from datetime import date, datetime
from dateutil.relativedelta import relativedelta


class HrEmployee(models.Model):
    _inherit = 'hr.employee'
    _description = 'Employee'

    @api.depends('birthday')
    def onchange_age(self):
        for rec in self:
            if rec.birthday:
                d1 = rec.birthday
                d2 = datetime.today().date()
                rd = relativedelta(d2, d1)
                rec.age = str(rd.years) + "y" + " " + str(rd.months) + "m" + " " + str(rd.days) + "d"
            else:
                rec.age = "No Date Of Birth!!"

    national_id = fields.Char(string="الرقم القومي")
    code = fields.Char(string="كود الموظف", required=True)
    age = fields.Char(compute=onchange_age, string="العمر", store=True)
    start_date = fields.Date(string='بدء العمل')
    hiring_date = fields.Date(string='تاريخ التعيين')
    current_status = fields.Selection([('basic', 'اساسي'),
                                       ('mandate', 'منتدب'),
                                       ('loan', 'اعارة'),
                                       ('Appendix', 'ملحق'),
                                       ('stoped', 'متوقف')],
                                      string="الحالة الحالية")
    job_type = fields.Selection([('manager', 'القيادية والاشرافية'),
                                       ('specialist', 'تخصصية'),
                                       ('user', 'فنية ومكتبية'),
                                       ('worker', 'حرفية وخدمات معاونة')],
                                      string="نوع الوظيفة")
    qualitative_group = fields.Many2one('hr.qualitative.group', string='المجموعة النوعية')
    degree = fields.Many2one('hr.degree',string='المؤهل الدراسي')
    level_id = fields.Many2one('hr.level',string='المستوي الوظيفي')
    level_date_got = fields.Date(string='تاريخ الحصول عليها')
    military_status = fields.Many2one('hr.milirary',string='الموقف من التجنيد')
    job_name = fields.Char(string='المسمي الوظيفي')
    sufficiency_report = fields.One2many('hr.sufficiency.report', 'sufficiency_report_id', string='تقرير الكفاية', copy=True, readonly=True,
        states={'draft': [('readonly', False)]})


    @api.onchange('national_id')
    def required_digits(self):
        if self.national_id:
            if len(self.national_id) == 14 and self.national_id.isnumeric():
                return print('true')
            else:
                raise UserError(_("يجب ان يكون الرقم القومي 14 رقما  %s" % self.national_id))

    def print_report(self):
        return self.env.ref('high_dam_hr.action_emp_id_card').report_action(self)

class QualitativeGroup(models.Model):
    _name = 'hr.qualitative.group'
    _rec_name = 'qualitative_group'

    qualitative_group = fields.Char(string='المجموعة النوعية')

class Degree(models.Model):
    _name = 'hr.degree'
    _rec_name = 'name'

    name = fields.Char(string='المؤهل الدراسي')

class Level(models.Model):
    _name = 'hr.level'
    _rec_name = 'name'

    name = fields.Char(string='المستوي الوظيفي')

class Milirary(models.Model):
    _name = 'hr.milirary'
    _rec_name = 'name'

    name = fields.Char(string='الموقف من التجنيد')

