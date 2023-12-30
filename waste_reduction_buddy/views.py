from django.db import IntegrityError
from django.shortcuts import render, redirect,  get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddStaffRecord, AppointmentRecord
from .models import Record, Appointment


def home(request):
    records = Record.objects.all()
    appointments = Appointment.objects.all()
    email_domain = request.session.get('email_domain', None)
    form = AppointmentRecord(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            appointment_register = form.save()
            messages.success(request, "Booking Completed...")
            return redirect('home')
        
    return render(request, 'home.html', {'records': records ,'appointments': appointments,'email_domain': email_domain,'form':form})
    

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
    email_domain = request.session.get('email_domain', None)
    if request.user.is_authenticated and email_domain == 'admin.com':
        staff_record =Record.objects.get(id = pk)
        return render(request, 'record.html', {'staff_record':staff_record},)
    else:
        messages.error(request, "You must be Admin to update.")
        return redirect('home')

def delete_staff_record(request, pk):
    email_domain = request.session.get('email_domain', None)
    if request.user.is_authenticated and email_domain == 'admin.com':
        delete_record = Record.objects.get(id=pk)
        delete_record.delete()
        messages.success(request, "Record Deleted Successfully...")
        return redirect('home')
    else:
        messages.error(request, "You Must Be Logged In To Delete Record...")
        return redirect('home')


def add_staff_record(request):
    email_domain = request.session.get('email_domain', None)
    form = AddStaffRecord(request.POST or None)
    if request.user.is_authenticated and email_domain == 'admin.com':
        if request.method == "POST":
            if form.is_valid():
                add_staff_record = form.save()
                messages.success(request, "Record Added...")
                return redirect('home')
        return render(request, 'add_staff_record.html', {'form':form})
    else:
        messages.error(request, "You Must Be Logged In...")
        return redirect('home')




def update_staff_record(request, pk):
    email_domain = request.session.get('email_domain', None)
    if request.user.is_authenticated and email_domain == 'admin.com':
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
    email_domain = request.session.get('email_domain', None)
    if request.user.is_authenticated and email_domain == 'admin.com':
        appointment_record =Appointment.objects.get(id = pk)
        return render(request, 'appointment.html', {'appointment_record':appointment_record},)
    else:
        messages.error(request, "You must be Admin to update.")
        return redirect('home')


def delete_appointment_record(request, pk):
    email_domain = request.session.get('email_domain', None)
    if request.user.is_authenticated and email_domain == 'admin.com':
        delete_record = Appointment.objects.get(id=pk)
        delete_record.delete()
        messages.success(request, "Record Deleted Successfully...")
        return redirect('home')
    else:
        messages.error(request, "You Must Be Logged In To Delete Record...")
        return redirect('home')

def appointment_register(request):
    form = AppointmentRecord(request.POST or None)
    
    if request.method == "POST":
        if form.is_valid():
            appointment_instance = form.save(commit=False)

            # Check if the user is authenticated
            if request.user.is_authenticated:
                # If authenticated, associate the form with the logged-in user
                appointment_instance.Created_By = request.user

            appointment_instance.save()
            messages.success(request, "Booking Completed...")
            return redirect('home')

    messages.error(request, "Booking was incomplete. Please try again later...")
    return redirect('home')
    
    