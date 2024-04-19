from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator
import sys
import os

# Ensure the scripts folder is in the PATH
dag_dir = os.path.dirname(os.path.realpath(__file__))
scripts_dir = os.path.join(dag_dir, 'scripts')
sys.path.append(scripts_dir)

# from scripts.transformation import transform_data
# from scripts.s3_config import upload_to_s3

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email': ['your_email@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    'data_processing_pipeline',
    default_args=default_args,
    description='A simple pipeline that runs a data transformation and then uploads to S3.',
    schedule_interval=timedelta(days=1),
    start_date=datetime(2024, 1, 1),
    catchup=False,
) as dag:

    transform_task = BashOperator(
        task_id='run_transformation',
        bash_command="python3 /opt/airflow/dags/scripts/transformation.py",
    )

    upload_to_s3_task = BashOperator(
        task_id='upload_transformed_data_to_s3',
        bash_command="python3 /opt/airflow/dags/scripts/s3_config.py",
        dag=dag,
    )

    check_sklearn_installation_task = BashOperator(
    task_id='check_sklearn_installation',
    bash_command="python3 /opt/airflow/dags/scripts/check_module.py",
    )

    check_sklearn_installation_task >> transform_task >> upload_to_s3_task