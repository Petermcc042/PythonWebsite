from flask import Flask, render_template, jsonify, request, session
#from flask_sitemap import Sitemap
import markdown

import os




app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'your_secret_key')  # Use environment variable for production
#ext = Sitemap(app=app)



import plotly.graph_objs as go
import plotly.io as pio

@app.route('/index')
def index():
    return '''
        <form action="/plot" method="get">
            <label>Select X-axis values:</label>
            <input type="text" name="x" value="1, 2, 3, 4, 5"><br>
            <label>Select Y-axis values:</label>
            <input type="text" name="y" value="1, 4, 9, 16, 25"><br>
            <button type="submit">Generate Plot</button>
        </form>
    '''

@app.route('/plot')
def plot():
    # Get the x and y data from the query parameters
    x_data = [int(i) for i in request.args.get('x', '').split(',')]
    y_data = [int(i) for i in request.args.get('y', '').split(',')]

    # Create a Plotly figure
    fig = go.Figure(data=[go.Scatter(x=x_data, y=y_data, mode='lines+markers')])
    fig.update_layout(title='Generated Plotly Chart', xaxis_title='X-axis', yaxis_title='Y-axis')

    # Convert Plotly figure to HTML
    graph_html = pio.to_html(fig, full_html=False)

    # Pass the HTML to the template
    return render_template('plot.html', plot_html=graph_html)

def return_markdown(file_name):
    # Path to the Markdown file
    markdown_file_path = os.path.join('markdown_files', file_name)
    
    # Read the Markdown file
    with open(markdown_file_path, 'r') as file:
        article_content = file.read()

    # Convert Markdown to HTML
    html_content = markdown.markdown(article_content)
    return html_content

def return_html(file_name):
    # Path to the Markdown file
    html_file_path = os.path.join('markdown_files', file_name)

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


##################  Data Analysis Tutorials ########################


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
def gsheets_index_match_sumif():
    return render_template('gsheets/gs_index_match_sumifs.html', 
                           article_content=return_markdown('index_match_sumif.md'))

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

if __name__ == '__main__':
    app.run(debug=True)