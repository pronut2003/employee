from datetime import date
from datetime import datetime
from employee_class import Employee
from employee_manager import Employee_manager
from contact import Contact
from appyear import AppYear
from performance import Performance_KRA
from gender import Gender
from models import Employee
from mongoengine import connect

'''connect(
    db="employeedb",
    host="mongodb+srv://admin:admin@cluster0.teul3as.mongodb.net/?appName=Cluster0"
)'''

em = Employee_manager()


def displaymenu():
    print("enter your choice between 1 to 12 ")
    print("1.ADD employee")
    print("2.SEARCH employee")
    print("3.UPDATE employee")
    print("4.DELETE employee")
    print("5.DISPLAY all employees")
    print("6.ATTENDANCE log")
    print("7.SORT employee data")
    print("8.FILTER employee data")
    print("9.APPRAISAL log")
    print("10.BONUS LOG")
    print("11.PROMOTION log")
    print("12.EXIT")
    choice = int(input("enter your choice"))
    return choice


def sort_sub_menu():
    print("0.Sort by ID")
    print("1.Sort by name")
    print("2.Sort by salary")
    print("3.Sort by date of birth")
    print("4.Sort by date of joining")
    choice = int(input("enter your choice"))
    return choice


def filter_sub_menu():
    print("1.Filter by department")
    print("2.Filter by designation")
    print("3.Filter by gender")
    print("4.Filter by Salary")
    choice = int(input("enter your choice"))
    return choice


def search_sub_menu():
    print("1.search by ID")
    print("2.search by NAME")
    choice = int(input("enter your choice"))
    return choice


def update_sub_menu():
    print("1.update by ID")
    print("2.update by NAME")
    print("3.update by DESIGNATION")
    choice = int(input("enter your choice"))
    return choice


def search_employee_name(name):
    for emp in em.employees:
        if (name == emp.emp_name):
            return emp


def search_employee_ID(eid):
    for emp in em.employees:
        if (eid == emp.emp_id):
            return emp


def filter_employee_dept(dept):
    emp_list = []
    for emp in em.employees:
        if (emp.dept == dept):
            emp_list.append(emp)
    return emp_list


def filter_employee_desg(desg):
    emp_list = []
    for emp in em.employees:
        if (emp.desg == desg):
            emp_list.append(emp)
    return emp_list

def filter_employee_salary(salary):
    emp_list = []
    for emp in em.employees:
        if (salary > emp.salary):
            emp_list.append(emp)
    return emp_list


def filter_employee_gender(gender):
    emp_list = []
    gender_enum = Gender.from_string(gender)
    if gender_enum:
        for emp in em.employees:
            if (emp.gender == gender_enum):
                emp_list.append(emp)
    return emp_list


def read_file(filename):
    with open(filename, "r") as file:
        lines = file.readlines()
        for line in lines[1:]:
            line_list = line.strip().split(",")
            emp = Employee(int(line_list[0]), line_list[1])

            gender_str = line_list[2].replace("Gender.", "")
            emp.set_gender(gender_str)

            dob_list = line_list[3].split("-")
            dob_day = int(dob_list[2])
            dob_month = int(dob_list[1])
            dob_year = int(dob_list[0])
            dob_obj = date(dob_year, dob_month, dob_day)
            emp.set_dob(dob_obj)

            emp.set_dept(line_list[4])
            emp.set_desg(line_list[5])
            emp.set_salary(int(line_list[6]))

            doj_list = line_list[7].split("-")
            doj_day = int(doj_list[2])
            doj_month = int(doj_list[1])
            doj_year = int(doj_list[0])
            doj_obj = date(doj_year, doj_month, doj_day)
            emp.set_doj(doj_obj)

            emp.set_contact(Contact(line_list[8], line_list[9]))
            em.add_emp(emp)


def write_to_file(fname, emp):
    with open(fname, "a") as file:
        line = f"{emp.emp_id},{emp.emp_name},{emp.gender},{emp.dob},{emp.dept},{emp.desg},{emp.salary},{emp.doj},{emp.contact}\n"
        file.write(line)


def is_file_empty(fname):
    with open(fname, "r") as file:
        lines = file.readlines()
        if len(lines) == 0:
            with open(fname, "w") as file1:
                line = f"ID,NAME,GENDER,DOB,DEPARTMENT,DESIGNATION,SALARY,DOJ,PHONE,EMAIL\n"
                file1.write(line)
                return True


