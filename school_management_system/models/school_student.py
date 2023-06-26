from odoo import models, fields, api, _

class SchoolStudent(models.Model):
    _name = 'school.student'
    _description = 'school student'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name= fields.Char('Student Name', required=True)
    class_id= fields.Many2one(comodel_name="school.class", string="Class", required=True)
    year=fields.Integer(related="class_id.year_id.year_num" ,string='Year')
    subject_ids= fields.One2many(comodel_name="school.subject",inverse_name="student_id" ,string="Subject", required=True)

