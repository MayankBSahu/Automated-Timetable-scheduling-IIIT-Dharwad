# Automated-Timetable-scheduling-IIIT-Dharwad
Automated-Timetable-scheduling-IIIT-Dharwad

A Python-based system developed for automating the generation of class timetables at IIIT Dharwad.

Table of Contents

Background

Features

Repository Structure

Getting Started

Prerequisites

Installation

Usage

How it works

Tests

Data & Inputs

Output

Contributing

License

Acknowledgements

Background

Generating academic timetables manually can be time-consuming and error-prone: room conflicts, teacher overlaps, student group restrictions, etc.
This project automates the timetable generation process for IIIT Dharwad, considering constraints such as course scheduling, faculty availability, room allocation, and student batch divisions.

Features

Automatic timetable generation using Python.

Constraint handling: faculty availability, room capacity, batch scheduling, unscheduled courses flagged.

Input data (courses, rooms, faculty) can be supplied in spreadsheet (Excel) format.

Multiple batch timetables and faculty timetables generated.

Exported timetable in Excel format for easy viewing and distribution.

Repository Structure
Automated-Timetable-scheduling-IIIT-Dharwad/
├── data/                      ← raw input data files (Excel)  
├── docs/                      ← documentation (design, algorithm, usage)  
├── tests/                     ← automated tests for modules  
├── timetable_automation/      ← main Python code and modules  
├── *.xlsx                     ← example output timetables (7-SEM, CSE-1-A, etc)  
└── README.md                  ← this file  

Getting Started
Prerequisites

Python 3.x

Required Python packages (e.g., pandas, openpyxl) — installable via pip.

Excel runtime environment (for reading/writing XLSX)

Sample data files (see data/ folder) with the correct schema.

Installation

Clone the repository:

git clone https://github.com/MayankBSahu/Automated-Timetable-scheduling-IIIT-Dharwad.git  
cd Automated-Timetable-scheduling-IIIT-Dharwad  


(Optional) Create and activate a virtual environment:

python3 -m venv venv  
source venv/bin/activate  # On Windows: venv\Scripts\activate  


Install dependencies:

pip install -r requirements.txt  


(If requirements.txt is missing, install packages manually: pip install pandas openpyxl etc.)

Usage

Place or update your input Excel files in data/.

Configure any scheduling parameters (e.g., number of slots per day, room lists) in the configuration file/module inside timetable_automation/.

Run the automation script:

python timetable_automation/main.py  


The output timetables will be generated as Excel files (see example: 7-SEM_timetable.xlsx, CSE-1-A_timetable.xlsx, etc).

Check the unscheduled_courses.xlsx file (if produced) to see any courses that could not be allocated under given constraints.

How it works

The system reads input data: courses, batches, faculty, rooms.

It builds a constraint model: each course must be assigned a time slot and room, no faculty/time conflicts, no student batch overlap, room capacity respected.

A scheduling algorithm (greedy or heuristic) iterates to allocate slots.

Output is formatted into student-batch timetables and faculty timetables.

Unallocatable courses are flagged for manual review.

Tests

Automated tests are in the tests/ folder covering:

Data input validation

Constraint checks (e.g., no double-booking of a faculty)

Output file generation
Run tests with:

pytest  


(Install pytest if needed: pip install pytest).

Data & Inputs

In the data/ directory you will find example spreadsheets:

Faculty list

Room list

Courses & batches
Ensure your data follows the same schema (sheet names, column headers) to avoid errors.

Output

Generated output includes:

Batch-wise timetables (for every batch e.g., CSE-3-A, DSAI-5)

Faculty timetable (e.g., faculty_timetable.xlsx)

Unscheduled courses list (if any)

Contributing

Contributions are welcome! If you’d like to contribute:

Fork the repository.

Create a new branch (feature/foo or bugfix/bar).

Commit your changes and push.

Submit a pull request with a clear description.

Please ensure you update tests and documentation accordingly.

License

This project is released under the MIT License.
Feel free to use, modify and distribute with attribution.

Acknowledgements

Thanks to all contributors and to the scheduling research literature which inspired the constraint-satisfaction approach.
Special thanks to the faculty and administrative staff of IIIT Dharwad for providing the input data and domain insights.
