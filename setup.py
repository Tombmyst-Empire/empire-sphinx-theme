from setuptools import setup

setup(
    name='empire_sphinx_theme',
    version='1.0',
    entry_points = {
        'sphinx.html_themes': [
            'empire_sphinx_theme = your_package',
        ]
    }
)

