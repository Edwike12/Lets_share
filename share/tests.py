from django.contrib.auth.models import User
from django.test import TestCase
from .models import Project, Profile,Rating

class ProjectTestClass(TestCase):
    def setUp(self):
        user = User.objects.create(
            username="test_user"
        )

        self.project = Project(
            title="Test Photos",
            description="Test Category",
            image="image.png",
            user=user,
        )

    def test_instance(self):
        self.assertTrue(isinstance(self.project, Project))

    def test_save_method(self):
        self.project.save_project()
        projects = Project.objects.all()
        self.assertTrue(len(projects) > 0)
    

    def test_update_project(self):
        self.project.save_project()
        projects = Project.objects.all()
        self.assertTrue(len(projects) > 0)

    def test_delete_method(self):
        self.project.save_project()
        self.project.delete_project()
        projects = Project.objects.all()
        self.assertTrue(len(projects) == 0)

class RatingTestClass(TestCase):
    def setUp(self):
        user = User.objects.create(
            username="test_user"
        )

        self.rating = Rating(
            user=user,
        )

    def test_instance(self):
        self.assertTrue(isinstance(self.rating, Rating))

