#vickyok
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
from django.contrib import messages
from django.core.mail import send_mail
import logging                                   #hivicky
logging.basicConfig(level=logging.DEBUG)
logging.debug('this is a debug meesage')

from event.models import vic_event,vic_register



















from django.core.mail import EmailMessage
from django.shortcuts import redirect
from PIL import Image, ImageDraw, ImageFont
import io

def utkarsh(request):
    if request.method == 'GET':
        # Get data from URL parameters
        name = request.GET.get('name')
        email = request.GET.get('email')

        # Text to display
        contact_details = [
            f"Name: {name}",
            f"Email: {email}"
        ]

        # Image settings
        image_width = 600
        background_color = (240, 248, 255)  # Light blue background
        text_color = (25, 25, 112)  # Dark blue text
        border_color = (176, 224, 230)  # Light turquoise border
        border_thickness = 10

        # Load font
        try:
            font = ImageFont.truetype("arial.ttf", 22)
        except IOError:
            font = ImageFont.load_default()

        # Calculate image height
        line_height = font.getsize('A')[1] + 10
        total_text_height = line_height * len(contact_details) + 2 * 40
        image_height = total_text_height + 2 * border_thickness
        image = Image.new('RGB', (image_width, image_height), background_color)
        draw = ImageDraw.Draw(image)

        # Draw border
        draw.rectangle(
            [(border_thickness, border_thickness), (image_width - border_thickness, image_height - border_thickness)],
            outline=border_color,
            width=border_thickness
        )

        # Draw each line of contact details
        text_y = border_thickness + 40
        for line in contact_details:
            text_width, _ = draw.textsize(line, font=font)
            text_x = (image_width - text_width) // 2
            draw.text((text_x, text_y), line, fill=text_color, font=font)
            text_y += line_height

        # Save the image to a BytesIO stream
        image_io = io.BytesIO()
        image.save(image_io, format="PNG")
        image_io.seek(0)

        # Email with the image attachment
        email_message = EmailMessage(
            'Enquiry Details',  # Subject
            'Please find the contact enquiry details attached as an image.',  # Message body
            'vg314671@gmail.com',  # From email
            ['vg314670@gmail.com'],  # To email (admin)
        )
        email_message.attach('contact_details.png', image_io.getvalue(), 'image/png')
        email_message.send(fail_silently=False)

        utkarsh1(request)
        return HttpResponseRedirect("/contact/")












def utkarsh1(request):
    name = request.GET.get('name')
    email = request.GET.get('email')

    # Message content
    intro_line = f"Dear {name},"
    message_content = [
        "Thank you for reaching out to us!",
        "We appreciate your interest in our event management services.",
        "Our team will review your enquiry and reach out shortly."
    ]
    
    closing_lines = [
        "Warm Regards,",
        "Vicky Event Planner"
    ]

    # Image settings
    image_width = 700
    background_color = (250, 250, 240)  # Light beige background
    text_color = (0, 0, 128)  # Navy blue text
    border_color = (210, 180, 140)  # Tan border
    border_thickness = 12

    # Font settings
    try:
        font = ImageFont.truetype("arial.ttf", 20)
        footer_font = ImageFont.truetype("arial.ttf", 18)
    except IOError:
        font = ImageFont.load_default()
        footer_font = font

    # Calculate height needed for the image
    line_height = font.getsize('A')[1] + 10
    padding = 40
    total_text_height = line_height * (1 + len(message_content) + len(closing_lines)) + padding * 2
    image_height = total_text_height + 2 * border_thickness

    # Create the image canvas
    image = Image.new('RGB', (image_width, image_height), background_color)
    draw = ImageDraw.Draw(image)

    # Draw the border
    draw.rectangle(
        [(border_thickness, border_thickness), (image_width - border_thickness, image_height - border_thickness)],
        outline=border_color,
        width=border_thickness
    )

    # Draw the intro line, left-aligned
    text_y = border_thickness + padding
    draw.text((border_thickness + padding, text_y), intro_line, fill=text_color, font=font)
    text_y += line_height  # Only one line-height space after "Dear {name}"

    # Draw each line of the main message, left-aligned
    for line in message_content:
        draw.text((border_thickness + padding, text_y), line, fill=text_color, font=font)
        text_y += line_height

    # Draw the closing lines, left-aligned, within the border
    text_y += line_height  # Add a line-height space before closing lines
    for line in closing_lines:
        draw.text((border_thickness + padding, text_y), line, fill=text_color, font=footer_font)
        text_y += line_height

    # Save image to BytesIO for email attachment
    image_io = io.BytesIO()
    image.save(image_io, format="PNG")
    image_io.seek(0)

    # Send thank-you email with the attached image
    email_message = EmailMessage(
        'Thank You for Your Enquiry!',
        'Thank you for reaching out to us. Please find the details attached as an image.',
        'vg314671@gmail.com',
        [email],
    )
    email_message.attach('thank_you.png', image_io.getvalue(), 'image/png')
    email_message.send(fail_silently=False)

    messages.success(request, 'Thank you, your enquiry has been created successfully!')
    return HttpResponseRedirect("/contact/")




























