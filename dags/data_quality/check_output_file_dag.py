from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import os

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2025, 6, 15),
    'retries': 0,
}

def check_output_file(**context):
    execution_date = context['ds']
    date_str = datetime.strptime(execution_date, "%Y-%m-%d").strftime("%d-%m-%Y")

    file_name = f"statecodes_output_{date_str}.csv"
    folder_path = "/opt/airflow/data/Output_data/"
    full_path = os.path.join(folder_path, file_name)

    if not os.path.exists(full_path):
        raise FileNotFoundError(f"❌ Output file NOT found: {full_path}")
    
    print(f"✅ Output file found: {full_path}")

with DAG(
    dag_id='check_output_file_dag',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=True,
    tags=['validation', 'file-check'],
) as dag:

    check_output = PythonOperator(
        task_id='check_output_file',
        python_callable=check_output_file,
        provide_context=True
    )
