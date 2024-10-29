from flask import Flask, render_template, jsonify, request, session
#from flask_sitemap import Sitemap
import plotly.express as px
import plotly.graph_objects as go
import markdown
import os
import pandas as pd
from itables import init_notebook_mode

import reactiveCharting as rc



app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Set a secret key for sessions
#ext = Sitemap(app=app)

def return_markdown(file_name):
    # Path to the Markdown file
    markdown_file_path = os.path.join('mysite\markdown_files', file_name)
    
    # Read the Markdown file
    with open(markdown_file_path, 'r') as file:
        article_content = file.read()

    # Convert Markdown to HTML
    html_content = markdown.markdown(article_content)
    return html_content

def return_html(file_name):
    # Path to the Markdown file
    html_file_path = os.path.join('mysite\markdown_files', file_name)

    # Read the HTML file with UTF-8 encoding
    try:
        with open(html_file_path, 'r', encoding='utf-8') as file:
            html_content = file.read()
    except UnicodeDecodeError as e:
        print(f"Error reading {file_name}: {e}")
        return "Error loading content."

    return html_content


@app.route('/')
def home():
    return render_template("navigation/home.html")

# @app.route('/sitemap.xml')
# def sitemap():
#     return render_template("sitemap.xml")

@app.route('/tutorials_list')
def tutorials_list():
    return render_template("navigation/tutorial_list_home.html")

@app.route('/cv/')
def cv():
    return render_template("cv.html",
                           article_content=return_markdown('cv.md'))

from flask_socketio import SocketIO, emit
import jedi

socketio = SocketIO(app)

@socketio.on('get_suggestions')
def get_suggestions(data):
    code = data['code']
    line = data['line']
    column = data['column']
    script = jedi.Script(code, line, column)
    completions = script.complete()
    suggestions = [{'label': c.name, 'kind': c.type, 'insertText': c.name} for c in completions]
    emit('suggestions', suggestions)

@app.route('/input/')
def input():
    return render_template("input.html")


# Create dummy data
data = {
    'Name': ['A', 'B', 'C', 'D', 'E'],
    'Value': [10, 20, 30, 40, 50],
    'Category': ['X', 'Y', 'X', 'Y', 'X']
}
df = pd.DataFrame(data)


##################  Data Analysis Tutorials ########################

# Route for the main page
@app.route('/bigqueries', methods=['GET', 'POST'])
def bigqueries():
    results = None
    if request.method == 'POST':
        user_query = request.form['query']
        
        # Create a BigQuery client
        ##client = bigquery.Client()

        # Execute the query
        #query_job = client.query(user_query)
        
        # Wait for the query to finish
        #results = query_job.result()

        # Convert results to a list of dictionaries
        results = [dict(row) for row in results]

    return render_template('index.html', results=results)

##################  Data Science Tutorials ########################
@app.route('/decisiontreetut/')
def decisiontreetut():
    return render_template("data_science/decision_tree.html")

@app.route('/knearest/')
def knearest():
    return render_template("data_science/k_nearest.html")

@app.route('/custclust/')
def custclust():
    return render_template("data_science/custclust.html",
                           article_content=return_markdown('customer_clustering.md'))


##################  Google Sheets Tutorials ########################
@app.route('/gs_home/')
def gs_home():
    return render_template("gsheets/gs_home.html")

@app.route('/gs/index_match_sumifs')
def gs_index_match_sumifs():
    return render_template('gsheets/GS_index_match_sumifs.html', 
                           article_content=return_markdown('customer_clustering.md'))

@app.route('/gsheets/test')
def gsheets_test():
    return render_template('gsheets/GS_test.html', 
                           article_content=return_markdown('content.md'))

@app.route('/gsheets/xlookup_vs')
def gsheets_xlookup():
    return render_template('gsheets/gs_xlookup_vs.html', 
                           article_content=return_markdown('xlookup.md'))

##################  R Tutorials ########################
@app.route('/r_basics/')
def r_basics():
    return render_template("Learn_R/r_basics.html")

##################  WEB DEV ########################
@app.route('/webDev/stickyNav')
def stickyNav():
    return render_template("web_dev/stickyNav.html",
                           article_content=return_markdown('fixed_navbar.md'))

@app.route('/webDev/FlaskMarkdown')
def flaskMarkdown():
    return render_template("web_dev/flaskMarkdown.html",
                           article_content=return_markdown('markdownFlaskFile.md'))



