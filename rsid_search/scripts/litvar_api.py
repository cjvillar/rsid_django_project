import json
import os, sys
from re import U
import requests
import argparse
import logging

sys.path.append("/Users/chrisv/rsid_django_project/")
sys.path.append("./rsid_django_project/")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "rsid_search.settings")
import django

django.setup()
logging.basicConfig(level=logging.INFO)

from rsid_catalog.models import Rsids, User


def rs_from_file(rs_ids):
    rs_list = []
    with open(rs_ids,"r") as f:
        for line in f:
            rs_list.append(line.rstrip("\n"))
    return rs_list
        
def litvar_url(rs_list, username):
    user = User.objects.get(username=username)
    for rs_id in rs_list:
        url = "https://www.ncbi.nlm.nih.gov/research/bionlp/litvar/api/v1/entity/litvar/{}%23%23".format(
            rs_id
        )
        response = requests.get(url)
        try:
            data = response.json()
            rs_id = data["id"]
            gene = data["gene"]
            diseases = data["diseases"]
            clean_id = rs_id.strip("##")
            new_id = Rsids.objects.create(
                rs_id=clean_id, diseases=diseases, gene=gene, user=user
            )
            new_id.save()
            
            logging.info(f'{rs_id}, {diseases}, {response}, {gene}.')
            
        except ValueError as e:
            print(e)
    

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('rs_list', help=' an input file with rsIDs on each line')
    parser.add_argument('username')
    arguments = parser.parse_args()
    username = arguments.username
    rs_ids = arguments.rs_list
    rs_list = rs_from_file(rs_ids)
    litvar_url(rs_list , username)
   