#for event
from django.core.mail import EmailMessage
from django.shortcuts import redirect
from PIL import Image, ImageDraw, ImageFont
import io

def prince(request):
    if request.method == 'GET':
        # Get data from URL parameters
        your_name = request.GET.get('your_name')
        event_name = request.GET.get('event_name')
        event_date = request.GET.get('event_date')
        event_mail = request.GET.get('event_mail')
        event_city = request.GET.get('event_city')
        event_description = request.GET.get('event_description')
        event_category = request.GET.get('event_category')
        guests = request.GET.get('guests')

        # Format text for the image
        event_details = [
            f"Event Name: {event_name}",
            f"Event Date: {event_date}",
            f"Event Email: {event_mail}",
            f"Event City: {event_city}",
            f"Event Description: {event_description}",
            f"Event Category: {event_category}",
            f"Guests: {guests}"
        ]
        footer_text = "Warm Regards,\nVicky Event Planner"

        # Image settings
        image_width = 800
        background_color = (255, 248, 240)  # Light cream background
        text_color = (0, 51, 102)  # Dark blue text for the main content
        footer_color = (51, 51, 51)  # Dark gray for footer text
        border_color = (255, 204, 153)  # Light orange border
        border_thickness = 12

        # Initialize font
        try:
            font = ImageFont.truetype("arial.ttf", 20)
            footer_font = ImageFont.truetype("arial.ttf", 16)
        except IOError:
            font = ImageFont.load_default()
            footer_font = font

        # Calculate heights based on individual lines
        line_height = font.getsize('A')[1] + 10  # Adding extra space between lines
        main_text_height = line_height * len(event_details)
        footer_height = line_height * 3  # Footer section height
        total_text_height = main_text_height + footer_height + 2 * 40  # Add top and bottom padding

        # Adjust image height based on total text height
        image_height = total_text_height + 2 * border_thickness
        image = Image.new('RGB', (image_width, image_height), background_color)
        draw = ImageDraw.Draw(image)

        # Draw the border
        draw.rectangle(
            [(border_thickness, border_thickness), (image_width - border_thickness, image_height - border_thickness)],
            outline=border_color,
            width=border_thickness
        )

        # Draw each line of event details, center-aligned
        text_y = border_thickness + 40  # Starting Y position with padding
        for line in event_details:
            text_width, _ = draw.textsize(line, font=font)
            text_x = (image_width - text_width) // 2
            draw.text((text_x, text_y), line, fill=text_color, font=font)
            text_y += line_height

        # Draw "Thank you..." section at the bottom, centered
        footer_y = text_y + 40  # 40 px gap before footer
        for line in footer_text.splitlines():
            footer_x = (image_width - draw.textsize(line, font=footer_font)[0]) // 2
            draw.text((footer_x, footer_y), line, fill=footer_color, font=footer_font)
            footer_y += line_height

        # Save the image to a BytesIO stream
        image_io = io.BytesIO()
        image.save(image_io, format="PNG")
        image_io.seek(0)  # Move to the beginning of the BytesIO stream

        # Prepare email with the event details image attached
        email = EmailMessage(
            'Event Details',  # Subject
            'Please find your event details attached as an image.',  # Message body
            'vg314671@gmail.com',  # From email
            ['vg314670@gmail.com'],  # To email (admin)
        )

        # Attach the image
        email.attach('event_details.png', image_io.getvalue(), 'image/png')

        # Send the email
        email.send(fail_silently=False)
        vicky1(request)
        # Redirect to payment page
        return redirect('/payment/')


    