# Dictionary to map dataset names to their corresponding functions
dataset_map = {
    'iris': px.data.iris,
    'gapminder': px.data.gapminder,
    'medals_long': px.data.medals_long
}


@app.route('/charting_using_POST/')
def charting_using_POST():
    filenames = [px.data.iris.__name__, px.data.medals_long.__name__]

    return render_template('data_analysis/bigQueryQuery.html', 
                           filenames=filenames,
                           article_content=return_markdown('big_query.md'))




@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        # Retrieve dataset name from the form
        dataset_name = request.form['dataset_name']

        # Store dataset name in session
        session['_dataset_name'] = dataset_name

        # Display the selected dataset
        selected_dataset = "Selected Dataset: " + dataset_name

        # Access the dataset using the dictionary
        dataset_function = dataset_map.get(dataset_name)

        if dataset_function is None:
            return "Dataset not found", 404

        # Get the data
        data = dataset_function()
        tempdata = data.head()

        # Get column names
        colNames = data.columns
        
        filenames = [dataset_name]

        # Pass the data to the template
        return render_template('data_analysis/bigQueryQuery.html',
                               filenames=filenames,
                               selected_dataset=selected_dataset, 
                               colNames=colNames,
                               table_html=tempdata.to_html(),
                               article_content=return_markdown('big_query.md'))


@app.route('/submit_col', methods=['POST'])
def submit_col():
    if request.method == 'POST':

        dataset_name = session.get('_dataset_name')
        selected_dataset = [dataset_name]

        col_name = request.form['colName']  
        selected_column = [col_name]
        session['_colName'] = col_name

        # Access the dataset using the dictionary
        dataset_function = dataset_map.get(dataset_name)

        
        if dataset_function is None:
            return "Dataset not found", 404


        col_name = col_name

        data = dataset_function()

        df = data[col_name]
    
        fig = px.histogram(df, x=col_name, title=f'Histogram of {col_name}')
        plotly_html = fig.to_html(full_html=False)

        # Pass the data to the template
        return render_template('data_analysis/bigQueryQuery.html',
                               filenames=selected_dataset,
                               selected_dataset=selected_dataset,
                               colNames=selected_column,
                               selected_column=selected_column,
                               plot_html=plotly_html,
                               article_content=return_markdown('big_query.md'))

    


##################  PORTFOLIO WEBSITE ########################
@app.route('/build_your_own_portfolio_website/')
def pw_setup():
    return render_template("portfolio_website/pw_setup.html")

@app.route('/build_your_own_portfolio_website/python_setup')
def pw_python_setup():
    return render_template("portfolio_website/pw_python_setup.html")

@app.route('/build_your_own_portfolio_website/flask_code')
def pw_flask_code():
    return render_template("portfolio_website/pw_flask_code.html")

@app.route('/build_your_own_portfolio_website/css_code')
def pw_css_code():
    return render_template("portfolio_website/pw_css_code.html")

@app.route('/build_your_own_portfolio_website/run_locally')
def pw_run_locally():
    return render_template("portfolio_website/pw_run_locally.html")

@app.route('/build_your_own_portfolio_website/hosting')
def pw_hosting():
    return render_template("portfolio_website/pw_hosting.html")

##################  Old Projects Tutorials ########################

@app.route('/covidanalysis/')
def covidanalysis():
    return render_template("old_projects/covidtableaupublic.html")

@app.route('/using_ml_in_banking_churn/')
def bankingchurn():
    return render_template("old_projects/bankingchurn.html")

@app.route('/shiny_dashboard/')
def shiny_dash():
    return render_template("old_projects/shiny_dash.html")

@app.route('/walmartanalysis/')
def walmartanalysis():
    return render_template("old_projects/walmart_analysis.html")

##################  REGRESSION PREDICTION ########################
#@app.route('/regressionprediction/', methods = ["GET","POST"])
#def regpredweb():
#    if request.method == "POST":
#        hrs = request.form["hours"]
#        markpred = sm.marksprediction(hrs)
#        bar = sm.create_plot(hrs,markpred)
#    else:
#        markpred = 0
#        bar = sm.create_plot(0,0)
#    
#    return render_template("regpredweb.html", mymark = markpred, plot = bar)

##################  REGRESSION PREDICTION ########################
@app.route('/regressionprediction/')
def regpredweb():
    return render_template("home.html")


if __name__ == "__main__":
    socketio.run(app, debug=True)