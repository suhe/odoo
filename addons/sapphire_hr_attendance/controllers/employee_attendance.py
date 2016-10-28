from datetime import datetime
from openerp.report import report_sxw
import time

class employee_attendance(report_sxw.rml_parse):
    def __init__(self, cr, uid, name, context):
        super(employee_attendance, self).__init__(cr, uid, name, context=context)
        cr.execute(
            "select * from employee "
        )
        self.localcontext.update({
            'time': time,
            'get_month': self.get_month,
        })

        report_sxw.report_sxw('report.webkit.emp_attendance',
                          'hr.attendance',
                          'saphire_hr_attendance/report/employee_attendance.mako',
                          parser=employee_attendance)

    def get_month(self, id):
        acnt_rec = self.pool.get('account.period').browse(self.cr, self.uid, id)
        dt = acnt_rec.name
        dt = datetime.strptime(dt.__str__(), "%m/%Y")
        return datetime.strptime((dt.date().__str__()), "%Y-%m-%d").strftime("%B") + "-" + datetime.strptime(
            (dt.date().__str__()), "%Y-%m-%d").strftime("%Y")

