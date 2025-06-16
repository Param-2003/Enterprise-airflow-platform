## 🔄 Simulated DAGs: S3 Ingestion & ETL Processing

In a real-world production environment, the data pipeline would include S3 ingestion and heavy transformation logic. However, due to **limited budget and local processing power**, we performed all actual data transformation outside the Airflow system (e.g., using Jupyter notebooks or external scripts). The DAGs in this section simulate a complete orchestration system without actually executing the full ETL logic inside the container.

These simulated DAGs are still **architecturally accurate**, so this project can be scaled to production with minimal changes.

---

### 1. 📦 `simulate_s3_ingestion_dag.py`

**What it does (simulated):**
- Pretends to download a date-partitioned CSV from an S3 bucket.
- Logs the intended path where it would be stored.

**What it would do (real logic inside):**
- Use `boto3` to download a file from S3 like:  
  `s3.download_file(bucket, s3_key, destination_path)`

---

### 2. ⚙️ `simulate_etl_processing_dag.py`

**What it does (simulated):**
- Simulates reading the ingested file and performing ETL logic.
- Logs the steps: read → transform → group by district → save output.

**What it would do (real logic inside):**
- Use `pandas` to read input, apply business logic (e.g., group by district), and save results.
- Logic is placed in the code but commented out to prevent execution inside limited environments.

---

### 💡 Why Simulation?

- This project was built on a student system with minimal RAM & CPU.
- Transformations and ingestion were completed outside Airflow (e.g., in Jupyter).
- However, we designed the DAGs to simulate real-world orchestration so that:
  - ✅ The DAG code structure looks enterprise-grade
  - ✅ Logic can be swapped in with actual production services later
  - ✅ The DAG logs and task metadata still reflect realistic behavior

---

### ⚠️ Known Mistake: Execution Date Confusion

We made a small mistake while testing:
- We set the DAG's `start_date = datetime(2025, 6, 15)`.
- When running the DAG manually on `2025-06-16`, Airflow still triggered for `2025-06-15`, due to how `catchup=True` works.
- As a result, logs show errors like:
  ```text
  ❌ No input file found for 2025-06-15

⚠️ This is intentional and reflects the type of debugging needed in production pipelines.

📸 Supporting Logs & Screenshots
You’ll find:

Screenshots of the DAG run logs

Task failure messages when input/output files are missing

Simulated print() logs showing each ETL step

🧩 How to Scale This Up
You can easily:

Swap the print() logic with real boto3 and pandas code

Mount real file systems or connect to cloud buckets

Deploy these DAGs on a production Airflow/Kubernetes stack

✅ Summary
These simulated DAGs are a key part of this Airflow project. They:

Mimic realistic orchestration steps

Teach the DAG structure for ingestion & transformation

Are safe for low-resource environments

Provide a launchpad for future production deployment
