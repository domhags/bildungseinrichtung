import re


class Management:
    def __init__(self):
        self.people = []
        self.courses = []

    def add_person(self, person):
        self.people.append(person)

    def add_course(self, course):
        self.courses.append(course)

    def export_people(self, export_filename):
        if self.is_valid_filename(export_filename):
            try:
                with open(export_filename, 'a') as file:
                    for person in self.people:
                        file.write(str(person) + '\n')
                print(f"Personen wurden nach '{export_filename}' exportiert.")
            except IOError as e:
                print(f"Fehler beim Exportieren der Personen: {e}")
        else:
            print(f"Ungültiger Dateiname: {export_filename}")

    @staticmethod
    def import_people(import_filename):
        if Management.is_valid_filename(import_filename):
            try:
                with open(import_filename, 'r') as file:
                    for line in file:
                        print(line.strip())
            except FileNotFoundError:
                print("Datei nicht gefunden.")
            except IOError as e:
                print(f"Fehler beim Importieren der Personen: {e}")
        else:
            print(f"Ungültiger Dateiname: {import_filename}")

    def export_filtered(self, filtered_export_filename, person_type):
        if self.is_valid_filename(filtered_export_filename):
            try:
                with open(filtered_export_filename, 'w') as file:
                    for person in self.people:
                        if isinstance(person, person_type):
                            file.write(str(person) + '\n')
                print(f"Gefilterte Personen wurden nach '{filtered_export_filename}' exportiert.")
            except IOError as e:
                print(f"Fehler beim Exportieren der gefilterten Personen: {e}")
        else:
            print(f"Ungültiger Dateiname: {filtered_export_filename}")

    @staticmethod
    def import_filtered(filtered_import_filename):
        if Management.is_valid_filename(filtered_import_filename):
            try:
                with open(filtered_import_filename, 'r') as file:
                    for line in file:
                        print(line.strip())
            except FileNotFoundError:
                print("Datei nicht gefunden.")
            except IOError as e:
                print(f"Fehler beim Importieren der gefilterten Personen: {e}")
        else:
            print(f"Ungültiger Dateiname: {filtered_import_filename}")

    @staticmethod
    def is_valid_filename(filename):
        return not bool(re.search(r'[<>:"/\\|?*]', filename))
