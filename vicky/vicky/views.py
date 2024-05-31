#vickyok
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
from django.contrib import messages
from django.core.mail import send_mail
import logging                                   #hivicky
logging.basicConfig(level=logging.DEBUG)
logging.debug('this is a debug meesage')

from event.models import vic_event,vic_register

def utkarsh(request):
    if request.method == 'GET':
        # Get data from URL parameters
        name=request.GET.get('name')
        email = request.GET.get('email')

        email_content = f'''
        name:  {name}
        Email: {email}
        '''
        send_mail(
             'Enquiry details',#subejct heading
             email_content,#show message in mail
             'vg314671@gmail.com',#from
             ['vg314670@gmail.com'],#where
             fail_silently=False
         )
        utkarsh1(request)#it is fucntion 
        return HttpResponseRedirect("/contact/")
        
def utkarsh1(request):
    event_messsage = f'''
        Dear {request.GET.get('name')},

I hope this message finds you well.

I am writing to inquire about your event management services. My organization, is planning an event and we are seeking professional assistance to ensure its success.'''
      
    send_mail(
        'Thank you for your enquiryy!',#subject
         event_messsage,#message show hoga
        'vg314671@gmail.com',  # from
        [request.GET.get('email')],  # recipient_list should be a list
        fail_silently=False
    )

    messages.success(request, 'Thank you, your enquiry has been created successfully!')
    return HttpResponseRedirect("/contact/")
    
def prince(request):
    if request.method == 'GET':
        # Get data from URL parameters
        your_name=request.GET.get('your_name')
        event_name = request.GET.get('event_name')
        event_date = request.GET.get('event_date')
      
        event_mail = request.GET.get('event_mail')
        event_state = request.GET.get('event_state')
        event_city = request.GET.get('event_city')
        event_description = request.GET.get('event_description')
        event_category = request.GET.get('event_category')
        guests = request.GET.get('guests')

        # Format email content
        email_content = f'''
        Your name:  {your_name}
        Event Name: {event_name}
        Event Date: {event_date}
       
        Event mail: {event_mail}
        Event state: {event_state}
        Event city: {event_city}
        
        Event Description: {event_description}
        Event Category: {event_category}
        Guests: {guests}
        '''

        # Send email it is build in function
        send_mail(
             'Event details',#subejct heading
             email_content,#show message in mail
             'vg314671@gmail.com',#from
             ['vg314670@gmail.com'],#where
             fail_silently=False
         )
        vicky1(request)#it is fucntion 
        return HttpResponseRedirect("/event/")
    
def vicky1(request):
    event_messsage = f'''
        Dear {request.GET.get('your_name')},

        We are thrilled to extend our heartfelt thanks to you for your valuable participation in {request.GET.get('event_name')} held on {request.GET.get('event_date')}. Your presence and active engagement were pivotal to making this event a grand success.

        The insights shared, the connections made, and the enthusiasm displayed by all attendees truly exemplified the spirit of collaboration and learning that we aimed to foster. We are grateful for the opportunity to have hosted such an inspiring and impactful event.

        A special thank you to our speakers, sponsors, and volunteers for their dedication and hard work. Your contributions were instrumental in creating an unforgettable experience for everyone involved.

        We look forward to your continued support and participation in future events. Together, we can achieve even greater milestones.
        '''
    send_mail(
        'Thank you for your event submission!',#subject
         event_messsage,#message show hoga
        'vg314671@gmail.com',  # from
        [request.GET.get('event_mail')],  # recipient_list should be a list
        fail_silently=False
    )

    messages.success(request, 'Thank you, your event has been created successfully!')
    return HttpResponseRedirect("/event/")

    

    


