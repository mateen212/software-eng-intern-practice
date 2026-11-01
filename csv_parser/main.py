import csv
from typing import Optional

from pydantic import (
    BaseModel,
    Field,
    EmailStr,
    ConfigDict,
    ValidationError,
    field_validator,
    model_validator
)


# =====================================
# 1. STUDENT DATA MODEL
# =====================================

class Student(BaseModel):

    # Strict model configuration
    model_config = ConfigDict(
        extra="forbid"
    )

    name: str = Field(
        min_length=2,
        max_length=50
    )

    age: int = Field(
        ge=18,
        le=60
    )

    email: EmailStr

    marks: float = Field(
        ge=50,
        le=100
    )

    phone: str = Field(
        min_length=11,
        max_length=11
    )

    city: str = Field(
        min_length=2,
        max_length=30
    )

    # Optional field
    department: Optional[str] = None


    # =====================================
    # 2. FIELD VALIDATORS
    # =====================================

    @field_validator("name")
    @classmethod
    def validate_name(cls, value: str) -> str:

        if not value.replace(" ", "").isalpha():
            raise ValueError("Name must contain only letters")

        return value.strip().title()


    @field_validator("phone")
    @classmethod
    def validate_phone(cls, value: str) -> str:

        if not value.isdigit():
            raise ValueError("Phone must contain only digits")

        return value


    @field_validator("city")
    @classmethod
    def validate_city(cls, value: str) -> str:

        return value.strip().title()


    # =====================================
    # 3. MODEL VALIDATOR
    # =====================================

    @model_validator(mode="after")
    def validate_student(self):

        if self.marks < 50:
            raise ValueError("Student must have at least 50 marks")

        return self


# =====================================
# 4. READ AND VALIDATE CSV
# =====================================

def parse_csv(
    filename: str
) -> tuple[list[Student], list[dict]]:

    valid_students: list[Student] = []

    invalid_students: list[dict] = []

    seen_emails: set[str] = set()

    with open(filename, "r", newline="") as file:

        reader = csv.DictReader(file)

        for row_number, row in enumerate(reader, start=2):

            try:

                # Validate CSV row
                student = Student(**row)

                # Check duplicate emails
                email = str(student.email).lower()

                if email in seen_emails:

                    raise ValueError("Duplicate email address")

                seen_emails.add(email)

                valid_students.append(student)

            except ValidationError as error:

                invalid_students.append({
                    "row": row_number,
                    "data": row,
                    "error": error.errors()
                })
            except ValueError as error:

                invalid_students.append({
                    "row": row_number,
                    "data": row,
                    "error": str(error)
                })
    return valid_students, invalid_students


# =====================================
# 5. SAVE VALID STUDENTS
# =====================================

def save_valid_students(
    students: list[Student],
    filename: str
) -> None:

    if not students:
        print("No valid students to save.")
        return

    with open(filename, "w", newline="") as file:

        fieldnames = [
            "name",
            "age",
            "email",
            "marks",
            "phone",
            "city",
            "department"
        ]

        writer = csv.DictWriter(
            file,
            fieldnames=fieldnames
        )

        writer.writeheader()

        for student in students:

            writer.writerow(student.model_dump())


# =====================================
# 6. SAVE INVALID STUDENTS
# =====================================

def save_invalid_students(
    students: list[dict],
    filename: str
) -> None:

    if not students:
        print("No invalid students found.")
        return

    with open(filename, "w", newline="") as file:

        writer = csv.DictWriter(
            file,
            fieldnames=["row", "data", "error"]
        )

        writer.writeheader()

        writer.writerows(students)


# =====================================
# 7. MAIN FUNCTION
# =====================================

def main() -> None:

    valid, invalid = parse_csv("csv_parser/contacts_data.csv")

    print("\n========== VALID STUDENTS ==========")

    for student in valid:

        print(student.model_dump())

    print("\n========== INVALID STUDENTS ==========")

    for record in invalid:

        print("Row:", record["row"])

    for error in record["error"]:

        print("Field:", error["loc"])
        print("Message:", error["msg"])

    # Save results
    save_valid_students(valid, "csv_parser/valid_students.csv")

    save_invalid_students(invalid, "csv_parser/invalid_students.csv")

    print("\n========== SUMMARY ==========")

    print(f"Total valid students: {len(valid)}")
    print(f"Total invalid students: {len(invalid)}")
    print(f"Total processed: {len(valid) + len(invalid)}")


if __name__ == "__main__":
    main()