A constraint-aware, reproducible timetable generator for IIIT Dharwad that builds clash-free schedules from CSV/JSON inputs and serves an optional web app for browsing, filtering, and printing timetables. The system models real academic entities and constraints, supports heuristic/metaheuristic solvers, and exports both machine-readable and human-friendly outputs.[1]

### Highlights
- Clash-free across instructors, rooms, sections, and slots with hard/soft constraint handling and tunable weights.[1]
- Deterministic runs via seed control; exports CSV/JSON and HTML; optional Flask/Django web viewer.[1]
- Pluggable solving strategies: constructive + repair, GA, SA, Tabu; configurable limits and weights.[1]

## Table of contents
- About[1]
- Problem model[1]
- Project structure[1]
- Quick start[1]
- Web app[1]
- Data formats[1]
- Algorithms[1]
- Configuration[1]
- Testing[1]
- Roadmap[1]
- Contributing[1]
- License[1]

## About
This project formulates institute timetabling as a combinatorial optimization problem with explicit hard and soft constraints tailored for departmental scale deployment at IIIT Dharwad. It ingests institute data, enforces feasibility, optimizes preferences, and publishes timetables for review and distribution.[1]

## Problem model
- Entities: Departments, Courses, Sections/Batches, Instructors, Rooms/Labs, Timeslots (Mon–Fri).[1]
- Hard constraints:
  - No overlaps for instructor/room/section.[1]
  - Room capacity/type match; labs need contiguous multi-slot blocks.[1]
  - Fixed slots and mandatory assignments honored.[1]
- Soft constraints:
  - Instructor preferred slots and balanced daily/weekly load.[1]
  - Avoid extreme early/late slots and long idle gaps.[1]

## Project structure
```
.
├── data/          # CSV/JSON inputs (courses, instructors, rooms, sections, constraints)
├── src/           # Core scheduler, constraints/fitness, solver strategies, CLI
├── web/           # Optional Flask/Django app to visualize and filter timetables
├── outputs/       # Generated CSV/JSON and HTML reports
├── scripts/       # Validation and batch-run utilities
└── requirements.txt
```

## Quick start
- Environment
  - python -m venv .venv; activate; pip install -r requirements.txt.[1]
- Prepare data
  - Place input CSV/JSON in data/ and adjust constraints.json to institute rules.[1]
- Run scheduler
  - python src/run_scheduler.py --input data --out outputs --seed 42.[1]
- Review results
  - Outputs include machine-readable CSV/JSON and optional HTML views.[1]

## Web app
Start the server and browse http://localhost:5000 to filter by department, semester, instructor, and room, with weekly/daily views and print-friendly exports.[1]

```
python web/app.py
```
- Features:
  - Weekly/daily views with search and filters.[1]
  - Export/print pages for publishing.[1]

## Data formats
- courses.csv: course_id, name, dept, hours_per_week, is_lab.[1]
- instructors.csv: instructor_id, name, dept, qualified_courses, preferred_slots.[1]
- rooms.csv: room_id, name, capacity, type (LECTURE/LAB), allowed_depts.[1]
- sections.csv: section_id, program, semester, size, required_courses.[1]
- constraints.json: hard_rules, soft_rules, fixed_assignments, weights.[1]

Example constraints.json (minimal):[1]
```
{
  "hard": {
    "no_overlaps": true,
    "respect_capacity": true,
    "lab_contiguous": true
  },
  "soft": {
    "prefer_morning": ["CSE101_INSTR_1"],
    "avoid_last_slot": ["BTECH_CSE_S3"]
  },
  "weights": {
    "overlap_penalty": 1000,
    "capacity_violation": 500,
    "preference_violation": 5
  },
  "fixed": [
    { "course_id": "CSE201", "section_id": "BTECH_CSE_S3", "room_id": "LH-102", "day": "MON", "slot": 2 }
  ]
}
```

## Algorithms
- Initialization produces feasible or near-feasible candidates.[1]
- Fitness aggregates hard and soft violations using configurable weights.[1]
- Search strategies:
  - Heuristic constructive with repair for fast feasibility.[1]
  - Metaheuristics: Genetic Algorithm, Simulated Annealing, Tabu Neighborhood.[1]
- Termination by max iterations, time budget, or convergence threshold.[1]

## Configuration
Common flags:[1]
- --input: path to data directory.
- --out: output directory path.
- --seed: RNG seed for reproducibility.
- --max-iters / --time-budget: search effort limits.
- --strategy: solver choice (heuristic, ga, etc.).
- --weights: path to a JSON overriding weights in constraints.json.

Example:[1]
```
python src/run_scheduler.py \
  --input data \
  --out outputs \
  --strategy ga \
  --max-iters 2000 \
  --seed 1337
```

## Outputs
- CSV/JSON master schedules per section, instructor, and room.[1]
- HTML weekly/daily pages for quick review and printing.[1]
- Deterministic runs when seed is specified.[1]

## Testing
- Data validation:
  - python scripts/validate_data.py --input data.[1]
- Unit tests:
  - pytest -q.[1]

## Usage tips
- Start with accurate room types/capacities and clear lab duration blocks.[1]
- Encode faculty unavailability as fixed blocks or prohibited slots in soft rules with high weights.[1]
- For tight instances, begin with heuristic strategy, then refine with GA at lower time budgets.[1]

## Roadmap
- Instructor/room unavailability calendars and holiday/event exceptions.[1]
- Multi-objective optimization and trade-off visualizations.[1]
- Drag-and-drop manual edits with live conflict detection.[1]
- Incremental re-scheduling for late changes.[1]

## Contributing
- Fork, create a feature branch, commit changes, and open a PR with tests; include minimal reproducible data and exact constraints snippet for bug reports.[1]

```
git checkout -b feature/amazing-improvement
git commit -m "Add amazing improvement"
git push origin feature/amazing-improvement
```


## License
Open-source; see repository for license details or include a LICENSE file if missing.[1]

## Acknowledgments
Thanks to the IIIT Dharwad community and contributors for datasets, validation feedback, and deployment support.[1]

## Badges and status
- Languages: Python 100% (per repository stats).[1]
- Stars/Watchers/Forks: repository initialized; community growth welcome.[1]

