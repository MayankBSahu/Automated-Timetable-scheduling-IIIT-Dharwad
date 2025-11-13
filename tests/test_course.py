import pytest
from timetable_automation import Course

def test_course_valid_fields():
    row = {
        "Course_Code": " CS101 ",
        "Course_Title": " Intro to Programming ",
        "Faculty": "Prof X",
        "L-T-P-S-C": "3-1-0-0-4",
        "Semester_Half": "1",
        "Elective": "0",
    }
    c = Course(row)
    assert c.code == "CS101"
    assert c.title == "Intro to Programming"
    assert c.faculty == "Prof X"
    assert (c.L, c.T, c.P) == (3, 1, 0)
    assert not c.is_elective

def test_course_malformed_ltp():
    row = {
        "Course_Code": "CS102",
        "Course_Title": "Error Test",
        "Faculty": "",
        "L-T-P-S-C": "3-1-x-0-4",   # malformed
    }
    c = Course(row)
    assert (c.L, c.T, c.P) == (0, 0, 0)

def test_course_missing_optional_fields():
    row = {
        "Course_Code": "CS103",
        "L-T-P-S-C": "3-0-0-0-3"
    }
    c = Course(row)
    assert c.faculty == ""
    assert c.sem_half == "0"

def test_course_elective_detection():
    row = {
        "Course_Code": "CS104",
        "L-T-P-S-C": "3-1-0-0-4",
        "Elective": "1",
    }
    c = Course(row)
    assert c.is_elective
