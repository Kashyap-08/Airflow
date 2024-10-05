from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'kash',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}

with DAG(
    dag_id = 'first_dag_v5',
    description = 'This is my first dag that is being created',
    default_args = default_args,
    start_date = datetime(2024, 9, 29, 13),
    schedule_interval = '0 */5 * * *'
    # schedule_interval = '@daily'
    # schedule_interval = '*/5 * * * *'   # Explanation  = */5 Every 5 minutes; * (Every hour); * (Every day), * (Every month); * (Every day of the week)

) as dag:
    task1 = BashOperator(
        task_id = 'first_task',
        bash_command= 'echo Hello World! This is my first task!'
    )

    task2 = BashOperator(
        task_id = 'second_task',
        bash_command = 'echo I am the second task and will run after first task.'
    )

    task3 = BashOperator(
        task_id = 'third_task',
        bash_command = 'echo I am task three and will run in paraller to task second'
    )

    # ======== METHOD 1 ===========
    #task1.set_downstream(task2)
    #task1.set_downstream(task3)

    # ========= METHOD 2 =========
    # Use Bit shift operator
    # task1 >> task2
    # task1 >> task3

    # ========= METHOD 3 ===== (Task Dependency method)
    task1 >> [task2, task3]
