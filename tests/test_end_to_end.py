import os
from timetable_automation import Scheduler

def test_generate_timetable_end_to_end(tmp_path):
    # prepare dummy files
    slots_file = "tests/data/slots.csv"
    rooms_file = "tests/data/rooms.csv"
    courses_file = "tests/data/courses.csv"

    out = tmp_path / "timetable.xlsx"

    sch = Scheduler(slots_file, courses_file, rooms_file, global_room_usage={})
    sch.run_all_outputs("TEST", student_filename=str(out), faculty_filename=str(tmp_path / "faculty.xlsx"))

    assert out.exists()

def test_unscheduled_courses_generated(tmp_path):
    # course that cannot fit must produce unscheduled file
    slots_file = "tests/data/slots.csv"
    rooms_file = "tests/data/rooms.csv"
    courses_file = "tests/data/too_many_hours.csv"  # create huge L values

    out = tmp_path / "timetable.xlsx"
    sch = Scheduler(slots_file, courses_file, rooms_file, global_room_usage={})
    sch.run_all_outputs("TEST", student_filename=str(out), faculty_filename=str(tmp_path / "faculty.xlsx"))

    unsched = tmp_path / "TEST_unscheduled_courses.xlsx"
    assert unsched.exists()
