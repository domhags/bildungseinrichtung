class Person:
    def __init__(self, person_id, person_name, person_email):
        self.person_id = person_id
        self.person_name = person_name
        self.person_email = person_email

    def __str__(self):
        return f"ID: {self.person_id} | Name: {self.person_name} | Email: {self.person_email}"
