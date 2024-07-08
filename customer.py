from person import Person


class Customer(Person):
    def __init__(self, customer_id, customer_name, customer_email, customer_number):
        super().__init__(customer_id, customer_name, customer_email)
        self.customer_number = customer_number

    def __str__(self):
        return (f"ID: {self.person_id} | Name: {self.person_name} | Email: {self.person_email} | "
                f"Kundennummer: {self.customer_number}")
