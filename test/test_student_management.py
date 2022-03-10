from student_management import StudentManagement
import unittest


class TestStudentManagement(unittest.TestCase):

    def setUp(self):
        self.manager = StudentManagement()

    # this is not a test case, it is a function to set data
    def set_data(self):
        name = "nanda"
        age = 20
        course = "computers"
        self.manager.add_student(name, age, course)
        self.assertEqual(len(self.manager.students), 1)

    # writing test case for adding_Students
    def test_add_student(self):
        self.set_data()
        name = "kishore"
        age = 20
        course = "Mechanical"
        output = self.manager.add_student(name, age, course)
        expected_output = str(f"{name} details added")
        self.assertEqual(expected_output, output)

