from google.cloud import bigquery
import os

def query_bigquery():
    # Set the path to your service account key file
    service_account_key_path = 'mysite\pro-icon-424409-m5-7873eec57d9a.json'
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = service_account_key_path

    # Create a BigQuery client
    client = bigquery.Client()

    # Define your query
    query = """
    SELECT * 
    FROM `pro-icon-424409-m5.spotify_dataset.spotify_table`
    LIMIT 10
    """

    # Execute the query
    query_job = client.query(query)

    # Wait for the query to finish
    results = query_job.result()

    # Process the results
    for row in results:
        print(row)

def list_datasets():
    # Set the path to your service account key file
    service_account_key_path = 'mysite\pro-icon-424409-m5-7873eec57d9a.json'
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = service_account_key_path

    # Create a BigQuery client
    client = bigquery.Client()

    datasets = client.list_datasets()  # Make an API request
    project = client.project

    if datasets:
        print(f'Datasets in project {project}:')
        for dataset in datasets:
            print(f'\t{dataset.dataset_id}')
    else:
        print(f'No datasets found in project {project}.')

if __name__ == "__main__":
    query_bigquery()
    list_datasets()
