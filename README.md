# Automated-Timetable-scheduling-IIIT-Dharwad
A Python-based system developed to automate the generation of academic timetables for IIIT Dharwad, handling room constraints, faculty availability, batch divisions, and scheduling conflicts.

---

## Table of Contents
- [Background](#background)  
- [Features](#features)  
- [Repository Structure](#repository-structure)  
- [Getting Started](#getting-started)  
  - [Prerequisites](#prerequisites)  
  - [Installation](#installation)  
  - [Usage](#usage)  
- [How It Works](#how-it-works)  
- [Tests](#tests)  
- [Data & Inputs](#data--inputs)  
- [Output](#output)  
- [Contributing](#contributing)  
- [License](#license)  
- [Acknowledgements](#acknowledgements)

---

##  Background
Manually creating academic timetables is time-consuming and prone to issues such as:
- Room conflicts  
- Faculty clashes  
- Batch overlaps  
- Uneven distribution of classes  

This project automates the timetable generation process by applying constraints and rules specific to IIIT Dharwad, producing complete batch and faculty timetables in Excel format.

---

##  Features
- Automatic timetable generation using Python  
- Handles constraints:
  - Faculty availability  
  - Room capacity & allocation  
  - Batch-wise scheduling  
  - Conflict detection  
- Accepts input in Excel format  
- Generates:
  - Batch-wise timetables  
  - Faculty timetables  
  - Unscheduled course lists  
- Clean Excel output for easy distribution  

---

##  Repository Structure

Automated-Timetable-scheduling-IIIT-Dharwad/
├── data/                      ← raw input data files (Excel)  
├── docs/                      ← documentation (design, algorithm, usage)  
├── tests/                     ← automated tests for modules  
├── timetable_automation/      ← main Python code and modules  
├── *.xlsx                     ← example output timetables (7-SEM, CSE-1-A, etc)  
└── README.md                  ← this file  


---

##  Getting Started

###  Prerequisites
- Python 3.x  
- Required packages:
  - pandas  
  - openpyxl  
- Excel environment for opening XLSX files  
- Input data placed in the `data/` folder  

---

###  Installation

Clone the repository:
```bash
git clone https://github.com/MayankBSahu/Automated-Timetable-scheduling-IIIT-Dharwad.git
cd Automated-Timetable-scheduling-IIIT-Dharwad
```
(Optional) Create and activate a virtual environment:

python3 -m venv venv
source venv/bin/activate   # For Windows: venv\Scripts\activate


Install dependencies:
pip install -r requirements.txt

If requirements.txt is not available:
pip install pandas openpyxl

(If requirements.txt is missing, install packages manually: pip install pandas openpyxl etc.)

##  Usage
1. **Place or update your input Excel files** in:
data/
2. **Configure scheduling variables** (such as slots, rooms, constraints) inside:
timetable_automation/
3. **Run the timetable generator:**
```bash
python timetable_automation/main.py
```
4.**Generated files** will appear in the project folder, for example:
7-SEM_timetable.xlsx
CSE-1-A_timetable.xlsx
faculty_timetable.xlsx
5.**If some courses cannot be placed**, check:
unscheduled_courses.xlsx

##  How It Works

1. **Data Loading**  
   The system reads all required inputs from Excel files:
   - Courses  
   - Faculty information  
   - Rooms and capacities  
   - Batch details  

2. **Constraint Model Construction**  
   Several scheduling constraints are applied to ensure a valid timetable:
   - **No faculty can be assigned to two rooms at the same time**
   - **No batch can attend overlapping courses**
   - **Room capacity and availability must match the scheduled course**
   - **Lecture counts and lecture types (L/T/P) are considered if configured**

3. **Scheduling Algorithm**  
   A greedy/heuristic algorithm attempts to assign each course to an optimal
   day, time slot, and room while respecting all constraints.

4. **Timetable Generation**  
   Successfully scheduled entries are exported into:
   - **Batch-wise timetables**
   - **Faculty timetables**

5. **Unscheduled Courses Handling**  
   Any course that cannot be placed due to conflicts is written to:
   unscheduled_courses.xlsx for manual inspection and adjustments.

6. **Excel Output**  
Final outputs are generated as `.xlsx` files for easy sharing and editing.

##  Tests

All test files are located in the `tests/` directory. These tests cover:

- **Data validation**  
  Ensures input files contain correct formats, headers, and data types.

- **Conflict checking**  
  Detects faculty double-booking, batch overlaps, and room conflicts.

- **Timetable generation integrity**  
  Verifies that schedules generated meet required constraints and structure.

---

###  Running Tests

To execute all tests, run:

```bash
pytest
```
(Install pytest if needed: pip install pytest).

##  Data & Inputs

The `data/` directory contains all the input Excel files required to generate the timetable.  
These files must follow the expected structure and column names.

### Required Input Files

- **Faculty list**  
  Contains faculty names, codes, availability, and other metadata.

- **Room list**  
  Includes room numbers, capacities, and room types (lecture/lab/tutorial if applicable).

- **Course list**  
  Contains course codes, titles, faculty assignments, number of lectures per week, L/T/P type, etc.

- **Batch information**  
  Lists batches and their corresponding courses.

### Important Requirements

Ensure that all input Excel files have:

- ✔ **Correct sheet names**  
- ✔ **Correct column headers**  
- ✔ **No missing or inconsistent values**  
- ✔ **Consistent faculty/course codes**  
- ✔ **Proper lecture count values (L/T/P)**

Incorrect or incomplete data may lead to unscheduled courses or errors during timetable generation.


##  Output

After execution, the system generates the following Excel files:

### Timetables
- **Batch-wise timetables**  
  For example:  
  - `CSE-3-A_timetable.xlsx`  
  - `DSAI-5_timetable.xlsx`  
  Each file contains a full weekly timetable for that batch.

- **Faculty timetables**  
  Includes individual schedules for each faculty member.

### Unscheduled Courses
If some courses cannot be placed due to conflicts or insufficient slots, they appear in:
unscheduled_courses.xlsx
This allows easy manual review and adjustments.
### Output Format
All generated files use `.xlsx` (Excel) format to ensure compatibility with:
- Microsoft Excel  
- Google Sheets  
- LibreOffice  
- Other spreadsheet software


##  Contributing

Contributions are welcome! To contribute to this project:

1. **Fork** the repository on GitHub.

2. **Create a new feature branch**:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3.**Making Contributions**:

After creating your feature branch and making updates, follow these steps:

#### 1. Commit your changes
```bash
git commit -m "Add your descriptive commit message here"
```
#### 2. Push the branch to your fork
git push origin feature/your-feature-name
#### 3. Open a Pull Request (PR)
Go to the main repository on GitHub and open a Pull Request from your branch.
Clearly describe the changes you made and why they are needed.

 Contribution Guidelines:
Write clean, readable, and well-documented code.
Add or update tests whenever your changes affect functionality.
Ensure your changes do not break existing features.
Provide a clear and concise PR description explaining your modifications.
Thank you for contributing and helping improve the project!

### License
This project is released under the MIT License.
Feel free to use, modify and distribute with attribution.

### Acknowledgements
Special thanks to:
- Research literature on constraint-based scheduling
- Faculty and administration of IIIT Dharwad for providing real input data and feedback
- Contributors who helped refine and test the scheduling logic

Thanks to all contributors and to the scheduling research literature which inspired the constraint-satisfaction approach.
Special thanks to the faculty and administrative staff of IIIT Dharwad for providing the input data and domain insights.
