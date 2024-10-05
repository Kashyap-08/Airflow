## Follow this vide: https://www.youtube.com/watch?v=Fl64Y0p7rls

## Command to create admin user and password: `docker-compose run airflow-worker airflow users create --role Admin --username admin --email admin --firstname admin --lastname admin --password admin`

## Start the airflow server: `docker-compose up -d`

## Stop the airflow server: `docker-compose down -v`

## To remove all the example dags: 
* get into docker-compose.yaml file.
* Look for `AIRFLOW__CORE__LOAD_EXAMPLES` and set it to `false`.
* Initialize Airflow: `docker-compose up airflow-init`
* Start Airflow server: `docker-compose up -d` 
* 
