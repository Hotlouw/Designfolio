from django.urls import path
from . import views
from .views import login_view,create_blog,create_certification,create_other,create_project,email_list, businesscard_view, dataentry_view, certification_list,other_list, index_view, intro_view, other_view, project_list,create_email,blog_list,services_view,training_view
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
     
    path('projects/', project_list, name='project_list'),
    path('email/',email_list, name='email_list'),
    path('create_mail', create_email, name='create_email'),
    path('blog/', blog_list, name='blog_list'),
    path('certifications/',certification_list, name = "certification_list"),
    
    path('login/', login_view, name='login'),
    
    
    path('index/', index_view, name='index_view'),
    path('intro/', intro_view, name='intro_view'),
    path('other/', other_list, name='other_list'),
    path('services/', services_view, name ='services_view'),
    path('training/', training_view, name = 'training_view'),
    path('businesscard/', businesscard_view, name ='businesscard_view'),
    path('login/dataentry/', dataentry_view, name='dataentry_view'),

    path('create_project/', create_project, name='create_project'),
    path('create_certification/', create_certification, name='create_certification'),
    path('create_other/', create_other, name='create_other'),
    path('create_blog/', create_blog, name='create_blog'),
    

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
