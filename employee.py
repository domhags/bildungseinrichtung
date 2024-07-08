from person import Person


class Employee(Person):
    def __init__(self, employee_id, employee_name, employee_email, employee_number):
        super().__init__(employee_id, employee_name, employee_email)
        self.employee_number = employee_number

    def __str__(self):
        return (f"ID: {self.person_id} | Name: {self.person_name} | Email: {self.person_email} | "
                f"Mitarbeiternummer: {self.employee_number}")
    