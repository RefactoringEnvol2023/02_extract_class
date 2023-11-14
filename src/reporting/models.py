from io import StringIO
import sys
from typing import Optional


class Report:

    def generate_report(self, student, out: Optional[StringIO]=None):
        out = out if out else sys.stdout
        average_grade = (student.math_grade + student.literature_grade + student.science_grade) / 3
        print(f"Student: {student.student_name},", file=out, sep='\n')
        print(f"Math Grade: {student.math_grade},", file=out, sep='\n')
        print(f"Literature Grade: {student.literature_grade},", file=out, sep='\n')
        print(f"Science Grade: {student.science_grade},", file=out, sep='\n')
        print(f"Average Grade: {average_grade},", file=out, sep='\n')

class Student:
    def __init__(self, student_name, math_grade, literature_grade, science_grade):
        self.student_name = student_name
        self.math_grade = math_grade
        self.literature_grade = literature_grade
        self.science_grade = science_grade




if __name__ == "__main__":
    student1 = Student("John Doe", 90, 85, 95)
    student1.generate_report()