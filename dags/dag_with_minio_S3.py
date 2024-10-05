from airflow import DAG
from airflow.providers.amazon.aws.sensors.s3 import S3KeySensor

from datetime import datetime, timedelta

default_args = {
    'owner': 'kash',
    'retries':2,
    'retry_delay': timedelta(minutes=5)
}

with DAG(
    default_args = default_args,
    dag_id = 'dag_with_minio_s3_V02',
    start_date = datetime(2024,10,3),
    schedule_interval = '@daily'
) as dag:
    task1 = S3KeySensor(
        task_id = 'sensor_minio_s3',
        bucket_name = 'airflow',
        bucket_key = 'data.csv',
        aws_conn_id = 'minio_conn',
        mode = 'poke',
        poke_interval = 5,
        timeout = 30
    )
    