from management import Management
from customer import Customer
from employee import Employee
from course import Course
import re


def is_valid_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)


def main():
    management = Management()

    while True:
        print("Was möchten Sie tun?\n"
              "1. Person hinzufügen\n"
              "2. Kurs hinzufügen\n"
              "3. Personen exportieren\n"
              "4. Personen importieren\n"
              "5. Gefilterte Personen exportieren\n"
              "6. Gefilterte Personen importieren\n"
              "7. Programm beenden")

        choice = input("Bitte wählen Sie eine Option (1-7): ")

        if choice == "1":
            add_person(management)
        elif choice == "2":
            add_course(management)
        elif choice == "3":
            export_people(management)
        elif choice == "4":
            import_people()
        elif choice == "5":
            export_filtered_people(management)
        elif choice == "6":
            import_filtered_people()
        elif choice == "7":
            print("Das Programm wird beendet.")
            break
        else:
            print("Ungültige Eingabe: (1-7)")


def add_person(management):
    print("\nPerson hinzufügen:")
    person_choice = input("Wählen Sie die Art der Person aus:\n1. Kunde\n2. Mitarbeiter\n")
    if person_choice not in ["1", "2"]:
        print("Ungültige Eingabe: (1 oder 2)")
        return

    person_id = input("ID: ")
    if not person_id:
        print("ID darf nicht leer sein.")
        return

    name = input("Name: ")
    if not name:
        print("Name darf nicht leer sein.")
        return

    email = input("Email: ")
    if not is_valid_email(email):
        print("Ungültige Email-Adresse.")
        return

    if person_choice == "1":
        customer_number = input("Kundennummer: ")
        if not customer_number:
            print("Kundennummer darf nicht leer sein.")
            return
        customer = Customer(person_id, name, email, customer_number)
        management.add_person(customer)
        print(f"{customer} wurde erfolgreich hinzugefügt.")
    elif person_choice == "2":
        employee_number = input("Mitarbeiternummer: ")
        if not employee_number:
            print("Mitarbeiternummer darf nicht leer sein.")
            return
        employee = Employee(person_id, name, email, employee_number)
        management.add_person(employee)
        print(f"{employee} wurde erfolgreich hinzugefügt.")


def add_course(management):
    print("\nKurs hinzufügen:")
    course_id = input("ID: ")
    if not course_id:
        print("ID darf nicht leer sein.")
        return

    course_title = input("Titel: ")
    if not course_title:
        print("Titel darf nicht leer sein.")
        return

    course_description = input("Beschreibung: ")
    if not course_description:
        print("Beschreibung darf nicht leer sein.")
        return

    course = Course(course_id, course_title, course_description)
    management.add_course(course)
    print(f"{course} wurde erfolgreich hinzugefügt.")


def export_people(management):
    print("\nPersonen exportieren:")
    filename = input("Dateiname für den Export: ")
    if not filename:
        print("Dateiname darf nicht leer sein.")
        return
    management.export_people(filename)


def import_people():
    print("\nPersonen aus Datei importieren: ")
    filename = input("Dateiname für den Import: ")
    if not filename:
        print("Dateiname darf nicht leer sein.")
        return
    Management.import_people(filename)


def export_filtered_people(management):
    print("\nGefilterte Personen exportieren: ")
    filename = input("Dateiname für den Export gefilterter Personen: ")
    if not filename:
        print("Dateiname darf nicht leer sein.")
        return

    person_choice = input("Wählen Sie die Art der Person aus:\n1. Kunde\n2. Mitarbeiter\n")
    if person_choice == "1":
        management.export_filtered(filename, Customer)
        print(f"Gefilterte Kundenliste wurde nach '{filename}' exportiert.")
    elif person_choice == "2":
        management.export_filtered(filename, Employee)
        print(f"Gefilterte Mitarbeiterliste wurde nach '{filename}' exportiert.")
    else:
        print("Ungültige Eingabe: (1 oder 2)")


def import_filtered_people():
    print("\nGefilterte Personen importieren: ")
    filename = input("Dateiname für den Import gefilterter Personen: ")
    if not filename:
        print("Dateiname darf nicht leer sein.")
        return

    person_choice = input("Wählen Sie die Art der Person aus:\n1. Kunde\n2. Mitarbeiter\n")
    if person_choice == "1":
        Management.import_filtered(filename)
        print("Gefilterte Kundenliste wurde erfolgreich importiert.")
    elif person_choice == "2":
        Management.import_people(filename)
        print("Gefilterte Mitarbeiterliste wurde erfolgreich importiert")
    else:
        print("Ungültige Eingabe: (1 oder 2)")


if __name__ == "__main__":
    main()
