from django.db import IntegrityError
from django.shortcuts import render, redirect,  get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddStaffRecord, AppointmentRecord, SelectedPersonUpdateForm, CompostInquiryForm,BlogPostForm
from .models import Record, Appointment, Compost_inquiry,BlogPost
from .faq_chatbot import FAQChatbot
from django.contrib.auth.models import User



def home(request):
    records = Record.objects.all()
    appointments = Appointment.objects.all()
    inquiries = Compost_inquiry.objects.all()
    email_domain = request.session.get('email_domain', None)
    email_user = request.session.get('email_user',None)
    form = AppointmentRecord(request.POST or None)


    if request.method == "POST":
        if form.is_valid():
            appointment_register = form.save()
            messages.success(request, "Booking Completed...")
            return redirect('home')

    
        
    return render(request, 'home.html', {'records': records ,'appointments': appointments,'inquiries': inquiries ,'email_domain': email_domain,'email_user': email_user,'form':form})


def faq_chatbot(request):
     # Check if the user is opening the panel for the first time
    if not request.session.get('has_visited_chatbot_panel', False):
        welcome_message = "Hello! I'm your WasteBuddy chatbot. Feel free to ask me any questions about WasteBuddy, like: 'What is WasteBuddy?' or 'How can I book an appointment?'"

        # Store the fact that the user has visited the chatbot panel
        request.session['has_visited_chatbot_panel'] = True

        return render(request, 'faq_chatbot.html', {'chatbot_response': welcome_message})

    # Get user's question from the form
    user_question = request.POST.get('user_question', '')

    # Get the previous question and answer (if available) from the session
    previous_question = request.session.get('previous_question', '')
    previous_answer = request.session.get('previous_answer', '')

    # Get chatbot response
    chatbot_response = FAQChatbot.get_answer(user_question)
    print(user_question)

    # Store the current question and chatbot response as the previous question and answer in the sesssion
    request.session['previous_question'] = user_question
    request.session['previous_answer'] = chatbot_response


    return render(request, 'faq_chatbot.html', {'chatbot_response': chatbot_response, 'previous_question': previous_question, 'previous_answer': previous_answer,'current_question': user_question,})

    

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_authenticated:
            login(request, user)
            messages.success(request, "You have been Logged in!!")
            email_domain = (username.split('@')[-1]).lower()
            request.session['email_domain'] = email_domain
            email_user = username.lower()
            request.session['email_user'] = email_user

            return redirect('home')
            #return render(request, 'home.html', {'email_domain': email_domain})
            
        else:
            messages.error(request, "Error logging in. Re-try again later...")
            return redirect('home')
    else:
        return render(request, 'login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, "You have been Logged out ...")
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                # Authentication
                email = form.cleaned_data['email']
                password = form.cleaned_data['password1']
                user = authenticate(request, username=email, password=password)
                messages.success(request, "You have successfully registered.")
                email_domain = (email.split('@')[-1]).lower()
                request.session['email_domain'] = email_domain
                return redirect('login_user')
            except IntegrityError:
                messages.error(request, "This email address is already in use. Please use a different email.")
    else:
        form = SignUpForm()

    return render(request, 'register.html', {'form':form})


def staff_record(request,pk):
    email_user = request.session.get('email_user', None)
    if request.user.is_authenticated and email_user == 'binod.raut@wastebuddy.com':
        staff_record =Record.objects.get(id = pk)
        return render(request, 'record.html', {'staff_record':staff_record},)
    else:
        messages.error(request, "You must be Admin to update.")
        return redirect('home')

def delete_staff_record(request, pk):
    email_user = request.session.get('email_user', None)
    if request.user.is_authenticated and email_user == 'binod.raut@wastebuddy.com':
        if request.method == 'POST':
            # Delete the record if the user confirmed
            delete_record = Record.objects.get(id=pk)
            delete_record.delete()
            messages.success(request, "Record Deleted Successfully...")
            return redirect('home')
        else:
            # Render a confirmation page if the request method is GET
            return render(request, 'delete_confirmation_record.html', {'record_id': pk})
    else:
        messages.error(request, "You Must Be Logged In To Delete Record...")
        return redirect('home')


def add_staff_record(request):
    if request.method == 'POST':
        form = AddStaffRecord(request.POST)
        if form.is_valid():
            # Create a new user
            user = User.objects.create_user(username=form.cleaned_data['email'], email=form.cleaned_data['email'], password=form.cleaned_data['password'])
            # Save the staff record
            staff_record = form.save(commit=False)
            staff_record.save()
            # Render the registration page again with an empty form
            form = AddStaffRecord()
            return render(request, 'add_staff_record.html', {'form': form, 'registration_success': True})
    else:
        form = AddStaffRecord()
    return render(request, 'add_staff_record.html', {'form': form})




def update_staff_record(request, pk):
    email_user = request.session.get('email_user', None)
    if request.user.is_authenticated and email_user == 'binod.raut@wastebuddy.com':
        current_record = get_object_or_404(Record, id=pk)
        form = AddStaffRecord(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request, "Record Updated...")
            return redirect('home')
        return render(request, 'update_staff_record.html', {'form': form})
    else:
        messages.error(request, "You Must Be Logged In...")
        return redirect('home')


def appointment_record(request,pk):
    email_user = request.session.get('email_user', None)
    if request.user.is_authenticated and email_user == 'binod.raut@wastebuddy.com':
        appointment_record =Appointment.objects.get(id = pk)
        return render(request, 'appointment.html', {'appointment_record':appointment_record},)
    else:
        messages.error(request, "You must be Admin to update.")
        return redirect('home')


def delete_appointment_record(request, pk):
    email_user = request.session.get('email_user', None)
    if request.user.is_authenticated and email_user == 'binod.raut@wastebuddy.com':
        if request.method == 'POST':
            delete_record = Appointment.objects.get(id=pk)
            delete_record.delete()
            messages.success(request, "Record Deleted Successfully...")
            return redirect('home')
        else:
            # Render a confirmation page if the request method is GET
            return render(request, 'delete_confirmation_appointment.html', {'record_id': pk})
    else:
        messages.error(request, "You Must Be Logged In To Delete Record...")
        return redirect('home')


def update_appointment_record(request, pk):
    email_user = request.session.get('email_user', None)
    if request.user.is_authenticated and email_user == 'binod.raut@wastebuddy.com':
        current_record = get_object_or_404(Appointment, id=pk)
        form = AppointmentRecord(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request, "Appointment Updated...")
            return redirect('home')
        return render(request, 'update_appointment_record.html', {'form': form})
    else:
        messages.error(request, "You Must Be Logged In...")
        return redirect('home')



def appointment_register(request):
    form = AppointmentRecord(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            appointment_instance = form.save(commit=False)            
            if request.user.is_authenticated:                
                appointment_instance.Created_By = request.user

            appointment_instance.save()
            messages.success(request, "Booking Completed...")
            return redirect('home')
        else:
            messages.error(request, "Booking was incomplete. Please try again ...")
    return render(request, 'bookappointment.html', {'form': form})
    
def update_selected_person(request, appointment_id):
    if request.method == 'POST':
        appointment_instance = get_object_or_404(Appointment, id=appointment_id)
        form = SelectedPersonUpdateForm(request.POST, instance=appointment_instance)
        
        if form.is_valid():
            form.save()
            messages.success(request, "Pickup man updated successfully.")
        else:
            messages.error(request, "Error updating selected person.")
        
        return redirect('home')
    else:
        messages.error(request, "Invalid request.")
        return redirect('home')



def compost_inquiry(request):
    form = CompostInquiryForm()
    if request.method == "POST":
        form = CompostInquiryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Compost Inquiry Added Successfully.")
            return redirect('home')
        else:
            messages.error(request, "Compost Inquiry was incomplete. Please enter valid information.")

    return render(request, 'compost_inquiry.html', {'form': form})


def compost_inquiry_record(request,pk):
    email_user = request.session.get('email_user', None)
    if request.user.is_authenticated and email_user == 'binod.raut@wastebuddy.com':
        compost_inquiry_record =Compost_inquiry.objects.get(id = pk)
        return render(request, 'compost_inquiry_record.html', {'compost_inquiry_record':compost_inquiry_record},)
    else:
        messages.error(request, "You must be Admin to update.")
        return redirect('home')

def update_compost_inquiry_record(request, pk):
    email_user = request.session.get('email_user', None)
    if request.user.is_authenticated and email_user == 'binod.raut@wastebuddy.com':
        current_record = get_object_or_404(Compost_inquiry, id=pk)
        form = CompostInquiryForm(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request, "Inquiry Updated...")
            return redirect('home')
        return render(request, 'update_compost_inquiry_record.html', {'form': form})
    else:
        messages.error(request, "You Must Be Logged In...")
        return redirect('home')

def delete_compost_inquiry_record(request, pk):
    email_user = request.session.get('email_user', None)
    if request.user.is_authenticated and email_user == 'binod.raut@wastebuddy.com':
        if request.method == 'POST':
            delete_record = Compost_inquiry.objects.get(id=pk)
            delete_record.delete()
            messages.success(request, "Inquiry Deleted Successfully...")
            return redirect('home')
        else:
            # Render a confirmation page if the request method is GET
            return render(request, 'delete_compost_inquiry_record.html', {'inquiries_id': pk})
    else:
        messages.error(request, "You Must Be Logged In To Delete Record...")
        return redirect('home')


def blog_show(request):
    email_user = request.session.get('email_user', None)
    posts = BlogPost.objects.all()
    return render(request, 'blog.html', {'posts': posts,'email_user': email_user})


def add_blog(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('blog_show')
    else:
        form = BlogPostForm()
    return render(request, 'add_blog.html', {'form': form})


def bookapt(request):
    form = AppointmentRecord(request.POST or None)
    return render(request, 'bookappointment.html',{'form': form})
