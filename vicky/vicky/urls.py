
from django.contrib import admin
from django.urls import path
from vicky import views



from django.conf import settings
from django.conf.urls.static import static
from django.urls import path


from .views import logout_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/',views.home,name='home'),
    path('',views.front),
    path('front/',views.front),

    path('event/',views.event,name='event'),
    path('prince/',views.prince,name='prince'),
    path('mehndi/',views.mehndi,name='mehndi'),
    path('utkarsh/',views.utkarsh,name='utkarsh'),
  
    
    path('vacant/',views.vacant,name='vacant'),
   
    path('delete_event/<int:id>/', views.delete_event, name='delete_event'),
    path('update_event/<int:id>/', views.update_event, name='update_event'),


    
   
    path('register/',views.register,name='register'),

    path('check_username/', views.check_username, name='check_username'),

    path('login/',views.login,name='login'),

    
    path('contact/',views.contact, name='contact'),


    path('logout/', logout_view, name='logout'),



    path('about/',views.about, name='about'),
    path('ourwork/',views.ourwork, name='ourwork'),
    #services we provide
    path('decor/',views.decor, name='decor'),
    path('food/',views.food, name='food'),
    path('destination/',views.destination, name='destination'),
    path('meeting/',views.meeting, name='meeting'),
    path('marriage/',views.marriage, name='marriage'),
    path('festival/',views.festival, name='festival'),
    path('vendor/',views.vendor, name='vendor'),
    path('entertainment/',views.entertainment, name='entertainment'),


    path('success/',views.success, name='success'),

    path('payment/',views.payment, name='payment'),

    path('adminlogin/',views.adminlogin, name='adminlogin'),

    path('adminlogout/', views.adminlogout, name='adminlogout'),

    path('showdetails/', views.showdetails, name='showdetails'),


    path('contactdetails/', views.contactdetails, name='contactdetails'),
    

    path('change_username_password/', views.change_username_password, name='change_username_password'),

    path('successful/',views.successful, name='successful'),













   
     

    


]



#for media image ke liye Your urlpatterns here...

from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

