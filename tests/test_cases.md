| Test Case Input                                    | Action        | Description                                        | Expected Output                                            |
| -------------------------------------------------- | ------------- | -------------------------------------------------- | ---------------------------------------------------------- |
| Row with all fields correct                        | `Course(row)` | Parses fields, trims whitespace, parses L-T-P-S-C  | Correct `.code`, `.title`, `.faculty`, numeric `L,T,P,S,C` |
| Row with malformed L-T-P-S-C (e.g., `"3-1-x-0-4"`) | `Course(row)` | Invalid integers must not crash                    | All components default to `0`                              |
| Missing `"Faculty"` field                          | `Course(row)` | Missing optional fields should not raise exception | `.faculty == ""`                                           |
| Missing `"Semester_Half"` field                    | `Course(row)` | Must default to `"0"`                              | `.sem_half == "0"`                                         |
| Elective value `"1"` or integer `1`                | `Course(row)` | Should detect elective correctly                   | `.is_elective == True`                                     |
| Elective value `"0"` or integer `0`                | `Course(row)` | Should detect non-elective                         | `.is_elective == False`                                    |
| Extra whitespace in fields                         | `Course(row)` | Trim whitespace                                    | `" CS101 "` → `"CS101"`                                    |
| Short L-T-P format (`"3-1"`)                       | `Course(row)` | Should pad missing entries to 5 values             | `(L,T,P,S,C)=(3,1,0,0,0)`                                  |



| Test Case Input                           | Function Under Test             | Description                             | Expected Output                                           |
| ----------------------------------------- | ------------------------------- | --------------------------------------- | --------------------------------------------------------- |
| `"09:00-10:00"`                           | `_slot_len()`                   | Standard 1-hour slot                    | Returns `1.0`                                             |
| `"10:00-11:30"`                           | `_slot_len()`                   | 1.5-hour slot                           | Returns `1.5`                                             |
| Bad format `"abc"`                        | `_slot_len()`                   | Invalid times                           | Should raise safe `ValueError` or be caught upstream      |
| Day with all empty slots                  | `_free_blocks(table, "Monday")` | Table with all empty except excluded    | One large continuous block (excluding the excluded slots) |
| Day with alternating filled/empty pattern | `_free_blocks()`                | Detects multiple separated blocks       | Correct block segmentation                                |
| Excluded slot ("13:15-14:00") in middle   | `_free_blocks()`                | Must break block at excluded slot       | Two separate blocks                                       |
| Deterministic ordering                    | `stable_key()`                  | Same input must always produce same key | Identical ordering every run                              |


| Test Input                                 | Expected Behavior                                    | Expected Output                                           |
| ------------------------------------------ | ---------------------------------------------------- | --------------------------------------------------------- |
| Empty table, 1-hour lecture                | Should assign first valid slot                       | Returns `True`, table updated                             |
| Slot already filled                        | Attempt to place in occupied slot                    | Returns `False`                                           |
| Faculty already busy for slot              | Should skip slot                                     | No assignment, `False`                                    |
| Room conflict: same room used in same slot | Room conflict detected via `global_room_usage`       | Should try another room or return `False`                 |
| Elective session (`is_elective=True`)      | Should skip room assignment entirely                 | Room in record is `""`                                    |
| Lab session after daily lab assigned       | `labs_scheduled[day] == True` and session_type `"P"` | Must NOT schedule → `False`                               |
| Multi-slot sessions (1.5 hr)               | Needs contiguous blocks                              | Should allocate exactly required number of adjacent slots |
| Session spills over excluded slot          | Must NOT allocate across excluded slot               | Should fail or re-try different day                       |



| Scenario                                  | Description                                                 | Expected Behavior                                  |
| ----------------------------------------- | ----------------------------------------------------------- | -------------------------------------------------- |
| No electives scheduled on sheet           | Should exit without error                                   | `elective_room_map[sheet] = {}`                    |
| One elective placeholder scheduled        | Should assign a single free room                            | Room assigned (classroom)                          |
| Two electives same day & slot             | Should assign different rooms                               | `room1 != room2`                                   |
| All rooms occupied by other courses       | Should fall back to “best fit” (max free slots)             | Graceful assignment with deterministic room choice |
| Multiple electives but one room available | Should assign same room only if no conflict with slot usage | Assign sequentially but conflict-free              |
| Elective titles differ but same basket    | Only placeholder Elective_X is used                         | Proper mapping per sheet                           |


| Test Input                              | Description                              | Expected Output                                 |
| --------------------------------------- | ---------------------------------------- | ----------------------------------------------- |
| Minimal dataset (1 course, 1 slot)      | Smoke test small dataset                 | Excel file produced                             |
| Dataset with no courses                 | No scheduling work needed                | Empty timetable sheet created                   |
| Multiple courses same faculty           | Checks faculty conflict logic            | No overlapping faculty bookings                 |
| Multiple labs same day                  | Must enforce "only one lab per day" rule | Only one lab scheduled each day                 |
| Check room conflict across departments  | Uses shared `global_room_usage`          | No two departments use same room same time      |
| With electives in CSV                   | Elective placeholder inserted            | Placeholder course scheduled normally           |
| Deterministic scheduling                | Run twice → identical output             | Excel identical across runs (except timestamps) |
| Un-schedulable course (no room or time) | Course cannot be placed                  | Appears in `unscheduled_courses.xlsx`           |
| Combined multi-department generation    | End-to-end main execution                | All department files created; no crash          |



