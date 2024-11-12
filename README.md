# Flask App Project

This is a simple Flask web application that demonstrates how to structure a project with templates and static files.

## Project Structure

The project follows the typical Flask application layout with `app.py` (or `app2.py` in this case), `templates/` for HTML files, and `static/` for CSS/JS files.

Here is the directory structure:


app/
│
├── app2.py                     # Flask application code
│
├── templates/                   # HTML templates folder
│   ├── base2.html               # Base HTML structure
│   ├── index2.html              # Home page template
│   └── login_details.html       # Login details page template
│
└── static/                      # Static files (CSS, JS, images)
    └── css/
        └── main2.css            # CSS file for styling


app.py: Contains the Flask app logic and routes.
templates/: Stores HTML files.
base.html: Common structure.
index.html: The main page.
login_details.html: Login-specific page.
static/: For static files like CSS or JavaScript.
css/main.css: A CSS file that you can link in your HTML templates.
