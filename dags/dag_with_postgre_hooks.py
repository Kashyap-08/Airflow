from datetime import datetime, timedelta
import csv
import logging
from tempfile import NamedTemporaryFile

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook
from airflow.providers.amazon.aws.hooks.s3 import S3Hook

default_args = {
    'owner': 'kash',
    'retries':2,
    'retry_delay': timedelta(minutes=2)
}

def postgre_to_s3(ds_nodash, next_ds_nodash):
    # step1: query data from postgresql db and save into text file
    hook = PostgresHook(postgres_conn_id = 'postgres_localhost')
    conn = hook.get_conn()
    cursor = conn.cursor()
    cursor.execute(f"""
        select * from orders where date >= '{ds_nodash}' and date < '{next_ds_nodash}'
    """)

    file_name = f"dags/get_orders{ds_nodash}.txt" 
    # with open(file_name, "w") as f:
    with NamedTemporaryFile(mode='w', suffix=f"{ds_nodash}") as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(i[0] for i in cursor.description)
        csv_writer.writerows(cursor)

        f.flush()
    
        cursor.close()
        conn.close()
        logging.info(f"Saved Orders data in text file {f.name}")


        # step2: upload text file into s3 bucker
        s3_hook = S3Hook(aws_conn_id = 'minio_conn')
        s3_hook.load_file(
            filename = f.name,
            key = f"orders/{ds_nodash}.txt",
            bucket_name = 'airflow',
            replace=True
        )
        logging.info(f"Successfully Uploaded file {f.name} to S3 airflow Bucket")

with DAG(
    default_args = default_args,
    dag_id = 'dag_with_postgre_hooks_V04',
    start_date = datetime(2024, 10, 4),
    schedule_interval = '@daily'
) as dag:
    task1 = PythonOperator(
        task_id = "postgres_to_s3",
        python_callable = postgre_to_s3
    )

    task1