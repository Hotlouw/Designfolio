from django.shortcuts import render
from django.http import HttpResponse
from .models import Certification, Projects, Email, Blog, Library, Other, OtherLibrary
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from .forms import EmailForm, ProjectsForm, OtherForm, CertificationForm, BlogForm
from django.core.mail import send_mail
from django.contrib.auth.views import LoginView
from .forms import LoginForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

#DATABASE SITES
#def project_list(request):
#    projects = Projects.objects.all()
#    return render(request, 'projects.html', {'projects': projects})


@login_required
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('dataentry/')
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})

@login_required
def data_entry(request):
    return render(request, 'dataentry.html')

def certification_list(request,):
    certifications = Certification.objects.all     
    return render(request, 'certifications.html', {'certifications': certifications})

@login_required
def create_certification(request):
    if request.method == 'POST':
        form = CertificationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("You have melded the certification")  # Redirect to a success page after form submission
    else:
        form = CertificationForm()

    return render(request, 'create_certification.html', {'form': form})

def email_list(request):
    emails = Email.objects.all()
    return render(request, 'email.html', {'email': emails})


def create_email(request):
    form = EmailForm(request.POST)
    if form.is_valid():
        form.save()
        email_instance = form.save()
        # Send an email
        send_mail(
                from_email=email_instance.sender,
                subject=email_instance.subject,
                message=email_instance.message,
                recipient_list=['johanwlouw@gmail.com'],  # Replace with your email address
                fail_silently=False,)
        return JsonResponse({'status': 'success'})
    else:
        # Return errors as JSON if needed
        return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)


def blog_list(request):
    libraries = Library.objects.all()

    if request.method == 'POST':
        selected_library_id = request.POST.get('library', None)
        if selected_library_id:
            selected_library = Library.objects.get(pk=selected_library_id)
            blogs = Blog.objects.filter(category=selected_library)
            return render(request, 'blog.html', {'libraries': libraries, 'selected_library': selected_library, 'blogs': blogs})

    return render(request, 'blog.html', {'libraries': libraries})

@login_required
def create_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("You have melded the blog")  # Redirect to a success page after form submission
    else:
        form = BlogForm()

    return render(request, 'create_blog.html', {'form': form})

def project_list(request):
    libraries = Library.objects.all()

    if request.method == 'POST':
        selected_library_id = request.POST.get('library', None)
        if selected_library_id:
            selected_library = Library.objects.get(pk=selected_library_id)
            projects = Projects.objects.filter(category=selected_library)
            return render(request, 'projects.html', {'libraries': libraries, 'selected_library': selected_library, 'projects': projects})

    return render(request, 'projects.html', {'libraries': libraries})

@login_required
def create_project(request):
    if request.method == 'POST':
        form = ProjectsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("You have melded the project")  # Redirect to a success page after form submission
    else:
        form = ProjectsForm()

    return render(request, 'create_project.html', {'form': form})

def other_list(request):
    libraries = OtherLibrary.objects.all()

    if request.method == 'POST':
        selected_library_id = request.POST.get('library', None)
        if selected_library_id:
            selected_library = OtherLibrary.objects.get(pk=selected_library_id)
            others = Other.objects.filter(category=selected_library)
            return render(request, 'other.html', {'libraries': libraries, 'selected_library': selected_library, 'others': others})

    return render(request, 'other.html', {'libraries': libraries})

@login_required
def create_other(request):
    if request.method == 'POST':
        form = OtherForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("You have melded the ... other ... thing... ?")  # Redirect to a success page after form submission
    else:
        form = OtherForm()

    return render(request, 'create_other.html', {'form': form})
#STATIC SITES
def index_view(request):
    return render(request, 'index.html')

def intro_view(request):
    return render(request, 'intro.html')

def other_view(request):
    return render(request, 'other.html')

def services_view(request):
    return render(request,'services.html')

def training_view(request):
    return(render(request,'training.html'))

def businesscard_view(request):
    return(render(request,'bc.html'))

def dataentry_view(request):
    return(render(request,'dataentry.html'))