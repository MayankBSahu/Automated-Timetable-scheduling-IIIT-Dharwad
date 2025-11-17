# Automated Timetable Scheduling – IIIT Dharwad

A constraint-aware system to generate clash-free academic timetables for IIIT Dharwad with reproducible outputs and an optional web interface for viewing and sharing.

## Features

- Clash-free schedules across instructors, rooms, sections, and timeslots with hard/soft constraint handling.  
- CSV/JSON input and export; human-readable HTML views for easy review.  
- Pluggable solving core (heuristics/metaheuristics) with tunable weights and seeds.  
- Optional lightweight web app to browse, filter, and print weekly/daily timetables.

## Table of Contents

- About  
- Problem Model  
- Project Structure  
- Quick Start  
- Web App (Optional)  
- Data Formats  
- Algorithms  
- Configuration  
- Testing  
- Roadmap  
- Contributing  
- License

## About

This project automates institute timetable creation by modeling scheduling as a combinatorial optimization problem with real-world academic constraints. It supports departmental scale inputs and exports final schedules for publishing.

## Problem Model

- Entities: Departments, Courses, Sections/Batches, Instructors, Rooms/Labs, Timeslots (Mon–Fri periods).  
- Hard constraints:  
  - No instructor/room/section overlaps.  
  - Room capacity/type must match (e.g., lab vs lecture).  
  - Labs require contiguous multi-slot blocks.  
  - Fixed/mandatory slots must be honored.  
- Soft constraints:  
  - Instructor preferred slots.  
  - Balanced daily load and spread across the week.  
  - Avoid extreme late/early slots and long idle gaps.

## Project Structure

```
.
├── data/           # CSV/JSON inputs for courses, instructors, rooms, sections, constraints
├── src/            # Scheduler core, fitness/constraints, CLI entrypoints
├── web/            # Optional Flask/Django app to visualize timetables
├── outputs/        # Generated CSV/JSON and HTML reports
├── scripts/        # Validation and batch-run utilities
└── requirements.txt
```

## Quick Start

1) Set up environment
```
python -m venv .venv
# Windows: .venv\Scripts\activate
# Linux/macOS:
source .venv/bin/activate
pip install -r requirements.txt
```

2) Prepare data  
Place your input files in data/ (see “Data Formats” below). Adjust constraints.json to reflect institute rules.

3) Run scheduler
```
python src/run_scheduler.py --input data --out outputs --seed 42
```

4) Review results  
Generated CSV/JSON and optional HTML views will appear in outputs/.

## Web App (Optional)

Start the web server to preview and filter timetables by department, semester, instructor, and room.

```
python web/app.py
# then open http://localhost:5000
```

Features:
- Weekly/daily views.  
- Filters and search.  
- Export/print-friendly pages.

## Data Formats

- courses.csv  
  - course_id, name, dept, hours_per_week, is_lab  
- instructors.csv  
  - instructor_id, name, dept, qualified_courses, preferred_slots  
- rooms.csv  
  - room_id, name, capacity, type (LECTURE/LAB), allowed_depts  
- sections.csv  
  - section_id, program, semester, size, required_courses  
- constraints.json  
  - hard_rules, soft_rules, fixed_assignments, weights

Example constraints.json (minimal):
```json
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

- Initialization creates feasible or near-feasible candidate schedules.  
- Fitness function scores violations of hard and soft constraints with configurable weights.  
- Search methods can be chosen or combined:
  - Heuristic constructive with repair.  
  - Metaheuristics (e.g., Genetic Algorithm, Simulated Annealing, Tabu Neighborhood).  
- Termination by max iterations/time or convergence threshold.

## Configuration

Common CLI flags:
- --input: folder containing data files (default: data)  
- --out: output directory (default: outputs)  
- --seed: RNG seed for reproducibility (default: none)  
- --max-iters / --time-budget: control search effort  
- --strategy: choose solver strategy (e.g., heuristic, ga)  
- --weights: path to custom weights JSON (overrides constraints.json weights)

Example:
```
python src/run_scheduler.py \
  --input data \
  --out outputs \
  --strategy ga \
  --max-iters 2000 \
  --seed 1337
```

## Testing

- Data validation:
```
python scripts/validate_data.py --input data
```
- Unit tests:
```
pytest -q
```

## Roadmap

- Instructor/room unavailability calendars and holiday/event exceptions.  
- Multi-objective optimization with trade-off visualizations.  
- Drag-and-drop manual edits with live conflict detection.  
- Incremental re-scheduling for last-minute changes.

## Contributing

1) Fork the repo and create a feature branch:
```
git checkout -b feature/amazing-improvement
```
2) Commit and push:
```
git commit -m "Add amazing improvement"
git push origin feature/amazing-improvement
```
3) Open a Pull Request with a clear description and tests.  
4) For bug reports, include a minimal dataset in data/ and the exact constraints snippet to reproduce.


## Acknowledgments

Thanks to the IIIT Dharwad community and contributors for datasets, validation feedback, and deployment support.

[1](https://github.com/topics/readme-template)
[2](https://github.com/othneildrew/Best-README-Template)
[3](https://gist.github.com/DomPizzie/7a5ff55ffa9081f2de27c315f5018afc)
[4](https://www.readme-templates.com)
[5](https://www.makeareadme.com)
[6](https://docs.github.com/github/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)
[7](https://www.reddit.com/r/programming/comments/l0mgcy/github_readme_templates_creating_a_good_readme_is/)
[8](https://rahuldkjain.github.io/gh-profile-readme-generator/)
[9](https://github.com/topics/readme-template-list)
[10](https://githubprofile.com/templates)
