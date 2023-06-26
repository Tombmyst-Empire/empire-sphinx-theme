from setuptools import setup

# 'setup.py'
setup(
    name="empire-sphinx-theme",
    version="1.0",
    author="Yann Tremblay",
    entry_points = {
        'sphinx.html_themes': [
            'empire_sphinx_theme = empire_sphinx_theme'
        ]
    }
)

# 'your_package.py'
from os import path

def setup(app):
    app.add_html_theme('empire_sphinx_theme', path.abspath(path.dirname(__file__)))