from django.core.mail import EmailMessage
from django.shortcuts import redirect
from PIL import Image, ImageDraw, ImageFont
import io
from django.contrib import messages
from django.http import HttpResponseRedirect
import textwrap

def vicky1(request):
    # Get data from request
    your_name = request.GET.get('your_name')
    event_name = request.GET.get('event_name')
    event_date = request.GET.get('event_date')
    event_mail = request.GET.get('event_mail')

    # Format text for the thank-you message
    dear_text = f"Dear {your_name},"
    main_message = f'''
    We are thrilled to extend our heartfelt thanks to you for your valuable participation in {event_name} held on {event_date}. Your presence and active engagement were pivotal to making this event a grand success.

    The insights shared, the connections made, and the enthusiasm displayed truly exemplified the spirit of collaboration we aimed to foster. We are grateful for the opportunity to have hosted such an inspiring event.

    A special thank you to our speakers, sponsors, and volunteers. Your contributions were instrumental in creating an unforgettable experience.

    We look forward to your continued support in future events.
    '''
    regards_text = "Warm Regards,\nVicky Event Planner"

    # Image settings
    image_width = 800
    background_color = (255, 248, 240)  # Light cream background
    text_color = (0, 51, 102)  # Dark blue text
    border_color = (255, 204, 153)  # Light orange border
    border_thickness = 10

    # Initialize font
    try:
        font = ImageFont.truetype("arial.ttf", 18)
    except IOError:
        font = ImageFont.load_default()

    # Wrap the main message to fit within the image width
    max_text_width = image_width - 2 * (border_thickness + 40)  # Account for padding and border
    wrapped_main_message = textwrap.wrap(main_message, width=50)  # Adjust width as necessary

    # Calculate text heights for each section
    line_height = font.getsize('A')[1] + 10  # Adding extra space between lines
    dear_height = line_height
    main_text_height = line_height * len(wrapped_main_message)
    regards_height = line_height * 2  # Add extra spacing for "Warm Regards" section
    total_text_height = dear_height + main_text_height + regards_height + 2 * 40  # Top and bottom padding

    # Adjust image height based on total text height
    image_height = total_text_height + 2 * border_thickness
    image = Image.new('RGB', (image_width, image_height), background_color)
    draw = ImageDraw.Draw(image)

    # Draw the border
    draw.rectangle(
        [(border_thickness, border_thickness), (image_width - border_thickness, image_height - border_thickness)],
        outline=border_color,
        width=border_thickness
    )

    # Draw "Dear [name]" at the top, centered
    dear_x = (image_width - draw.textsize(dear_text, font=font)[0]) // 2
    dear_y = border_thickness + 20
    draw.text((dear_x, dear_y), dear_text, fill=text_color, font=font)

    # Draw main message, center-aligned under "Dear [name]"
    text_y = dear_y + dear_height + 20  # 20 px gap between "Dear" and main text
    for line in wrapped_main_message:
        text_width, _ = draw.textsize(line, font=font)
        text_x = (image_width - text_width) // 2
        draw.text((text_x, text_y), line, fill=text_color, font=font)
        text_y += line_height

    # Draw "Warm Regards" section at the bottom, centered
    regards_x = (image_width - draw.textsize(regards_text, font=font)[0]) // 2
    regards_y = text_y + 40  # 40 px gap before "Warm Regards"
    for line in regards_text.splitlines():
        draw.text((regards_x, regards_y), line, fill=text_color, font=font)
        regards_y += line_height

    # Save the image to a BytesIO stream
    image_io = io.BytesIO()
    image.save(image_io, format="PNG")
    image_io.seek(0)  # Move to the beginning of the BytesIO stream

    # Prepare email with the thank-you image attached
    email = EmailMessage(
        'Thank You for Your Participation!',  # Subject
        'Please find a thank-you message attached as an image.',  # Message body
        'vg314671@gmail.com',  # From email
        [event_mail],  # To email (customer's email)
    )

    # Attach the image
    email.attach('thank_you_message.png', image_io.getvalue(), 'image/png')

    # Send the email
    email.send(fail_silently=False)

    # Send a success message to the user
    messages.success(request, 'Thank you! Your event has been created successfully. Now please proceed with the advance payment.')

    return HttpResponseRedirect("/event/")

    

    

