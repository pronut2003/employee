from contact import Contact
from datetime import date
from performance import Performance_KRA
from gender import Gender
import numpy as np

class Employee:
    def __init__(self, id, name):
        try:
            self.emp_id = id
            self.emp_name = name
            self.gender = Gender.MALE
            self.dob = date(2004, 4, 17)
            self.dept = None
            self.desg = None
            self.salary = 0
            self.doj = date(2000, 10, 15)
            self.contact = Contact("9999999999", "xyz@gmail.com")
            self.appraisal = {}
        except (ValueError):
            print("invalid input")

    def __str__(self):
        return (
            f"EID: {self.emp_id}, NAME: {self.emp_name}\n"
            f"GENDER; {self.gender}, DOB: {self.dob}, DOJ: {self.doj}\n"
            f"DEPARTMENT: {self.dept}, DESIGNATION; {self.desg}, SALARY: {self.salary}\n"
            f"CONTACT: {self.contact}\n"
        )

    def set_salary(self, sal):
        if sal >= 10000:
            self.salary = sal
            return True
        else:
            print("invalid salary entered")
            return False

    def set_gender(self, gen):
        if isinstance(gen, Gender):
            self.gender = gen
            return True
        elif isinstance(gen, Gender):
            gender_enum = Gender.from_string(gen)
            if gender_enum:
                self.gender = gender_enum
                return True
        print("invalid gender")
        return False

    def set_dob(self, dob):
        if isinstance(dob, date) and (date.today().year - dob.year > 18):
            self.dob = dob
            return True
        else:
            print("Invalid date of birth")
            return False

    def set_dept(self, dept):
        self.dept = dept

    def set_desg(self, desg):
        self.desg = desg

    def set_doj(self, doj):
        if isinstance(doj, date) and doj <= date.today():
            self.doj = doj
            return True
        else:
            print("invalid date of joining")
            return False

    def set_contact(self, cont):
        if isinstance(cont, Contact):
            self.contact = cont
            return True
        else:
            print("invalid contact")

    def add_appraisal(self, appyear, appvalues):
        self.appraisal[appyear] = appvalues

    def get_performance_value(self, sy, ey):
        g_val = []
        ay = self.get_ay_object(sy, ey)
        if ay is not None:
            grades = list(self.appraisal[ay].values())
            for g in grades:
                g_val.append(Performance_KRA.grades[g])
            a = np.array(g_val)
            b = np.array(Performance_KRA.weightage_values)
            result = a * b
            return sum(result) / 100
        else:
            print("performance_appraisal not available")
            return 0

    def get_ay_object(self, sy, ey):
        for ay, v in self.appraisal.items():
            if ay.sy == sy and ay.ey == ey:
                return ay
        return None

    def print_appraisal_values(self):
        lines = []
        emp_str = str(self.emp_id)
        for ay, val in self.appraisal.items():
            for k, v in val.items():
                lines.append(f"{emp_str},{ay},{k},{v}")
        return lines