def mehndi(request):
    if request.method == 'GET':
        print('vikcy')
        # Get data from URL parameters
        your_name=request.GET.get('your_name')
        event_name = request.GET.get('event_name')
        event_date = request.GET.get('event_date')
       
        event_mail = request.GET.get('event_mail')
        event_state = request.GET.get('event_state')
        event_city = request.GET.get('event_city')
        
        event_description = request.GET.get('event_description')
        event_category = request.GET.get('event_category')
        guests = request.GET.get('guests')

        # Format email content
        email_content = f'''
        Your name:  {your_name}
        Event Name: {event_name}
        Event Date: {event_date}
    
        Event mail: {event_mail}
        Event state: {event_state}
        Event city: {event_city}
        
        Event Description: {event_description}
        Event Category: {event_category}
        Guests: {guests}
        '''

        # Send email
        send_mail(
             'updated Event details',#subejct heading

              email_content,#show message in mail

             'vg314671@gmail.com',
             ['vg314670@gmail.com'],
             fail_silently=False
         )
        vicky2(request)
        return render(request,"update.html")
     
def vicky2(request):
    send_mail(
        'Thank you for your event submission!',#subject
        'your event was updated',#message
        'vg314671@gmail.com',  # from
        [request.GET.get('event_mail')],  # recipient_list should be a list
        fail_silently=False
    )

    messages.success(request, 'Thank you, your event has been updated successfully!')
    

    

def event(request):
    data={}
    vrg=vic_event.objects.all()
    if request.method == 'POST':
        try:
            data={'vrg':vrg}
            your_namee=request.POST.get('your_name')
            event_namee = request.POST.get('event-name')
            event_datee = request.POST.get('event-date')
           
            event_maill = request.POST.get('mail')
            event_statee = request.POST.get('state')
            event_cityy = request.POST.get('city')
          
            event_dess = request.POST.get('event-description')
            guestss = request.POST.get('guests')
            event_categoryy = request.POST.get('event-category')

            if not all([event_namee, event_datee,event_maill,event_statee,event_cityy, event_dess, guestss, event_categoryy,your_namee]):
                messages.info(request, 'All fields are required')
                return redirect('/event')

            if vic_event.objects.filter(event_date=event_datee):
               if vic_event.objects.filter(event_date=event_datee).exists():
                   messages.info(request,'this day was already booked')
                   return redirect('/event')
               
            #if vic_event.objects.filter(email=event_maill):   
                   messages.info(request,'email was already taken')
                   return redirect('/event')

            
            vic_event.objects.create(
                event_name=event_namee,
                event_date=event_datee,
            
                
                event_description=event_dess,
                event_category=event_categoryy,
                guests=guestss,
                email=event_maill,
                state=event_statee,
                city=event_cityy,
                your_name=your_namee,

            )
            #return HttpResponseRedirect('/growbiz')
           
            return HttpResponseRedirect('/prince/?your_name={}&event_name={}&event_date={}&event_description={}&event_category={}&guests={}&event_mail={}&event_state={}&event_city={}'.format(
                your_namee,event_namee, event_datee, event_dess, event_categoryy, guestss,event_maill,event_statee,event_cityy,your_namee))

        except Exception as e:
            print(e)  
            pass

    return render(request, "event.html",data)



def vacant(request):
     eventdata=vic_event.objects.all()
     data={'eventdata':eventdata}
     return render(request,"vacant.html",data)



def delete_event(request,id):
     eventdata=vic_event.objects.get(id=id)
     eventdata.delete()
     return HttpResponseRedirect("/vacant/")

