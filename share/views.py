from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators  import login_required
from share.forms import *
from share.models import *
from rest_framework import serializers
from rest_framework.views import APIView
from .permissions import IsAdminOrReadOnly
from share import serializer
from django.http import HttpResponseRedirect, Http404
from .serializer import ProfileSerializer, ProjectSerializer
from rest_framework.response import Response

# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    projects = Project.objects.all().order_by('-id')

    return render(request, 'index.html', {'projects':projects})

@login_required()
def profile(request):
    current_user = request.user
    profile = Profile.objects.filter(user_id=current_user.id).first()
    return render(request, "profile.html", {"profile": profile, })


@login_required(login_url='/accounts/login/')
def update_profile(request,id):
    user = User.objects.get(id=id)
    profile = Profile.objects.get(user_id = user)
    form = UpdateProfileForm(instance=profile)
    if request.method == "POST":
            form = UpdateProfileForm(request.POST,request.FILES,instance=profile)
            if form.is_valid():  
                
                profile = form.save(commit=False)
                profile.save()
                return redirect('profile') 
            
    return render(request, 'update_profile.html', {"form":form})   

def add_project(request):
    projects = Project.objects.all().order_by('-id')
    if request.method == 'POST':  
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            com = form.save(commit=False)
            com.user = request.user
            com.save()
            return redirect('index')
    
    else:
        form = ProjectForm() 
    return render (request, 'add_project.html', {'form':form, 'projects':projects})

@login_required(login_url='/accounts/login/')
def search_project(request):    
    if 'search' in request.GET and request.GET['search']:        
        search_term = request.GET.get('search').lower()        
        images = Project.search_project_name(search_term)        
        message = f'{search_term}'
        return render(request, 'search.html', {'found': message, 'images': images})    
    else:        message = 'Not found'        
    return render(request, 'search.html', {'danger': message})
    
@login_required(login_url='/accounts/login/')
def project_details(request, project_id):
    project = Project.objects.get(id=project_id)
    rating = Rating.objects.filter(project = project)
    return render(request, "project_details.html", {"project": project, 'rating':rating})

@login_required(login_url='/accounts/login/')
def rate(request,id):
    if request.method == 'POST':
        project = Project.objects.get(id = id)
        current_user = request.user
        design_rate = request.POST['design']
        content_rate = request.POST['content']
        usability_rate = request.POST['usability']

        Rating.objects.create(
            project=project,
            user=current_user,
            design_rate=design_rate,
            usability_rate=usability_rate,
            content_rate=content_rate,
            avarage_rate=round((float(design_rate)+float(usability_rate)+float(content_rate))/3,2),)

        return redirect('index')
    else:
        project = Project.objects.get(id = id) 
        return render(request,"project_details.html",{"project":project})


class ProjectList(APIView):
    permission_classes = (IsAdminOrReadOnly,)
    def get(self,request,format=None):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects,many=True)
        return Response(serializer.data)

class ProfileList(APIView):
    permission_classes = (IsAdminOrReadOnly,)
    def get(self,request,format=None):
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(profiles,many=True)
        return Response(serializer.data)



