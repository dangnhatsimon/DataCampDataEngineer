# Import the BashOperator
from airflow.operators.bash import BashOperator

with DAG(dag_id="test_dag", default_args={"start_date": "2024-01-01"}) as analytics_dag:
  # Define the BashOperator 
    cleanup = BashOperator(
        task_id="cleanup_task",
        # Define the bash_command
        bash_command="cleanup.sh",
    )



# Define a second operator to run the `consolidate_data.sh` script
consolidate = BashOperator(
    task_id='consolidate_task',
    bash_command="consolidate_data.sh"
    )

# Define a final operator to execute the `push_data.sh` script
push_data = BashOperator(
    task_id="pushdata_task",
    bash_command="push_data.sh"
    )



# Define a new pull_sales task
pull_sales = BashOperator(
    task_id='pullsales_task',
    bash_command="wget https://salestracking/latestinfo?json"
)

# Set pull_sales to run prior to cleanup
pull_sales >> cleanup

# Configure consolidate to run after cleanup
cleanup >> consolidate

# Set push_data to run last
consolidate >> push_data
