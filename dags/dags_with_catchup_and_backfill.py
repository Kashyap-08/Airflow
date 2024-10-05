from datetime import timedelta, datetime

from airflow.operators.bash import BashOperator
from airflow import DAG

default_args = {
    'ownder': 'kash',
    'retries':5,
    'retry_delay':timedelta(minutes=5)
}

with DAG(
    dag_id = 'dag_with_catchup_and_backfill_V3',
    default_args = default_args,
    start_date = datetime(2024, 9, 28),
    schedule_interval = '@daily',
    catchup=False
) as dag:
    task1 = BashOperator(
        task_id = 'task1',
        bash_command = 'echo This is the simple bash command!'
    )