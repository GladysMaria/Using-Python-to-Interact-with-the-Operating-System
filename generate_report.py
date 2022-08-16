""" This script opens a csv file, counts how many people are in each department and creates a report.

This is the Handling Files exam:
Given a list of employees containing FullName, Username, Department...
You want to know how many people are in each department.

The initial file is employees.csv"""

import csv
def read_employees(csv_file_location):
    """ Convert CSV data to a list of dictionaries."""
    csv.register_dialect('empDialect', skipinitialspace=True, strict=True)
    # The purpose of  dialect is to remove any spaces while parsing the file
    with open(csv_file_location, dialect='empDialect') as file:
        employee_file = csv.DictReader(file)
    employee_list = []
    for data in employee_file:
        employee_list.append(data)
    return employee_list

employee_list = read_employees('<file_location>')


def process_data(employee_list):
    """  Receive the list of dictionaries from  read_employees(csv_file_location) and return a department:amount dictionary."""
    department_list = []
    for employee_data in employee_list:
        department_list.append(employee_data['Department'])
    department_data = {}
    for department_name in set(department_list): #El metodo set elimina las redundancias
        department_data[department_name] = department_list.count(department_name)
    return department_data
dictionary = process_data(employee_list)

def write_report(dictionary, report_file):
    """ Create a text file and generate the report."""
    with open(report_file, "w+") as f:
        for k in sorted(dictionary):
            f.write(str(k)+':'+str(dictionary[k])+'\n')
    f.close()
write_report(dictionary, '<report_file>')