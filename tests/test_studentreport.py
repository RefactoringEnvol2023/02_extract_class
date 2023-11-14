from io import StringIO
from reporting.models import StudentReport

def test_instantiation():
    # __Given__
    report = StudentReport("John Doe", 90, 85, 95)
    out = StringIO()
    # __When__
    report.generate_report(out)
    # __Then__
    assert out.getvalue() == 'Student: John Doe,\n' \
        'Math Grade: 90,\n' \
        'Literature Grade: 85,\n' \
        'Science Grade: 95,\n' \
        'Average Grade: 90.0,\n'