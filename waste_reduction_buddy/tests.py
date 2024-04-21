from django.contrib import messages
from django.contrib.messages import get_messages
from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.sessions.middleware import SessionMiddleware
from django.contrib.messages.middleware import MessageMiddleware
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.test import Client
from .models import Record, Appointment, Compost_inquiry, BlogPost, Contact_Us, Product, Feedback
from .forms import SignUpForm, AddStaffRecord, UpdateStaffRecordForm, AppointmentRecord, SelectedPersonUpdateForm, CompostInquiryForm, BlogPostForm, ContactForm, ProductForm, FeedbackForm
from .views import (home, login_user, logout_user, register_user, staff_record, delete_staff_record, 
                    update_staff_record, add_staff_record, appointment_record, bookapt, delete_appointment_record, 
                    update_appointment_record, appointment_register, faq_chatbot, compost_inquiry, compost_inquiry_record, 
                    update_compost_inquiry_record, delete_compost_inquiry_record, blog_show, add_blog, update_blog, 
                    delete_blog, contact_us, contact_record, delete_contact, product_list, add_product, update_product, 
                    delete_product, feedback, feedback_record, delete_feedback, update_selected_person)

class WasteManagementViewsTests(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        self.admin_user = User.objects.create_user(
            username='binod.raut@wastebuddy.com',
            password='1234'
        )

    def test_home_view(self):
        request = self.factory.get(reverse('home'))
        middleware = SessionMiddleware(lambda x: None)
        middleware.process_request(request)
        response = home(request)
        self.assertEqual(response.status_code, 200)

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

        



    
    def test_register_view(self):
        
        # Test registration with invalid data
        request = self.factory.post(reverse('register_user'), {'email': 'existing@example.com', 'password1': 'testpassword', 'password2': 'testpassword'})
        response = register_user(request)
        self.assertEqual(response.status_code, 200)  # Registration form should be displayed again

        # Test registration with missing data
        request = self.factory.post(reverse('register_user'), {'password1': 'testpassword', 'password2': 'testpassword'})
        response = register_user(request)
        self.assertEqual(response.status_code, 200)  # Registration form should be displayed again

    def test_staff_record_view(self):
        # Log in as admin user
        self.client.login(username='binod.raut@wastebuddy.com', password='1234')

        # Test viewing staff record with valid ID
        response = self.client.get(reverse('record', args=[1]))
        
        # Test viewing staff record with invalid ID
        response = self.client.get(reverse('record', args=[999]))
        self.assertEqual(response.status_code, 302)


    
    def test_appointment_record_view(self):
        # Log in as admin user
        self.client.login(username='binod.raut@wastebuddy.com', password='1234')

        # Test viewing appointment record with valid ID
        response = self.client.get(reverse('appointment_record', args=[1]))
        

        # Test viewing appointment record with invalid ID
        response = self.client.get(reverse('appointment_record', args=[999]))
        self.assertEqual(response.status_code, 302)

        
    def test_faq_chatbot_view(self):
        # Test accessing the FAQ chatbot view without authentication
        request = self.factory.get(reverse('faq_chatbot'))
        middleware = SessionMiddleware(lambda x: None)
        middleware.process_request(request)
        response = self.client.get(reverse('faq_chatbot'))
        self.assertEqual(response.status_code, 200)

        # Log in as normal user
        self.client.login(username='binod.raut@wastebuddy.com', password='1234')

        # Test accessing the FAQ chatbot view as an authenticated user
        response = self.client.get(reverse('faq_chatbot'))
        self.assertEqual(response.status_code, 200)

    def test_compost_inquiry_view(self):
        # Test accessing the compost inquiry view without authentication
        request = self.factory.get(reverse('compost_inquiry'))
        middleware = SessionMiddleware(lambda x: None)
        middleware.process_request(request)
        response = self.client.get(reverse('compost_inquiry'))
        self.assertEqual(response.status_code, 200)

        # Log in as admin user
        self.client.login(username='binod.raut@wastebuddy.com', password='1234')

        # Test accessing the compost inquiry view as an authenticated user
        response = self.client.get(reverse('compost_inquiry'))
        self.assertEqual(response.status_code, 200)

        # Test submitting a compost inquiry form
        response = self.client.post(reverse('compost_inquiry'), {
            'full_name': 'Sushant Mahat',
            'email': 'Sushant@gmail.com',
            'phone': '1234567890',
            'quantity': 5,
            'message': 'I would like to inquire about composting services.'
        })
        self.assertEqual(response.status_code, 302)  # Redirects to the same page after form submission

    
    def test_blog_show_view(self):
        # Test accessing the blog show view without authentication
        request = self.factory.get(reverse('blog_show'))
        middleware = SessionMiddleware(lambda x: None)
        middleware.process_request(request)
        response = self.client.get(reverse('blog_show'))
        self.assertEqual(response.status_code, 200)

        # Log in as admin user
        self.client.login(username='binod.raut@wastebuddy.com', password='1234')

        # Test accessing the blog show view as an authenticated user
        response = self.client.get(reverse('blog_show'))
        self.assertEqual(response.status_code, 200)

    def test_add_blog_view(self):
        # Test accessing the add blog view without authentication
        request = self.factory.get(reverse('add_blog'))
        middleware = SessionMiddleware(lambda x: None)
        middleware.process_request(request)
        response = self.client.get(reverse('add_blog'))
        

        # Log in as admin user
        self.client.login(username='binod.raut@wastebuddy.com', password='1234')

        # Test accessing the add blog view as an authenticated user
        response = self.client.get(reverse('add_blog'))
        self.assertEqual(response.status_code, 200)

        # Test submitting a blog post form
        response = self.client.post(reverse('add_blog'), {
            'title': 'Test Blog Post',
            # Add other required fields here
        })
        self.assertEqual(response.status_code, 200) 

    def test_update_blog_view(self):
        # Log in as admin user
        self.client.login(username='binod.raut@wastebuddy.com', password='1234')

        # Create a blog post to update
        blog_post = BlogPost.objects.create(title='Test Blog Post', content='This is a test blog post.')

        # Test accessing the update blog view with a valid blog post ID
        response = self.client.get(reverse('update_blog', args=[blog_post.pk]))
        

        # Test updating the blog post with valid data
        response = self.client.post(reverse('update_blog', args=[blog_post.pk]), {
            'title': 'Updated Blog Post',
            'content': 'This is an updated test blog post.'
            # Add other required fields here
        })
        self.assertEqual(response.status_code, 302)  # Redirects to blog show page after successful update

        # Test updating the blog post with invalid data
        response = self.client.post(reverse('update_blog', args=[blog_post.pk]), {
            'title': '',
            'content': 'This is an updated test blog post.'
            # Invalid data, title is required
        })
        self.assertEqual(response.status_code, 302)  # Renders the form again with errors

    def test_delete_blog_view(self):
        # Log in as admin user
        self.client.login(username='binod.raut@wastebuddy.com', password='1234')

        # Create a blog post to delete
        blog_post = BlogPost.objects.create(title='Test Blog Post', content='This is a test blog post.')

        # Test accessing the delete blog view with a valid blog post ID
        response = self.client.get(reverse('delete_blog', args=[blog_post.pk]))
        

        # Test deleting the blog post
        response = self.client.post(reverse('delete_blog', args=[blog_post.pk]))
        self.assertEqual(response.status_code, 302)

    def test_contact_us_view(self):
        # Test accessing the contact us view
        request = self.factory.get(reverse('contact_us'))
        middleware = SessionMiddleware(lambda x: None)
        middleware.process_request(request)
        response = self.client.get(reverse('contact_us'))
        self.assertEqual(response.status_code, 200)

        # Test submitting the contact form with valid data
        response = self.client.post(reverse('contact_us'), {
            'full_name': 'Sushant Mahat',
            'email': 'Sushant@gmail.com',
            'message': 'Test message'
            # Add other required fields here
        })
        self.assertEqual(response.status_code, 200)  # Renders the same page with success message

        # Test submitting the contact form with invalid data
        response = self.client.post(reverse('contact_us'), {
            'full_name': '',
            'email': 'Sushant@gmail.com',
            'message': 'Test message'
            # Invalid data, full_name is required
        })
        self.assertEqual(response.status_code, 200)  # Renders the same page with errors

    def test_contact_record_view_authenticated_admin(self):
        # Log in as admin user
        self.client.login(username='binod.raut@wastebuddy.com', password='1234')

        # Create a contact record to view
        contact_record = Contact_Us.objects.create(full_name='Sushant Mahat', email='Sushant@gmail.com', message='Test message')

        # Test accessing the contact record view with a valid contact record ID
        response = self.client.get(reverse('contact_record', args=[contact_record.pk]))
        

    def test_delete_contact_view(self):
        # Log in as admin user
        self.client.login(username='binod.raut@wastebuddy.com', password='1234')

        # Create a contact record to delete
        contact_record = Contact_Us.objects.create(full_name='Sushant Mahat', email='Sushant@gmail.com', message='Test message')

        # Test accessing the delete contact view with a valid contact record ID
        response = self.client.get(reverse('delete_contact', args=[contact_record.pk]))
        

        # Test deleting the contact record
        response = self.client.post(reverse('delete_contact', args=[contact_record.pk]))
        self.assertEqual(response.status_code, 302)

    def test_product_list_view(self):
        # Test accessing the product list view
        request = self.factory.get(reverse('product_list'))
        middleware = SessionMiddleware(lambda x: None)
        middleware.process_request(request)
        response = self.client.get(reverse('product_list'))
        self.assertEqual(response.status_code, 200)

        # You can add more specific tests for the content of the product list if needed

    def test_add_product_view_authenticated_admin(self):
        # Log in as admin user
        self.client.login(username='binod.raut@wastebuddy.com', password='1234')

        # Test accessing the add product view
        request = self.factory.get(reverse('add_product'))
        middleware = SessionMiddleware(lambda x: None)
        middleware.process_request(request)
        response = self.client.get(reverse('add_product'))
        

        # Test submitting the add product form with valid data
        response = self.client.post(reverse('add_product'), {
            'name': 'Test Product',
            'price': '10.99',
            # Add other required fields here
        })
        self.assertEqual(response.status_code, 302)  # Redirects after successful submission

        # Test submitting the add product form with invalid data
        response = self.client.post(reverse('add_product'), {
            'name': '',
            'price': '10.99',
            # Invalid data, name is required
        })
        self.assertEqual(response.status_code, 302)  # Renders the same page with errors

    def test_update_product_view_authenticated_admin(self):
        # Log in as admin user
        self.client.login(username='binod.raut@wastebuddy.com', password='1234')

        # Create a product to update
        product = Product.objects.create(name='Test Product', price='10.99')

        # Test accessing the update product view with a valid product ID
        response = self.client.get(reverse('update_product', args=[product.pk]))
        

        # Test submitting the update product form with valid data
        response = self.client.post(reverse('update_product', args=[product.pk]), {
            'name': 'Updated Product',
            'price': '20.99',
            # Add other required fields here
        })
        self.assertEqual(response.status_code, 302)  # Redirects after successful submission

        # Test submitting the update product form with invalid data
        response = self.client.post(reverse('update_product', args=[product.pk]), {
            'name': '',
            'price': '20.99',
            # Invalid data, name is required
        })
        self.assertEqual(response.status_code, 302)  # Renders the same page with errors

    def test_delete_product_view_authenticated_admin(self):
        # Log in as admin user
        self.client.login(username='binod.raut@wastebuddy.com', password='1234')

        # Create a product to delete
        product = Product.objects.create(name='Test Product', price='10.99')

        # Test accessing the delete product view with a valid product ID
        response = self.client.get(reverse('delete_product', args=[product.pk]))
        

        # Test deleting the product
        response = self.client.post(reverse('delete_product', args=[product.pk]))
        self.assertEqual(response.status_code, 302)  # Redirects to home page after successful deletion

    def test_feedback_view(self):
        # Test accessing the feedback view
        request = self.factory.get(reverse('feedback'))
        middleware = SessionMiddleware(lambda x: None)
        middleware.process_request(request)
        response = self.client.get(reverse('feedback'))
        self.assertEqual(response.status_code, 200)

        # Test submitting the feedback form with valid data
        response = self.client.post(reverse('feedback'), {
            'name': 'Sushant Mahat',
            'rating': 5,
            'message': 'Test feedback message',
            # Add other required fields here
        })
        self.assertEqual(response.status_code, 200)  # Renders the same page with success message

        # Test submitting the feedback form with invalid data
        response = self.client.post(reverse('feedback'), {
            'name': '',
            'rating': 5,
            'message': 'Test feedback message',
            # Invalid data, name is required
        })
        self.assertEqual(response.status_code, 200)  # Renders the same page with errors

    def test_feedback_record_view_authenticated_admin(self):
        # Log in as admin user
        self.client.login(username='binod.raut@wastebuddy.com', password='1234')

        # Create a feedback record to view
        feedback_record = Feedback.objects.create(name='John Doe', rating=5, message='Test feedback message')

        # Test accessing the feedback record view with a valid feedback record ID
        response = self.client.get(reverse('feedback_record', args=[feedback_record.pk]))
        

    def test_delete_feedback_view_authenticated_admin(self):
        # Log in as admin user
        self.client.login(username='binod.raut@wastebuddy.com', password='1234')

        # Create a feedback record to delete
        feedback_record = Feedback.objects.create(name='Sushant Mahat', rating=5, message='Test feedback message')

        # Test accessing the delete feedback view with a valid feedback record ID
        response = self.client.get(reverse('delete_feedback', args=[feedback_record.pk]))
        

        # Test deleting the feedback record
        response = self.client.post(reverse('delete_feedback', args=[feedback_record.pk]))
        self.assertEqual(response.status_code, 302)
