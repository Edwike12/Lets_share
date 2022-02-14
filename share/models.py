from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    profile_photo=CloudinaryField('image')
    name=models.TextField(max_length=50)
    user=models.OneToOneField(User,on_delete=models.CASCADE, related_name='profile')
    bio=models.TextField(null=True, max_length=1000)
    email=models.CharField(null=True, max_length=50)
    phone_number=models.IntegerField(null=True)

    @receiver(post_save , sender = User)
    def create_profile(instance,sender,created,**kwargs):
      if created:
        Profile.objects.create(user = instance)

    @receiver(post_save,sender = User)
    def save_profile(sender,instance,**kwargs):
      instance.profile.save()

      def __str__(self):
        return f'{self.user.username} profile'


# class Project(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
#     title = models.CharField(max_length=50)
#     image = CloudinaryField("image")
#     description = models.TextField(max_length=600)
#     category = models.TextField(max_length=50, null=True)
#     location = models.CharField(max_length=50, default="Kenya")
#     date = models.DateTimeField(auto_now_add=True, null=True)
#     url = models.URLField(null=True)

    
#     @classmethod
#     def search_project_name(cls, search_term):
#         projects = cls.objects.filter(
#         title__icontains=search_term)
#         return projects    

#     def str(self):
#         return self.user.username

#     @classmethod
#     def get_project_by_id(cls, id):
#         project = cls.objects.get(id=id)
#         return project

#     @classmethod
#     def get_all_projects(cls):
#         projects = cls.objects.all()
#         return projects

#     @classmethod
#     def get_all_projects_by_user(cls, user):
#         projects = cls.objects.filter(user=user)
#         return projects

#     def update_project(self, **kwargs):
#         for key, value in kwargs.items():
#             setattr(self, key, value)
#         self.save()

#     def save_project(self):
#         self.save()

#     def delete_project(self):
#         self.delete()

#     def __str__(self):
#         return self.title

# class Rating(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     project = models.ForeignKey(Project, on_delete=models.CASCADE)
#     design_rate = models.IntegerField(default=0, blank=True, null=True)
#     usability_rate = models.IntegerField(default=0, blank=True, null=True)
#     content_rate = models.IntegerField(default=0, blank=True, null=True)
#     avarage_rate = models.IntegerField(default=0, blank=True, null=True)

#     def _str_(self):
#         return self.user.username

#     def update_rating(self, **kwargs):
#         for key, value in kwargs.items():
#             setattr(self, key, value)
#         self.save()

#     def save_rating(self):
#         self.save()

#     def delete_rating(self):
#         self.delete()

#     def __str__(self):
#         return self.project