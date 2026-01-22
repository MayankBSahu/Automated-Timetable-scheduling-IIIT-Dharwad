import pandas as pd
import re
from collections import defaultdict

FILE = "Balanced_Timetable_latest.xlsx"

# Adjust if your days labels differ
DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

# Regex to extract room from cell text like "CS101T (C101)" or "CS101 (Lab-C102)"
ROOM_PATTERN = re.compile(r"\(([^)]+)\)$")

def extract_room(text: str):
    """
    Try to extract room name from the cell text.
    Returns None if no obvious room is found.
    """
    if not isinstance(text, str):
        return None
    text = text.strip()
    m = ROOM_PATTERN.search(text)
    if not m:
        return None
    room_raw = m.group(1)
    # Sometimes lab notation like "Lab-C102"
    # take the part after the last dash
    if "-" in room_raw:
        room_raw = room_raw.split("-")[-1].strip()
    return room_raw

def main():
    xls = pd.ExcelFile(FILE)
    clashes = []

    # key: (day, time_slot, room) -> list of entries
    occupancy = defaultdict(list)

    for sheet_name in xls.sheet_names:
        df = pd.read_excel(FILE, sheet_name=sheet_name)

        # Heuristic:
        # - first column = "Day"
        # - subsequent columns = time slots (like "08:30-09:30")
        # Adjust if your format is different.
        if "Day" not in df.columns:
            # Try to infer Day column
            # assume first column holds days
            df = df.rename(columns={df.columns[0]: "Day"})

        for _, row in df.iterrows():
            day = str(row["Day"]).strip()
            if day not in DAYS:
                continue

            for col in df.columns:
                if col == "Day":
                    continue
                time_slot = str(col).strip()
                cell = row[col]
                if pd.isna(cell) or str(cell).strip() == "":
                    continue

                text = str(cell).strip()
                room = extract_room(text)
                if not room:
                    continue  # no room in this cell, skip

                key = (day, time_slot, room)
                occupancy[key].append({
                    "sheet": sheet_name,
                    "course": text,
                })

    # Collect clashes
    for (day, time_slot, room), entries in occupancy.items():
        if len(entries) > 1:
            clashes.append((day, time_slot, room, entries))

    if not clashes:
        print("✅ No room clashes found between any sheets.")
    else:
        print("❌ Room clashes found:\n")
        for day, time_slot, room, entries in clashes:
            print(f"Day: {day}, Slot: {time_slot}, Room: {room}")
            for e in entries:
                print(f"  - Sheet: {e['sheet']}, Cell: {e['course']}")
            print()

if __name__ == "__main__":
    main()
