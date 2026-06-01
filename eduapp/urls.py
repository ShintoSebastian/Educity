from django.urls import path 
from . import views
from django.contrib.auth.views import LoginView,LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # USER SIDE
    path('', views.index, name="index"),
    path('register', views.register, name="register"),
    path('login', views.login, name="login"),
    path('logout', views.logout, name='logout'),
    path('search_event', views.search_event, name='search_event'),
    path('search_class', views.search_class, name='search_class'),
    path('search_venue', views.search_venue, name='search_venue'),
    path('search_all', views.search_all, name='search_all'),
    # path('search/',views.search_view,name='search'),

    #ADMIN URLS
    path('adminlogin', LoginView.as_view(template_name='admin/adminlogin.html'),name='adminlogin'),
    path('admin-dashboard', views.admin_dashboard_view,name='admin-dashboard'),
    
    #activity 
    path('add_activity',views.add_activity,name='add_activity'),
    path('edit_activity/<int:id>',views.edit_activity,name='edit_activity'),
    path('delete_activity/<int:id>',views.delete_activity,name='delete_activity'),
    
    path('select_activity/',views.select_activity,name='select_activity'),
    path('activitys/',views.activitys,name='activitys'),
    
    #activitys
    path('add_event/',views.event_view,name='add_event'),
    path('add_class/',views.class_view,name='add_class'),
    path('add_venue/',views.venue_view,name='add_venue'),

    path('one',views.one, name='one'),

]
urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)