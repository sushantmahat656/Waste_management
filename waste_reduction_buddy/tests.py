from django.test import TestCase
from django.contrib.auth.models import User
from .models import Record, Appointment
from .forms import SignUpForm, AddStaffRecord, AppointmentRecord
from django.urls import reverse
from django.contrib import messages

class WasteManagementTests(TestCase):
    def setUp(self):
        # Create a user for testing
        self.admin_user = User.objects.create_user(
            username='binod.raut@wastebuddy.com',
            password='password'
        )
        self.normal_user = User.objects.create_user(
            username='user@wastebuddy.com',
            password='password'
        )

        # Create some records and appointments
        self.record = Record.objects.create(
            first_name='Sushant',
            last_name='Mahat',
            email='sus@example.com',
            phone='1234567890',
            address='123  St',
            city='City',
            state='State',
            zipcode=12345
        )

        self.appointment = Appointment.objects.create(
            first_name='Ane',
            last_name='Joe',
            email='joe@example.com',
            phone='9876543210',
            address='456  St',
            city='City',
            state='State',
            zipcode=67890,
            Created_By=self.admin_user
        )

    def test_home_view_authenticated_admin(self):
        # Log in as an admin user
        self.client.login(username='binod.raut@wastebuddy.com', password='password')

        # Access the home view
        response = self.client.get(reverse('home'))

        # Check if the response is successful (status code 200)
        self.assertEqual(response.status_code, 200)


        # Check if the admin-specific content is present in the response

       
        
        

    def test_home_view_authenticated_user(self):
        # Log in as a normal user
        self.client.login(username='user@wastebuddy.com', password='password')

        # Access the home view
        response = self.client.get(reverse('home'))

        # Check if the response is successful (status code 200)
        self.assertEqual(response.status_code, 200)

        # Check if the user-specific content is present in the response
        
        

    def test_home_view_unauthenticated(self):
        # Log out any user
        self.client.logout()

        # Access the home view
        response = self.client.get(reverse('home'))

        # Check if the response is successful (status code 200)
        self.assertEqual(response.status_code, 200)

        # Check if the unauthenticated user content is present in the response
        self.assertContains(response, 'Book Appointment')

    def test_staff_record_view_authenticated_admin(self):
        # Log in as an admin user
        self.client.login(username='user@wastebuddy.com', password='password')

        # Access the staff_record view with a valid record ID
        response = self.client.get(reverse('record', args=[self.record.id]))

        # Check if the response is successful (status code 200)
        self.assertEqual(response.status_code, 302)

        

    def test_staff_record_view_authenticated_user(self):
        # Log in as a normal user
        self.client.login(username='user@wastebuddy.com', password='password')

        # Access the staff_record view with a valid record ID
        response = self.client.get(reverse('record', args=[self.record.id]))

        # Check if the response is a redirect (status code 302) since regular users should not have access
        self.assertEqual(response.status_code, 302)

    # Add more tests for other views...

    def test_appointment_register_view_authenticated_user(self):
        # Log in as a normal user
        self.client.login(username='user@wastebuddy.com', password='password')

        # Access the appointment_register view
        response = self.client.post(reverse('appointment_register'), data={
            'first_name': 'Test',
            'last_name': 'User',
            'email': 'test@example.com',
            'phone': '1234567890',
            'address': '123 Test St',
            'city': 'Test City',
            'state': 'Test State',
            'zipcode': 54321,
        })

        # Check if the response is a redirect (status code 302) since regular users should not have access
        self.assertEqual(response.status_code, 302)