#for update
def mehndi(request):
    if request.method == 'GET':
        print('vikcy')
        # Get data from URL parameters
        your_name=request.GET.get('your_name')
        event_name = request.GET.get('event_name')
        event_date = request.GET.get('event_date')
       
        event_mail = request.GET.get('event_mail')
      
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
















































from django.shortcuts import render, redirect
from django.contrib import messages


def event(request):
    data = {}
    vrg = vic_event.objects.all()

    if request.method == 'POST':
        your_namee = request.POST.get('your_name')
        event_namee = request.POST.get('event-name')
        event_datee = request.POST.get('event-date')
        event_maill = request.POST.get('mail')
        event_cityy = request.POST.get('state')  # Changed to match HTML
        event_dess = request.POST.get('event-description')
        guestss = request.POST.get('guests')
        event_categoryy = request.POST.get('event-category')

        # Validate if all fields are filled
        if not all([your_namee, event_namee, event_datee, event_maill, event_cityy, event_dess, guestss, event_categoryy]):
            messages.info(request, 'All fields are required.')
            return redirect('/event')

        # Check for date availability
        if vic_event.objects.filter(event_date=event_datee).exists():
            messages.info(request, 'This day is already booked.')
            return redirect('/event')

        # Create the event if validations pass
        vic_event.objects.create(
            your_name=your_namee,
            event_name=event_namee,
            event_date=event_datee,
            event_description=event_dess,
            event_category=event_categoryy,
            guests=guestss,
            email=event_maill,
            city=event_cityy,
        )

        return HttpResponseRedirect('/prince/?your_name={}&event_name={}&event_date={}&event_description={}&event_category={}&guests={}&event_mail={}&event_city={}'.format(
        your_namee,event_namee, event_datee, event_dess, event_categoryy, guestss,event_maill,event_cityy,your_namee))

    

    data = {'vrg': vrg}
    return render(request, "event.html", data)

    

        





















import razorpay
from django.shortcuts import render, redirect
from django.conf import settings
from payment.models import vic_payment

def payment(request):
    data = {}
    
    if request.method == "POST":
        try:
            # Get the amount from the form and convert to paise (smallest currency unit for Razorpay)
            amount = int(request.POST.get("amount")) * 100  
            
            # Print amount to check if it's received correctly
            print(f"Amount (in paise): {amount}")
            
            # Initialize Razorpay client with your keys
            client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
            
            # Create an order with Razorpay
            payment = client.order.create({
                'amount': amount,
                'currency': 'INR',
                'payment_capture': '1'  # Auto capture payment
            })
            
            # Print payment details to verify they are correct
            print(f"Payment details: {payment}")
            
            # Store payment details in the database
            event = vic_payment(amount=str(amount), payment_id=payment['id'])  # Cast amount to string
            event.save()  # Save the event object to the database
            
            # Check if payment was saved successfully
            print(f"Payment saved in DB with ID: {event.id}")
            
            # Pass the payment object to the template (for Razorpay's frontend integration)
            data['payment'] = payment
            
            # Redirect to the success page or handle further payment processing as needed
            return redirect('/success/')
        
        except Exception as e:
            # Print any errors during the process
            print(f"Error: {e}")
            return redirect('/event')  # Handle errors better if needed

    # Render the template for a GET request without a 'payment' key
    return render(request, "payment.html", data)







def success(request):
   
     return render(request,"success.html")     









































































































































































































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
            
            event_cityy= request.POST.get('city')
            
            event_dess = request.POST.get('event-description')
            guestss = request.POST.get('guests')
            event_categoryy = request.POST.get('event-category')

            if not all([event_namee, event_datee, event_dess, guestss, event_categoryy,event_maill,event_cityy,your_namee]):
                messages.info(request, 'All fields are required')
                return redirect('/event')
            


            
            
            vic_event.objects.update(
                event_name=event_namee,
                event_date=event_datee,
              
                event_description=event_dess,
                event_category=event_categoryy,
                guests=guestss, email=event_maill,
             
                city=event_cityy,
                your_name=your_namee
            )
            
            return HttpResponseRedirect('/mehndi/?event_name={}&event_date={}&event_description={}&event_category={}&guests={}&event_mail={}&event_city={}&your_name{}'.format(
                event_namee, event_datee,  event_dess, event_categoryy, guestss,event_maill,event_cityy,your_namee))

            
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

