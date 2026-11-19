def get_employee_count(employees):
    return len(employees)


def get_employee_names(employees):
    return employees

def get_active_employees(employees):
    active_employees = []

    for employee in employees:
        if employee["status"] == "active":
            active_employees.append(employee)

    return active_employees