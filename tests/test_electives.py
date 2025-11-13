from timetable_automation import Scheduler

def test_no_electives_in_sheet():
    sch = Scheduler("tests/data/slots.csv","tests/data/courses.csv",
                    "tests/data/rooms.csv", global_room_usage={})
    sch.records = []
    sch.elective_groups = {"Sheet1": []}

    sch._compute_elective_room_assignments_legally("Sheet1")
    assert sch.elective_room_map["Sheet1"] == {}

def test_elective_assigns_room():
    sch = Scheduler("tests/data/slots.csv","tests/data/courses.csv",
                    "tests/data/rooms.csv", global_room_usage={})

    # Simulate elective placed at one slot
    sch.records = [{"sheet":"Sheet1","day":"Monday","slot":"09:00-10:00","code":"Elective_1"}]
    sch.elective_groups = {"Sheet1":[(1, type("X",(object,),{"title":"ElectiveTitle"}))]}

    sch._compute_elective_room_assignments_legally("Sheet1")
    assert "Sheet1" in sch.elective_room_map
    assert len(sch.elective_room_map["Sheet1"]) == 1
