from io import StringIO
from reporting.models import Report, Student


def test_report():
    student = Student("John Doe", 90, 85, 95)
    out = StringIO()
    report = Report()
    # __When__
    report.generate_report(student, out)
    # __Then__
    assert out.getvalue() == 'Student: John Doe,\n' \
        'Math Grade: 90,\n' \
        'Literature Grade: 85,\n' \
        'Science Grade: 95,\n' \
        'Average Grade: 90.0,\n'
    