from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="index"),
    path ('signup',views.signup, name='signup'),
    path ('login',views.login_request, name='login'),
    path('logout', views.logout_request, name="logout"),
    path('project/<int:project_id>', views.project, name='project'),

]
