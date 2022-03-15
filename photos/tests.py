import datetime
from turtle import title
from unicodedata import name

from django.test import TestCase
from django.utils import timezone

from django.contrib.auth.models import User

from .models import Gallery


class GalleryModelTests(TestCase):

    def setUp(self):
        """
        Gallery setup test env
        """
        user = User.objects.create(username="qwe", password="qwer123423")
        Gallery.objects.create(title="test 1", description="test desc", owner=user)

    def test_gallery_create(self):
        """
        test title and description
        """
        test1 = Gallery.objects.get(title="test 1")

        self.assertEqual(test1.title, "test 1")
        self.assertEqual(test1.description, "test desc")