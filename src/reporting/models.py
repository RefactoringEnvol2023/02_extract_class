from io import StringIO
import sys
from typing import Optional


class StudentReport:
    def __init__(self, student_name, math_grade, literature_grade, science_grade):
        self.student_name = student_name
        self.math_grade = math_grade
        self.literature_grade = literature_grade
        self.science_grade = science_grade

    def generate_report(self, out: Optional[StringIO]=None):
        out = out if out else sys.stdout
        average_grade = (self.math_grade + self.literature_grade + self.science_grade) / 3
        print(f"Student: {self.student_name},", file=out, sep='\n')
        print(f"Math Grade: {self.math_grade},", file=out, sep='\n')
        print(f"Literature Grade: {self.literature_grade},", file=out, sep='\n')
        print(f"Science Grade: {self.science_grade},", file=out, sep='\n')
        print(f"Average Grade: {average_grade},", file=out, sep='\n')

if __name__ == "__main__":
    student1 = StudentReport("John Doe", 90, 85, 95)
    student1.generate_report()