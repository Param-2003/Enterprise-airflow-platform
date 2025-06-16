from datetime import datetime
import os
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
def check_input_file(**context):
    # Get the execution date passed by Airflow (not system date!)
    execution_date = context['ds']  # Format: '2025-06-15'
    date_str = datetime.strptime(execution_date, "%Y-%m-%d").strftime("%d-%m-%Y")

    file_name = f"districtLevel_{date_str}.csv"
    folder_path = "/opt/airflow/data/Input_data/"
    full_path = os.path.join(folder_path, file_name)

    if not os.path.exists(full_path):
        raise FileNotFoundError(f"❌ No input (CSV) file found for date {date_str} in {folder_path}")
    
    print(f"✅ Found input file: {full_path}")


with DAG(
    dag_id='check_input_file_dag',
    schedule_interval='@daily',
    start_date=days_ago(1),
    catchup=False,
    tags=['validation'],
) as dag:

    check_input_file_task = PythonOperator(
        task_id='check_input_file',
        python_callable=check_input_file,
        provide_context=True,  # Important to get execution_date
    )