def write_all_to_file(fname):
    with open(fname, "w") as file:
        line = f"ID,NAME,GENDER,DOB,DEPARTMENT,DESIGNATION,SALARY,DOJ,PHONE,EMAIL\n"
        file.write(line)
        for emp in em.employees:
            line = f"{emp.emp_id},{emp.emp_name},{emp.gender},{emp.dob},{emp.dept},{emp.desg},{emp.salary},{emp.doj},{emp.contact}\n"
            file.write(line)


def validate_gender(gender):
    return Gender.from_string(gender) is not None


def write_attendance_tofile(emp_id):
    with open("attendance.csv", "a") as file:
        emp = search_employee_ID(emp_id)
        if emp is not None:
            x = input("1.clockin \n2.clockout\n")
            file.write(f"{emp_id},{date.today()},{x},{datetime.now().time()}\n")
            print(f"attendance successfully recorded for emp_id : {emp_id}")
        else:
            print("invalid employee ID")


def validate_phone():
    repeat = True
    while repeat:
        phone = input("enter your 10 digit number")
        if (len(phone) == 10 and phone.isdigit()):
            return phone
        else:
            print("invalid phone number")


def validate_email():
    while True:
        email = input("enter email id")
        if "@" in email and "." in email and " " not in email:
            return email.lower()
        else:
            print("invalid email id")


def get_emp_details(id):
    name = input("enter your name")
    emp = Employee(id, name)
    gender = input("enter your gender - MALE/FEMALE/OTHERS")
    yob = int(input("enter year of birth"))
    mob = int(input("enter month of birth"))
    dob = int(input("enter date of birth"))
    dob_obj = date(yob, mob, dob)
    emp.set_dept(input("enter your department"))
    emp.set_desg(input("enter your designation"))
    emp.set_salary(int(input("enter your salary")))
    yoj = int(input("enter year of joining"))
    moj = int(input("enter month of joining"))
    doj = int(input("enter day of joining"))
    doj_obj = date(yoj, moj, doj)
    phone = validate_phone()
    email = validate_email()
    contact = Contact(phone, email)
    emp.set_dob(dob_obj)
    emp.set_doj(doj_obj)
    emp.set_contact(contact)
    emp.set_gender(gender)
    return emp


def aynotexist(emp, sy, ey):
    for ay in emp.appraisal.keys():
        if ay.sy == sy and ay.ey == ey:
            return False
    return True


def record_appraisal(emp):
    repeat = True
    ay = None
    while repeat:
        sy = int(input("enter start year"))
        ey = int(input("enter end year"))
        ay = AppYear()
        if (ay.set_sy(sy) and ay.set_ey(ey) and aynotexist(emp, sy, ey)):
            repeat = False
    repeat = True
    grades = []
    while repeat:
        print(
            f"enter the grades A/B/C/D/E for each of the performance parameters for appraisal year {ay} for employee ID {emp.emp_id}")
        p = input("enter grade for PRODUCTIVITY")
        q = input("enter grade for QUALITY")
        b = input("enter grade for BEHAVIORAL")
        e = input("enter grade for ENGAGEMENT")
        i = input("enter grade for INNOVATION")
        g = input("enter grade for GROWTH AND LEARNING")
        l = input("enter grade for LEADERSHIP")
        grades.extend([p, q, b, e, i, g, l])
        if all(g in Performance_KRA.allowed_grades for g in grades):
            repeat = False
        else:
            print("invalid grades , enter again")
    app_values = dict(zip(Performance_KRA.acronyms, grades))
    emp.add_appraisal(ay, app_values)
    em.write_appraisal_log("appraisal_log.csv")


def read_appraisal_log_file(fname):
    try:
        with open(fname) as file:
            lines = file.readlines()
            for line in lines[1:]:
                line_list = line.strip().split(",")
                if len(line_list) >= 4:
                    emp_id = int(line_list[0])
                    emp = search_employee_ID(emp_id)
                    if emp:
                        year_range = line_list[1].split("-")
                        if len(year_range) == 2:
                            sy = int(year_range[0])
                            ey = int(year_range[1])
                            param = line_list[2]
                            grade = line_list[3]

                            ay = emp.get_ay_object(sy, ey)
                            if not ay:
                                ay = AppYear()
                                ay.set_sy(sy)
                                ay.set_ey(ey)
                                emp.appraisal[ay] = {}

                            emp.appraisal[ay][param] = grade
    except FileNotFoundError:
        pass


