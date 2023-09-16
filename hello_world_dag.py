from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def helloworld():
    print("Hello World")
    
with DAG(dag_id = "hello_world_dag",
         start_date=datetime(2023,9,16),
         schedule="@hourly",
         catchup=False) as dag:
    
    task1 = PythonOperator(
        task_id = "hello_world",
        python_callable=helloworld
    )
    
task1