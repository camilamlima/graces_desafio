import airflow
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import timedelta

default_args = {
    'start_date': airflow.utils.dates.days_ago(0),
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}
dag = DAG(
    'dag_whats',
    default_args=default_args,
    description='import datasets whatsapp',
    schedule_interval='@hourly',
    dagrun_timeout=timedelta(minutes=60))

t1 = BashOperator(
    task_id='import_whatsapp',
    bash_command='python3 /mnt/c/dag/scripts/importa_whatsapp.py',
    dag=dag,
    depends_on_past=False)
