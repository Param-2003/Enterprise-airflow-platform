# 🧩 DAG Pipeline Flow Overview

This document outlines the structure and logic behind each DAG in the Airflow-based orchestration pipeline. It provides a clear separation of real vs simulated workflows and highlights decision points.

---

## ✅ DAG 1: Input File Validator
- **Filename**: `check_input_file_dag.py`
- **Goal**: Ensure an input file exists for the execution date.
- **Logic**:
  - Construct the expected filename using `{{ ds }}` (i.e., execution date).
  - Validate `.csv` or `.xlsx` format.
  - Print log or raise `FileNotFoundError`.
- **Failure we encountered**:
  - We ran the DAG one day early (`2025-06-15`) so it looked for a file named `2025-06-15.csv`, which didn't exist.
  - Misinterpreted `.csv` vs `.xlsx` at first.
  - Fixed volume mount paths for Docker correctly later.

---

## ✅ DAG 2: Output File Validator
- **Filename**: `check_output_file_dag.py`
- **Goal**: Verify that the output file after ETL is available.
- **Logic**:
  - Dynamically construct expected filename using `{{ ds }}`.
  - Check file presence and optionally verify it's not empty.
  - Logs simulate success/failure feedback.
- **Failure we encountered**:
  - Path bugs due to Docker mount points.
  - File not written due to transformation script running outside Airflow.

---

## ⚙️ DAG 3: Simulated Ingestion Pipeline
- **Filename**: `simulate_s3_ingestion_dag.py`
- **Goal**: Simulate a full S3 ingestion DAG.
- **Logic**:
  - Logs for: connection check, pulling file from S3, writing to local.
  - No actual S3 access; everything is printed.
- **Why simulation?**
  - Due to local environment constraints.
  - Showcases orchestration without real cloud dependency.

---

## ⚙️ DAG 4: Simulated ETL Flow
- **Filename**: `simulate_etl_transformation_dag.py`
- **Goal**: Simulate a full ETL pipeline transformation DAG.
- **Logic**:
  - Prints logs of typical ETL steps:
    - Data loading
    - Cleaning
    - Feature engineering
    - Writing output
  - Skips actual transformation due to resource limits.
- **Why simulation?**
  - We perform actual transformations in a Jupyter Notebook (outside Airflow).
  - Still want the orchestration logic to look complete in Airflow UI and logs.

---

## 📌 Notes:
- We follow modular DAG design: 1 DAG = 1 job.
- We simulate realistic logs, metadata, and structure even if actual processing is offloaded.
- Docker volume mount issues taught us that the path inside container **must match** `volume` path in `docker-compose.yml`.

---

✅ This pipeline structure is ready for extension into a real cloud or production environment.
