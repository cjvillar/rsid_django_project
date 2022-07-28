# rsid_django_project
A simple Django project.

## get started
- python3 -m venv .
- source ./bin/activate
(check your path for django and make sure its using django 3.0)
- pip install -r requirements.txt
- python manage.py migrate
- python manage.py runserver

### Populate DB

`
python rsid_search/scripts/litvar_api.py rs12516 admin
python rsid_search/scripts/litvar_api.py rs80356921 admin
python rsid_search/scripts/litvar_api.py rs8179066 admin
`
### API
`API access via cmnd line:
http -a admin:admin http://127.0.0.1:8000/variants/api/v1/rsid

Browser: http://127.0.0.1:8000/variants/api/v1/rsid
`