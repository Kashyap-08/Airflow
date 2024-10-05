from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import timedelta, datetime


def get_name(ti):
    # return "jerry"
    ti.xcom_push(key = 'first_name', value = 'Kash')
    ti.xcom_push(key = 'last_name', value = 'Kolhe')

def get_age(ti):
    ti.xcom_push(key = 'age', value = 26)

def greet(ti):
    # name = ti.xcom_pull(task_ids = 'get_name')
    # print(f"Hello World!! My name is {name} and my age is {26}")

    first_name  = ti.xcom_pull(task_ids = 'get_name', key = 'first_name')
    last_name  = ti.xcom_pull(task_ids = 'get_name', key = 'last_name')

    age = ti.xcom_pull(task_ids = 'get_age', key = 'age')

    print(f"Hello World!! My name is {first_name} {last_name} and my age is {age}")
    



default_args = {
    'owner': 'kash',
    'retries': 5,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    default_args = default_args,
    dag_id = 'dag_with_pythonOperator_V06',
    description = 'First Dag using Python Operator',
    start_date = datetime(2024, 9, 30),
    schedule_interval = '@daily'
) as dag:
    task1 = PythonOperator(
        task_id = 'greet',
        python_callable = greet
    )

    task2 = PythonOperator(
        task_id = 'get_name',
        python_callable = get_name
    )

    task3 = PythonOperator(
        task_id = 'get_age',
        python_callable = get_age
    )

    # ========= METHOD 1 ============
    # task2 >> task1
    # task3 >> task1
    

    # ======= METHOD 2 ==========
    [task2, task3] >> task1