# rsid_django_project (name subject to change)
A simple Django project to expand upon and explore all the features that django offers.
This projet is focused on Django and the variant data are just used for example data.

![Unit test](https://github.com/cjvillar/rsid_django_project/actions/workflows/run_django_test.yml/badge.svg)
![Python Formatting](https://github.com/cjvillar/rsid_django_project/actions/workflows/black_format.yml/badge.svg?branch=main)

![Metadata Dogs GitHub stats](https://github-readme-stats.vercel.app/api?username=cjvillar&show_icons=true&theme=synthwave)

## get started
- python -m venv . 
- source ./bin/activate . 
- pip install -r requirements.txt
- python manage.py migrate
- python manage.py runserver
- Create user http://127.0.0.1:8000/signup

### Populate DB

- Changed path in rsid_search/scripts/litvar_api.py to local location of repo
- python rsid_search/scripts/litvar_api.py rs12516 username
> This code hits the https://www.ncbi.nlm.nih.gov/research/bionlp/litvar/api/v1/entity/litvar/ API. Thanks NCBI! 

Try these: rs80356921, rs8179066

### API
API access via cmnd line:
http -a admin:admin http://127.0.0.1:8000/variants/api/v1/rsid

Browser: http://127.0.0.1:8000/variants/api/v1/rsid

## Contributing
Please join us in the fun! Pull requests are welcome. For major changes, please open an issue/ticket on our [Project](https://github.com/orgs/the-metadata-dog/projects?type=new) to discuss what you would like to change.



