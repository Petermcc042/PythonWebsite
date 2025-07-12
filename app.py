from flask import Flask, render_template, jsonify, request, session, redirect, url_for, abort
import markdown
import os
from functools import wraps
from url_config import TUTORIAL_CONFIG

app = Flask(__name__)

def return_markdown(file_name):
    markdown_file_path = os.path.join('markdown_files', file_name)
    with open(markdown_file_path, 'r') as file:
        article_content = file.read()
    html_content = markdown.markdown(article_content)
    return html_content

def return_html(file_name):
    html_file_path = os.path.join('markdown_files', file_name)
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

@app.route('/tutorials_list')
def tutorials_list():
    return render_template("navigation/tutorial_list_home.html")

@app.route('/cv/')
def cv():
    return render_template("cv.html",
                           article_content=return_markdown('cv.md'))

# Single dynamic route to handle all tutorials
@app.route('/<category>/<tutorial_name>/')
def tutorial_handler(category, tutorial_name):
    # Check if category exists
    if category not in TUTORIAL_CONFIG:
        abort(404)
    
    # Check if tutorial exists in category
    if tutorial_name not in TUTORIAL_CONFIG[category]:
        abort(404)
    
    config = TUTORIAL_CONFIG[category][tutorial_name]
    template = config['template']
    
    # Build context for template
    context = {}
    if 'markdown' in config:
        context['article_content'] = return_markdown(config['markdown'])
    
    return render_template(template, **context)



if __name__ == '__main__':
    app.run(debug=True)