from airflow.decorators import dag, task

from datetime import timedelta, datetime
default_args = {
    'owner': 'Kash',
    'retries': 5,
    'retry_delay': timedelta(minutes = 5),
}


@dag(
    dag_id = 'dag_with_taskflow_api_V2',
    default_args = default_args,
    start_date = datetime(2024, 9, 30),
    schedule_interval = '@daily'
)

def hello_world_etl():

    # Pass single value
    # @task()
    # def get_name():
    #     return 'Kash'

    # Pass multiple values
    @task(multiple_outputs=True)
    def get_name():
        return {
            'first_name':'kash',
            'last_name':'kolhe'
        }
    
    @task()
    def get_age():
        return 26

    @task()
    def greet(first_name, last_name, age):
        print(f"Helllo World!! My name is {first_name} {last_name}, and my age is {age}.")

    
    name_dict = get_name()
    age = get_age()

    greet(name_dict['first_name'], name_dict['last_name'], age)

greet_dag = hello_world_etl()