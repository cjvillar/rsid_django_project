import json
import os, sys
from re import U
import requests
import argparse

sys.path.append("/Users/chrisv/rsid_django_project/")
sys.path.append("rsid_django_project/")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "rsid_search.settings")
import django

django.setup()

from rsid_catalog.models import Rsids, User


def rs_from_file(infile):
    rs_list = []
    if infile is not None:
        with open(infile,"r") as f:
            for line in f:
                rs_list.append(line.rstrip("\r\n"))
        return rs_list
        
def litvar_url(rs, username):
    user = User.objects.get(username=username)
    url = "https://www.ncbi.nlm.nih.gov/research/bionlp/litvar/api/v1/entity/litvar/{}%23%23".format(
        rs
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

        return rs_id, diseases, response, gene, data.keys()
    except ValueError as e:
        print(e)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--infile', help='input file, with rsIDs on each line')
    parser.add_argument('--rs')
    parser.add_argument('username')
    arguments = parser.parse_args()
    username = arguments.username
    rs = arguments.rs
    infile = arguments.infile
    rs_list = rs_from_file(infile)
    if rs_list != None:
        for rs in rs_list:
            print(litvar_url(rs, username))
    print(litvar_url(rs, username))
