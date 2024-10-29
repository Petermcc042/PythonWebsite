How to use Markdown Files in Flask
=====================================

This article is just a quick example of how I use Markdown files to populate the content of this site. I got the idea partly due to my laziness in writing articles which I saw could be fixed using a CMS system. The ability to use normal word documents or text files greatly speeds up the process of creating web pages. 

<h1 id="summary"></h1>

## Summary
This tutorial explains how you can add markdown files into a html page in Flask.
The simple process is as follows

- Read markdown file and translate to html
- pass the html translate as a variable when rendering html file
- include the variable in the html file

<h1 id="markdownFiles"></h1>

## Markdown Files
Markdown files use normal text writing combined with basic syntax formatting which can be used to create formatted HTML pages. You can find out more about it here. [Markdown](https://www.markdownguide.org/getting-started/)

Using Markdown allows you to write normal text files and convert this to html rather simply. Rather than focusing on adding paragraph tags or header tags you pass in a markdown file and convert it. In Flask this is a simple process.

<h1 id="convertMd"></h1>

## Read Markdown and Convert
I am going to assume by the stage your are looking at this you have a functioning Flask backend with a basic homepage at least.

In your folders create a folder in the route directory named markdown_files. In your python script create a function that will convert the markdown files to html (shown below). You will also need to install the markdown package ("os" is already installed as default)

<pre><code class="language-python">
import markdown
import os

def return_markdown(file_name):
    # Path to the Markdown file
    markdown_file_path = os.path.join('mysite\markdown_files', file_name)
    
    # Read the Markdown file
    with open(markdown_file_path, 'r') as file:
        article_content = file.read()

    # Convert Markdown to HTML
    html_content = markdown.markdown(article_content)
    return html_content
</code></pre>

This function takes the file name you pass in and searches the markdown_files folder for it. It then takes the file and converts it to html before returning the new html file.

<h1 id="pass-variable"></h1>

## Pass HTML as Variable
Then all that is left to do is use this new function to render a page. Below is an example of how I use it 

<pre><code class="language-python">
@app.route('/webDev/FlaskMarkdown')
def flaskMarkdown():
    return render_template("web_dev/flaskMarkdown.html",
                           article_content=return_markdown('markdownFlaskFile.md'))
</code></pre>

The code above shows the classic way of creating html pages using Flask. You create the url route in the first line followed by the function you will call. then to present a html file you call render_template followed by the html file. The difference here is that we also pass a variable called **article_content**. To keep the code nice and neat we simply call the function created previously passing in the markdown file we wish to render.

<h1 id="include-variable"></h1>

## Include Variable In HTML
When this function is called the html file "flaskMarkdown.html" is rendered above. To include the markdown file in this you need to have an additional piece of code in the html page shown below.

<pre><code class="language-python">
{{ article_content | safe }}
</code></pre>

Passing the variable inside a HTML file allows you to add styling and positioning easily and lets you focus on the most annoying part of building HTML which is the text content. You can also create template HTML files which inherit from each other so that the styling and formating is the same across your site. Meaning you can very quickly write content and publish it without having to worry about creating a brand new custom HTML file each time.