def update_event(request,id):
    data={}
    eventdata=vic_event.objects.get(id=id)
    data={'event':eventdata}
    if request.method == 'POST':
        try:
            print('vicky update')
            your_namee=request.POST.get('your_name')
            event_namee = request.POST.get('event-name')
            event_datee = request.POST.get('event-date')
          
            event_maill = request.POST.get('mail')
            event_statee = request.POST.get('state')
            event_cityy= request.POST.get('city')
            
            event_dess = request.POST.get('event-description')
            guestss = request.POST.get('guests')
            event_categoryy = request.POST.get('event-category')

            if not all([event_namee, event_datee, event_dess, guestss, event_categoryy,event_maill,event_statee,event_cityy,your_namee]):
                messages.info(request, 'All fields are required')
                return redirect('/event')
            


            
            
            vic_event.objects.update(
                event_name=event_namee,
                event_date=event_datee,
              
                event_description=event_dess,
                event_category=event_categoryy,
                guests=guestss, email=event_maill,
                state=event_statee,
                city=event_cityy,
                your_name=your_namee
            )
            
            return HttpResponseRedirect('/mehndi/?event_name={}&event_date={}&event_description={}&event_category={}&guests={}&event_mail={}&event_state={}&event_city={}&your_name{}'.format(
                event_namee, event_datee,  event_dess, event_categoryy, guestss,event_maill,event_statee,event_cityy,your_namee))

            
        except Exception as e:
            print(e) 
            pass 
    return render(request,"update.html",data)
     
#front page
def home(request):
     
     return render(request,"home.html")
def front(request):
     
     return render(request,"front.html")









#signup
from django.contrib.auth.models import User
def register(request):
    if request.method == 'POST':
        # Retrieve form data
        first_namee = request.POST.get('first_name')
        last_namee = request.POST.get('last_name')
        usernamee = request.POST.get('username')
        password11 = request.POST.get('password1')
        password22 = request.POST.get('password2')

        # Check if all fields are filled
        if not all([first_namee, last_namee, usernamee, password11, password22]):
            messages.error(request, "All fields are required.")
            return HttpResponseRedirect('/register')

        # Check if passwords match
        if password11 == password22:
            # Check if the username already exists
            if User.objects.filter(username=usernamee).exists():
                messages.error(request, 'Username already taken')
            else:
                # Create user
                user = User.objects.create_user(username=usernamee,
                                                password=password11,
                                                first_name=first_namee,
                                                last_name=last_namee)
                messages.success(request, 'Account created successfully')
        else:
            messages.error(request, 'Passwords do not match')

        # Redirect to the registration page
        return HttpResponseRedirect('/register')

    return render(request, "register.html")



#Login
from django.contrib.auth import authenticate, login
def login(request):
    if request.method == 'POST':
      
        usernamee = request.POST.get('username')
        passwordd = request.POST.get('password')

      
        if not all([usernamee,passwordd]):
                messages.info(request, 'All fields are required')
                return redirect('/login')
        # Authenticate user
        user = authenticate(username=usernamee, password=passwordd)
        if user:
        
            return HttpResponseRedirect('/event')  # Redirect to some page after successful login
        else:
            messages.error(request, 'Invalid username or password')

        return HttpResponseRedirect('/login')

    return render(request, "login.html")

#Logout
from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/login/')  # Redirect to the login page after logout



from event.models import vic_contact
def contact(request):

    if request.method == 'POST':
        try:    
            namee=request.POST.get('name')
            emaill = request.POST.get('email')
            
            if not all([namee,emaill]):
                messages.info(request, 'All fields are required')
                return redirect('/contact')
            
            vic_contact.objects.create(
                name=namee,
                email=emaill
               
            )
            return HttpResponseRedirect('/utkarsh/?name={}&email={}'.format(
                namee, emaill))
            
        except Exception as e:
            print(e) 
            pass 
    return render(request,"contact.html")

def about(request):
     
     return render(request,"about.html")
def ourwork(request):
     
     return render(request,"ourwork.html")



#services

def vendor(request):
     
     return render(request,"vendor.html")

def food(request):
     
     return render(request,"food.html")

def marriage(request):
     
     return render(request,"marriage.html")

def destination(request):
     
     return render(request,"destination.html")

def festival(request):
     
     return render(request,"festival.html")

def decor(request):
     
     return render(request,"decor.html")

def entertainment(request):
     
     return render(request,"entertainment.html")

def meeting(request):
     
     return render(request,"meeting.html")

