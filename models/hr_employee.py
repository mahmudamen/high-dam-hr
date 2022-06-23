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

    national_id = fields.Char(string="national Id", required=True)
    code = fields.Char(string="code", required=True)
    age = fields.Char(compute=onchange_age, string="Age", store=True)
    start_date = fields.Date(string='start date')
    hiring_date = fields.Date(string='hiring date')
    current_status = fields.Selection([('basic', 'basic'),
                                       ('mandate', 'mandate'),
                                       ('loan', 'loan'),
                                       ('Appendix', 'Appendix'),
                                       ('stoped', 'stoped')],
                                      string="current status")
    resolution_id = fields.Char(string='resolution id')
    resolution_date = fields.Date(string='resolution date')
    qualitative_group = fields.Many2one('hr.qualitative.group', string='qualitative group')

    @api.onchange('national_id')
    def required_digits(self):
        if len(self.national_id) == 14 and self.national_id.isnumeric():
            return print('true')
        else:
            raise UserError(_("national id must be 14 digits and numbers  %s" % self.national_id))


class QualitativeGroup(models.Model):
    _name = 'hr.qualitative.group'
    _rec_name = 'qualitative_group'

    qualitative_group = fields.Char(string='qualitative group')
