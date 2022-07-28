from turtle import title
from django.test import TestCase

from rsid_catalog.models import Rsids
from django.contrib.auth.models import User

RSID = "rs12345"
GENE = {"id": 672, "name": "BRCA1"}
DISEASES = {
    "Neoplasms": 7,
    "Breast Neoplasms": 4,
    "Hereditary Breast and Ovarian Cancer Syndrome": 3,
    "Ovarian Diseases": 2,
    "Growth Disorders": 1,
}


class UserWorkflowTestCase(TestCase):
    def setUp(self):
        # create user
        self.user_1 = User.objects.create_user("Tester_1", "thefirstpassword098")
        self.client.login(
            username=self.user_1.first_name, password=self.user_1.password
        )
        # create variant
        self.var = Rsids.objects.create(
            rs_id=RSID, gene=GENE, diseases=DISEASES, user=self.user_1
        )

    def test_login_true(self):
        self.assertTrue(self.client.login)

    def test_Rsids_objects_exist(self):
        """Ensure Rsids are created correctly"""
        get_var = Rsids.objects.get(rs_id=RSID)
        self.assertEqual(get_var.rs_id, RSID)
