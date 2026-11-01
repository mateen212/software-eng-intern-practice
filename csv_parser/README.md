# Data-Validated CSV Parser

A small Python data-validation pipeline that reads student records from a CSV file, validates each row with Pydantic, and writes valid and invalid records to separate CSV files.

## Project files

- `main.py` — defines the student model, parses and validates rows, displays results, and saves the output files.
- `contacts_data.csv` — sample input data, including valid rows and rows with validation errors.
- `valid_students.csv` — output containing records that passed validation.
- `invalid_students.csv` — output containing rejected rows and their errors.

## Requirements

- Python 3.10 or later
- Pydantic 2
- `email-validator` (required by Pydantic's `EmailStr`)

Install the dependencies:

```bash
python3 -m pip install "pydantic[email]"
```

## Run

From the repository root, run:

```bash
python3 csv_parser/main.py
```

The script reads `csv_parser/contacts_data.csv`, prints validated students and a summary, then writes results to `csv_parser/valid_students.csv` and `csv_parser/invalid_students.csv`. Run it from the repository root because the input and output paths are relative to the current working directory.

## Validation rules

Each student record is checked against these rules:

- `name`: 2–50 characters, letters and spaces only; normalized to title case.
- `age`: integer from 18 through 60.
- `email`: valid email address.
- `marks`: number from 50 through 100.
- `phone`: exactly 11 digits.
- `city`: 2–30 characters; normalized to title case.
- `department`: optional.
- Extra fields are rejected, and an email already accepted from an earlier row is treated as a duplicate.

CSV values are initially strings. Pydantic converts compatible values to the model's declared types and reports validation errors for rows that cannot be accepted. A bad row does not stop the parser from processing later rows.

## Output files

`valid_students.csv` contains the normalized model fields for accepted students. `invalid_students.csv` contains the source row number, original row data, and validation or duplicate-email error details.
