import pandas as pd
from timetable_automation import Scheduler

def dummy_scheduler():
    return Scheduler("tests/data/slots.csv", 
                     "tests/data/courses.csv", 
                     "tests/data/rooms.csv",
                     global_room_usage={})

def test_slot_len_1hour():
    sch = dummy_scheduler()
    assert sch._slot_len("09:00-10:00") == 1.0

def test_slot_len_1_5hour():
    sch = dummy_scheduler()
    assert sch._slot_len("10:00-11:30") == 1.5

def test_free_blocks_all_free():
    sch = dummy_scheduler()
    table = pd.DataFrame("", index=sch.days, columns=sch.slots)
    blocks = sch._free_blocks(table, "Monday")
    assert len(blocks) > 0
    assert set(blocks[0]).issubset(set(sch.slots))

def test_free_blocks_with_excluded():
    sch = dummy_scheduler()
    table = pd.DataFrame("", index=sch.days, columns=sch.slots)
    excluded = sch.excluded[0]
    table.at["Monday", excluded] = "X"
    blocks = sch._free_blocks(table, "Monday")
    assert all(excluded not in block for block in blocks)
