# To Check version of python
python --version

# To create virtual environment
python -m venv venv

# To activate virtual environment
venv\Scripts\activate

# To install Django inside venv
pip install Django 

# To check Django version
django-admin --version

# To start Project folder
django-admin startproject myproject

# To go inside that folder
cd myproject

# To run server
python manage.py runserver

# To build the application using appName as BLOG
python manage.py startapp blog

# ani teslaii setting.py ma gayera installed app ma naya 'blog' add gara.

# MVT (Model View Templates) priciple of django

# Templates: HTML + Django Template language

{variable} e.g. {name}
{%tag%} e.g. {%if%}, {%for%}