# rsid_django_project (name subject to change)
A simple Django project to expand upon and explore all the features that django offers.
This projet is focused on Django and the variant data are just used for example data.

![Unit test](https://github.com/cjvillar/rsid_django_project/actions/workflows/run_django_test.yml/badge.svg)
![Python Formatting](https://github.com/cjvillar/rsid_django_project/actions/workflows/black_format.yml/badge.svg?branch=main)

## get started
- python -m venv . 
- source ./bin/activate . 
- pip install -r requirements.txt
- python manage.py migrate
- python manage.py runserver
- Create user http://127.0.0.1:8000/signup

### Populate DB
`
python rsid_search/scripts/litvar_api.py rs12516 <username>
python rsid_search/scripts/litvar_api.py rs80356921 <username>
python rsid_search/scripts/litvar_api.py rs8179066 <username>
`
### API
API access via cmnd line:
http -a admin:admin http://127.0.0.1:8000/variants/api/v1/rsid

Browser: http://127.0.0.1:8000/variants/api/v1/rsid

