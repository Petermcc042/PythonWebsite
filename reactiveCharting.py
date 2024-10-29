import os
import pandas as pd
import plotly.express as px

# Define the path to your datasets
DATASETS_PATH = os.path.join(os.path.dirname(__file__), 'datasets')

def return_datasets():
    # List all files in the given directory
    files = [f for f in os.listdir(DATASETS_PATH) if os.path.isfile(os.path.join(DATASETS_PATH, f))]
    return files

def get_files_with_headers():
    directory = DATASETS_PATH
    files_headers_dict = {}
    
    # List all files in the given directory
    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)
        if os.path.isfile(file_path) and file_path.endswith('.csv'):  # Ensure it's a file and a CSV
            try:
                # Read the CSV file
                df = pd.read_csv(file_path)
                # Get the headers
                headers = list(df.columns)
                # Add to the dictionary
                files_headers_dict[file] = headers
            except Exception as e:
                print(f"Error reading {file}: {e}")
    
    return files_headers_dict

def load_specific_column(file_name, column_name):
    try:
        file_path = os.path.join(DATASETS_PATH, file_name)
        # Read only the specified column from the CSV file
        df = pd.read_csv(file_path, usecols=[column_name])
        df['x_axis'] = range(1, len(df) + 1)
        return df
    except ValueError as e:
        print(f"Error: {e}")
        return None

#data = get_files_with_headers()
#filenames = list(data.keys())
#pdd = load_specific_column('data-export - 2.csv','Opens' )
# take the dataset and select the chosen column

# Dictionary to map dataset names to their corresponding functions
dataset_map = {
    'iris': px.data.iris,
    'gapminder': px.data.gapminder,
    'medals_long': px.data.medals_long
}

# Access the dataset using the dictionary
dataset_function = dataset_map.get("iris")

# Get the data
data = dataset_function()
df = data["sepal_width"]
#df['x_axis'] = range(1, len(df) + 1)

#print(type(df))

#fig = px.scatter(df, x='x_axis', y=col_name, title='Random Numbers vs. Index')
fig = px.histogram(df, x="sepal_width", title=f'Histogram of {"sepal_width"}')
plotly_html = fig.to_html(full_html=False)