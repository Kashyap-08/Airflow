from airflow import DAG
from airflow.operators.python import PythonOperator

from datetime import datetime, timedelta

def get_sklearn():
    import sklearn
    print(f" Scikit-learn with Version: {sklearn.__version__}")

def get_matplotlib():
    import matplotlib
    print(f" matplotlib with Version: {matplotlib.__version__}")


default_args = {
    'owner': 'kash',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}

with DAG(
    default_args = default_args,
    dag_id = 'dag_to_test_install_packages_V02',
    start_date = datetime(2024, 10, 3),
    schedule_interval = '@daily'
) as dag:
    get_sklearn = PythonOperator(
        task_id = 'get_sklearn',
        python_callable = get_sklearn
    )

    get_matplotlib = PythonOperator(
        task_id = 'get_matplotlib',
        python_callable = get_matplotlib
    )

    get_sklearn >> get_matplotlib
