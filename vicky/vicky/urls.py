
from django.contrib import admin
from django.urls import path
from vicky import views



from django.conf import settings
from django.conf.urls.static import static
from django.urls import path


from .views import logout_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),

    path('event/',views.event,name='event'),
    path('prince/',views.prince,name='prince'),
    path('mehndi/',views.mehndi,name='mehndi'),
  
    
    path('vacant/',views.vacant,name='vacant'),
   
    path('delete_event/<int:id>/', views.delete_event, name='delete_event'),
    path('update_event/<int:id>/', views.update_event, name='update_event'),


    
   
    path('register/',views.register,name='register'),

    path('login/',views.login,name='login'),




    path('logout/', logout_view, name='logout'),




   
     

    


]



#for media image ke liye Your urlpatterns here...

from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

