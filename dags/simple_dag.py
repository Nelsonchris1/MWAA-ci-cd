from airflow.models import DAG
from airflow.utils.dates import days_ago
from airflow.operators.dummy_operator import DummyOperator


with DAG(
   "etl_sales_daily",
   start_date=days_ago(1),
   schedule_interval=None,
) as dag:
    task_a = DummyOperator(task_id="task_ab")
    task_b = DummyOperator(task_id="task_bb")
    task_c = DummyOperator(task_id="task_cb")
    task_d = DummyOperator(task_id="task_db")
    task_a >> [task_b, task_c]
