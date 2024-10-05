from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    'ownder': 'kash',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}

with DAG(
    default_args = default_args,
    dag_id = 'dag_with_cron_expression_V5',
    start_date = datetime(2024, 9, 1),
    # schedule_interval = '@daily',
    # schedule_interval = '0 0 * * *',        # cron expression for running the dag daily
    # schedule_interval = '0 3 * * Tue',          # cron expression to run dag on Tuesday 3:00 AM Every Week.
    schedule_interval = '0 14 * * Tue,Fri',          # cron expression to run dag on Tuesday ad Friday 14:00 PM Every Week.
    catchup = True
) as dag:
    task1 = BashOperator(
        task_id = 'task1',
        bash_command= 'echo Testing Airflows Schedule Intervals'
    )