def write_promotion_log(fname):
    with open(fname, "w") as file:
        line = f"EMP_ID,NAME,CURRENT_DESIGNATION,CURRENT_SALARY,ELIGIBLE_FOR_PROMOTION\n"
        file.write(line)
        for emp in em.employees:
            if len(emp.appraisal) > 0:
                latest_ay = list(emp.appraisal.keys())[-1]
                perf_value = emp.get_performance_value(latest_ay.sy, latest_ay.ey)
                eligible = "YES" if perf_value >= 4.0 else "NO"
            else:
                eligible = "NO"
            line = f"{emp.emp_id},{emp.emp_name},{emp.desg},{emp.salary},{eligible}\n"
            file.write(line)


def main():
    read_file("emp_data.csv")
    read_appraisal_log_file("appraisal_log.csv")
    repeat = True
    while repeat:
        choice = displaymenu()

        # add employee
        if (choice == 1):
            id = int(input("enter employee id"))
            if em.does_id_exist(id):
                print(f"employee with id {id} already exists")
            else:
                new_emp = get_emp_details(id)
                if em.add_emp(new_emp):
                    is_file_empty("emp_data.csv")
                    write_to_file("emp_data.csv", new_emp)

        # search employee
        if (choice == 2):
            sub_choice = search_sub_menu()
            if (sub_choice == 2):
                name = input("enter name of an employee")
                emp = search_employee_name(name)
                if emp is None:
                    print(f"employee with this name:{name} does not exist")
                else:
                    print(emp)
            if (sub_choice == 1):
                eid = int(input("enter employee id to search"))
                emp = search_employee_ID(eid)
                if emp is None:
                    print(f"employee with this id:{eid} does not exist")
                else:
                    print(emp)

        # update employee
        if (choice == 3):
            sub_choice = update_sub_menu()

            if (sub_choice == 1):  # update by ID
                id = int(input("enter employee id to update"))
                if em.does_id_exist(id):
                    new_emp = get_emp_details(id)
                    old_emp = search_employee_ID(id)
                    old_emp.emp_name = new_emp.emp_name
                    old_emp.set_gender(new_emp.gender)
                    old_emp.set_dob(new_emp.dob)
                    old_emp.set_dept(new_emp.dept)
                    old_emp.set_desg(new_emp.desg)
                    old_emp.set_salary(new_emp.salary)
                    old_emp.set_doj(new_emp.doj)
                    old_emp.set_contact(new_emp.contact)
                    print(f"employee with id:{id} updated successfully")
                    write_all_to_file("emp_data.csv")
                else:
                    print("id does not exist to update employee details")

            if (sub_choice == 2):  # update by NAME
                name = input("enter employee name to update")
                emp = search_employee_name(name)
                if emp is not None:
                    new_emp = get_emp_details(emp.emp_id)
                    emp.emp_name = new_emp.emp_name
                    emp.set_gender(new_emp.gender)
                    emp.set_dob(new_emp.dob)
                    emp.set_dept(new_emp.dept)
                    emp.set_desg(new_emp.desg)
                    emp.set_salary(new_emp.salary)
                    emp.set_doj(new_emp.doj)
                    emp.set_contact(new_emp.contact)
                    print(f"employee with name:{name} updated successfully")
                    write_all_to_file("emp_data.csv")
                else:
                    print(f"employee with name:{name} does not exist")

            if (sub_choice == 3):  # update by DESIGNATION
                desg = input("enter designation to update")
                emp_list = filter_employee_desg(desg)
                if len(emp_list) == 0:
                    print(f"no employees with designation:{desg}")
                else:
                    print(f"list of {len(emp_list)} employees with designation:{desg}")
                    for idx, emp in enumerate(emp_list):
                        print(f"{idx + 1}. {emp.emp_name} (ID: {emp.emp_id})")

                    emp_choice = int(input("select employee number to update"))
                    if (emp_choice > 0 and emp_choice <= len(emp_list)):
                        selected_emp = emp_list[emp_choice - 1]
                        new_emp = get_emp_details(selected_emp.emp_id)
                        selected_emp.emp_name = new_emp.emp_name
                        selected_emp.set_gender(new_emp.gender)
                        selected_emp.set_dob(new_emp.dob)
                        selected_emp.set_dept(new_emp.dept)
                        selected_emp.set_desg(new_emp.desg)
                        selected_emp.set_salary(new_emp.salary)
                        selected_emp.set_doj(new_emp.doj)
                        selected_emp.set_contact(new_emp.contact)
                        print(f"employee updated successfully")
                        write_all_to_file("emp_data.csv")
                    else:
                        print("invalid selection")

        # delete employee
        if (choice == 4):
            emp_id = int(input("enter the employee id to delete employee record"))
            emp = search_employee_ID(emp_id)
            if emp is not None:
                em.employees.remove(emp)
                print(f"employee with id: {emp_id} deleted successfully ")
                write_all_to_file("emp_data.csv")
            else:
                print(f"employee with id: {emp_id} not found")

        if (choice == 5):
            em.display_emp()

        if (choice == 6):
            emp_id = int(input("enter the employee id for marking today's attendance"))
            write_attendance_tofile(emp_id)

        # sorting employees
        if (choice == 7):
            sub_choice = sort_sub_menu()
            if (sub_choice == 0):
                em.employees.sort(key=lambda e: e.emp_id)
            if (sub_choice == 1):
                em.employees.sort(key=lambda e: e.emp_name)
            if (sub_choice == 2):
                em.employees.sort(key=lambda e: e.salary)
            if (sub_choice == 3):
                em.employees.sort(key=lambda e: e.dob)
            if (sub_choice == 4):
                em.employees.sort(key=lambda e: e.doj)
            if (sub_choice > 4 or sub_choice < 0):
                print("invalid choice")
            write_all_to_file("emp_data.csv")

        # filter employees
        if (choice == 8):
            sub_choice = filter_sub_menu()
            if (sub_choice == 1):
                s = set()
                for emp in em.employees:
                    s.add(emp.dept)
                print(s)
                dept = input("enter employee department")
                emp_list = filter_employee_dept(dept)
                if len(emp_list) == 0:
                    print(f"no employees in department:{dept}")
                else:
                    print(f"list of {len(emp_list)} employees in department:{dept}")
                    for emp in emp_list:
                        print(emp)
            if (sub_choice == 2):
                s = set()
                for emp in em.employees:
                    s.add(emp.desg)
                print(s)
                desg = input("enter employee designation")
                emp_list = filter_employee_desg(desg)
                if len(emp_list) == 0:
                    print(f"no employees with designation :{desg}")
                else:
                    print(f"list of {len(emp_list)} employees with designation:{desg}")
                    for emp in emp_list:
                        print(emp)
            if (sub_choice == 3):
                gender = input("enter employee gender")
                if validate_gender(gender):
                    emp_list = filter_employee_gender(gender)
                    if len(emp_list) == 0:
                        print(f"no employees with gender :{gender}")
                    else:
                        print(f"list of {len(emp_list)} employees with gender:{gender}")
                        for emp in emp_list:
                            print(emp)
                else:
                    print("invalid gender")

            if (sub_choice == 4):
                salary = int(input("enter employee salary less than: Rs. "))
                emp_list = filter_employee_salary(salary)
                if len(emp_list) == 0:
                    print(f"no employees with salary less than: Rs. {salary}")
                else:
                    print(f"list of {len(emp_list)} employees with salary less than: Rs. {salary}")
                    for emp in emp_list:
                        print(emp)

        if (choice == 9):
            eid = int(input("enter employee ID"))
            emp = search_employee_ID(eid)
            if emp is not None:
                record_appraisal(emp)

        if (choice == 10):
            sy = int(input("enter appraisal starting year"))
            ey = int(input("enter end year"))
            em.write_bonus_log("bonus_log", sy, ey)

        if (choice == 11):
            write_promotion_log("promotion_log.csv")
            print("promotion log written to promotion_log.csv")

        if (choice >= 12 or choice < 1):
            repeat = False


if __name__ == "__main__":
    main()