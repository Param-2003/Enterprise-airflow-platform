from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import os
# import boto3  # If we were really using S3

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2025, 6, 15),
    'retries': 0,
}

def realistic_s3_ingestion(execution_date):
    """
    Example: Download from S3 and save locally
    """
    s3_key = f"raw-data/{execution_date}.csv"
    local_path = f"/opt/airflow/data/input_data/{execution_date}.csv"

    # # Actual logic (commented for GitHub visibility)
    # s3 = boto3.client('s3')
    # s3.download_file('my-bucket-name', s3_key, local_path)

    # Dummy simulation
    print(f"📦 Simulating S3 ingestion for: {execution_date}")
    print(f"✅ Data (pretend) saved to: {local_path}")

def s3_ingestion_task(**context):
    execution_date = context['ds']
    realistic_s3_ingestion(execution_date)

with DAG(
    dag_id='simulate_s3_ingestion_dag',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=True,
    tags=['simulation', 's3', 'ingestion'],
) as dag:

    ingest = PythonOperator(
        task_id='simulate_s3_ingestion',
        python_callable=s3_ingestion_task,
        provide_context=True
    )
