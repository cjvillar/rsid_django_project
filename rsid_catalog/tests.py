from turtle import title
from django.test import TestCase

# Create your tests here.
from rsid_catalogue.models import Notes

class NotesTestCase(TestCase):
    def setUp(self):
        Notes.objects.create(title="Note 1", text="This is a test 1")
        Notes.objects.create(title="Note 2", text="This is a test 2")

    def test_notes_are_created(self):
        """Ensure Notes are created correctly"""
        note_1 = Notes.objects.get(title="Note 1")
        note_2 = Notes.objects.get(title="Note 2")
        
        self.assertEqual(note_1.title, 'Note 1')
        self.assertEqual(note_2.title, 'Note 2')
        
