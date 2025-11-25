class Employee_manager:
    def __init__(self):
        self.employees = []

    def add_emp(self, e):
        if self.does_id_exist(e.emp_id):
            print("employee already exists")
            return False
        if self.does_name_exist(e.emp_name):
            print("employee name already exists")
            return False
        self.employees.append(e)
        print("employee added successfully")
        print(f"no of employees:{len(self.employees)}")
        return True

    def display_emp(self):
        for emp in self.employees:
            print(emp)

    def does_id_exist(self, id):
        for e in self.employees:
            if e.emp_id == id:
                return True
        return False

    def does_name_exist(self, name):
        for e in self.employees:
            if e.emp_name == name:
                return True
        return False

    def write_appraisal_log(self, fname):
        with open(fname, "w") as file:
            line = f"EMP_ID,APPRAISAL_YEAR,PARAMETER,GRADE\n"
            file.write(line)
            for emp in self.employees:
                for appr_line in emp.print_appraisal_values():
                    file.write(appr_line + "\n")

    def get_bonus_percentage(self, x):
        if x >= 4.5:
            return .2
        elif x >= 4:
            return .15
        elif x >= 3.5:
            return .1
        elif x >= 3:
            return .05
        else:
            return 0

    def write_bonus_log(self, fname, sy, ey):
        with open(f"{fname}_{sy}-{ey}.csv", "w") as file:
            line = f"EMP_ID,APPRAISAL_YEAR,SALARY,APPRAISAL_VALUE,BONUS_PERCENTAGE,BONUS_AMOUNT\n"
            file.write(line)
            for emp in self.employees:
                x = emp.get_performance_value(sy, ey)
                ay_obj = emp.get_ay_object(sy, ey)
                if ay_obj is not None:
                    bonus_amount = emp.salary * self.get_bonus_percentage(x)
                    line = f"{emp.emp_id},{ay_obj},{emp.salary},{x},{self.get_bonus_percentage(x)*100},{bonus_amount}\n"
                else:
                    line = f"{emp.emp_id},{emp.salary},\n"
                file.write(line)


