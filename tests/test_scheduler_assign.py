import pandas as pd
from timetable_automation import Scheduler

def setup_scheduler():
    return Scheduler("tests/data/slots.csv", 
                     "tests/data/courses.csv", 
                     "tests/data/rooms.csv",
                     global_room_usage={})

def test_assign_simple_lecture():
    sch = setup_scheduler()
    table = pd.DataFrame("", index=sch.days, columns=sch.slots)
    faculty_busy = {day: {slot: [] for slot in sch.slots} for day in sch.days}
    labs = {day: False for day in sch.days}

    ok = sch._assign_session(
        table, faculty_busy, labs,
        "Monday", "ProfX", "CS101",
        hrs=1.0, session_type="L",
        is_elective=False, sheet_name="TestSheet"
    )
    assert ok
    assert any("CS101" in table.at["Monday", s] for s in sch.slots)

def test_assign_fails_on_occupied():
    sch = setup_scheduler()
    table = pd.DataFrame("", index=sch.days, columns=sch.slots)
    some_slot = sch.slots[0]
    table.at["Monday", some_slot] = "BUSY"

    faculty_busy = {day: {slot: [] for slot in sch.slots} for day in sch.days}
    labs = {day: False for day in sch.days}

    ok = sch._assign_session(
        table, faculty_busy, labs,
        "Monday", "ProfX", "CS101",
        hrs=1.0, session_type="L",
        is_elective=False, sheet_name="TestSheet"
    )
    assert not ok

def test_assign_elective_has_empty_room():
    sch = setup_scheduler()
    table = pd.DataFrame("", index=sch.days, columns=sch.slots)
    faculty_busy = {day: {slot: [] for slot in sch.slots} for day in sch.days}
    labs = {day: False for day in sch.days}

    ok = sch._assign_session(
        table, faculty_busy, labs,
        "Tuesday", "ProfX", "Elective_1",
        hrs=1.0, session_type="L",
        is_elective=True, sheet_name="TestSheet"
    )
    assert ok
    rec = next(r for r in sch.records if r["code"] == "Elective_1")
    assert rec["room"] == ""
