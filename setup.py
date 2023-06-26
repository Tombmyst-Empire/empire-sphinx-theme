from setuptools import setup

setup(
    name='empire_sphinx_theme',
    version='1.0',
    packages=["empihre_sphinx_theme"],
    package_data={
        "empire_sphinx_theme": [
            "theme.conf",
            "static/*.*",
        ]
    },
    entry_points={"sphinx.html_themes": ["empiretheme = empire_sphinx_theme"]},
)

