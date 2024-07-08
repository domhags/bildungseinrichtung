class Course:
    def __init__(self, course_id, course_title, course_description):
        self.course_id = course_id
        self.course_title = course_title
        self.course_description = course_description

    def __str__(self):
        return f"ID: {self.course_id} | Titel: {self.course_title} | Beschreibung: {self.course_description}"
