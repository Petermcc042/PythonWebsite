from utils.data_loader import load_data

def create_chart_data(file_path, x_column, y_column, chart_type):
    df = load_data(file_path)
    x_data = df[x_column].tolist()
    y_data = df[y_column].tolist()
    return {
        "type": chart_type,
        "data": {
            "labels": x_data,
            "datasets": [{
                "label": f"{y_column} by {x_column}",
                "data": y_data
            }]
        }
    }
