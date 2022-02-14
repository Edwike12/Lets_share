from django.urls import path
from . import views

urlpatterns=[
   path('',views.index,name = 'index'),
   path('profile/', views.profile, name='profile'),
   path('update_profile/<int:id>', views.update_profile, name='update_profile'),
   path('add_project/', views.add_project, name='add_project'),
   path("project/<int:project_id>/", views.project_details, name="project_details"),
   path('search_project/', views.search_project, name='search_project'),
   path("rate/<int:id>",views.rate, name='rate'),
   path('api/projects/', views.ProjectList.as_view()),
   path('api/profiles/',views.ProfileList.as_view()),

]