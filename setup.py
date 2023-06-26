# 'setup.py'
setup(
    entry_points = {
        'sphinx.html_themes': [
            'empire_theme = empire_theme'
        ]
    }
)

# 'your_package.py'
from os import path

def setup(app):
    app.add_html_theme('empire_theme', path.abspath(path.dirname(__file__)))