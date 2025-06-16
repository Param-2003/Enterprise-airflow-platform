# ✅ Input & Output File Validation: The Foundation of Data Trust

In any data pipeline, ensuring the **availability and correctness of input and output files** is a foundational aspect of data quality. In this project, we implemented **dedicated DAGs to validate both input ingestion files and output transformation results** before proceeding with the actual ETL or downstream operations.

---

## 🗂️ 1. Input File Validation (`check_input_file_dag.py`)

**Purpose:**
- Check if the expected date-partitioned input file (e.g., `2025-06-16.csv`) exists.
- Prevent downstream DAGs from running with missing or incomplete data.

**Logic:**
- Dynamically constructs the expected file path based on `execution_date`.
- Validates the file’s existence inside the mounted Docker volume.
- Fails early with clear logs if the file is missing.

**Simulation Example Log:**
```text
✅ File found for 2025-06-16: /opt/airflow/data/input_data/2025-06-16.csv

📤 2. Output File Validation (check_output_file_dag.py)
Purpose:

Validate whether the ETL transformation output has been successfully saved for the given date.

Helps identify partial or failed ETL runs early.

Logic:

Checks for output files like district_level_2025-06-16.csv.

Logs success/failure clearly.

Acts as a QA checkpoint before archiving or reporting.

🔍 Why This Matters
✅ Data validation DAGs are not optional.
They help:

Avoid running transformations on stale or missing inputs

Stop alerting downstream tasks when upstream files are incorrect

Ensure business metrics are only calculated when raw and transformed data both exist

⚠️ What Went Wrong (Our Mistakes)
❌ 1. CSV vs Excel Misinterpretation
Initially, we misread the source file format and wrote logic for .xlsx files, while our input was in .csv. This caused:

Path mismatches

FileNotFoundErrors

Code-level parsing failures

✅ Fix: We rewrote our logic to use .csv consistently and removed any Excel-specific code.

❌ 2. Docker Volume Mount Bug
Our DAG expected input files at:

text
Copy
Edit
/opt/airflow/data/input_data/<date>.csv
But we initially placed files in a path not mounted into the container, which led to:

Airflow not seeing files placed outside Docker volume

Tasks failing even though files existed on the host machine

✅ Fix:
We corrected our docker-compose.yaml:

yaml
Copy
Edit
volumes:
  - ../../data:/opt/airflow/data
And ensured all input/output file folders were inside the data/ directory that’s mounted correctly.

📸 Supporting Logs & Screenshots
We will upload the following to this repository:

Screenshots of successful DAG runs

Logs of failed attempts due to misconfiguration

Code snippets that highlight our validation logic

This demonstrates:

Our debugging ability

Transparency in failures

Commitment to correctness

✅ Conclusion
These validation DAGs are crucial QA steps in our orchestration platform. They may look simple, but they represent our dedication to data integrity and clean pipeline practices.

This documentation also shows:

Our attention to detail

Our honesty about development challenges

Our readiness to scale this architecture to handle complex enterprise workflows
