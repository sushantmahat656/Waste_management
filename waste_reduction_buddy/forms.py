from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Record, Appointment, Compost_inquiry,BlogPost
from datetime import date, timedelta

class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}))
    first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
    last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}))

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['placeholder'] = 'Email Address'
        self.fields['email'].label = ''

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class AddStaffRecord(forms.ModelForm):
    first_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"First Name", "class":"form-control"}), label="First Name")
    last_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Last Name", "class":"form-control"}), label="Last Name")
    email = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Email", "class":"form-control"}), label="Email")
    phone = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Phone", "class":"form-control"}), label="Phone")
    address = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Address", "class":"form-control"}), label="Address")
    city = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"City", "class":"form-control"}), label="City")
    state = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"State", "class":"form-control"}), label="State")
    zipcode = forms.IntegerField(required=True, widget=forms.widgets.NumberInput(attrs={"placeholder":"Zipcode", "class":"form-control"}), label="Zipcode",min_value=0)

    class Meta:
        model = Record
        exclude = ("User",)



class AppointmentRecord(forms.ModelForm):
    full_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Full Name", "class":"form-control"}), label="Full Name")    
    email = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Email", "class":"form-control"}), label="Email")
    phone = forms.CharField(required=True, min_length=10, widget=forms.widgets.TextInput(attrs={"placeholder":"Phone", "class":"form-control"}), label="Phone")
    address = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Address", "class":"form-control"}), label="Address")
    calendar = forms.DateField(widget=forms.widgets.DateInput(attrs={"type":"date", "class":"form-control", "id":"id_calendar"}), label="Date")
    
    CHOICES = [('sell', 'Sell'), ('donate', 'Donate')]
    selling_option = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(), label='Selling Option', initial='sell')  

    class Meta:
        model = Appointment
        fields = ['full_name', 'email', 'phone', 'address', 'calendar', 'selling_option']
        exclude = ("User",)

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if len(phone) < 10:
            raise ValidationError("Phone number must be at least 10 characters long.")
        elif len(phone) > 16:
            raise ValidationError("Phone number must be at most 16 characters long.")
        return phone

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set min and max dates for calendar widget
        today = date.today()
        self.fields['calendar'].widget.attrs['min'] = today.strftime('%Y-%m-%d')
        self.fields['calendar'].widget.attrs['max'] = (today + timedelta(days=60)).strftime('%Y-%m-%d')

        

class SelectedPersonUpdateForm(forms.ModelForm):
    selected_person = forms.ModelChoiceField(
        queryset=Record.objects.all(),
        widget=forms.Select(attrs={"class": "form-control"}),
        label="Select Person"
    )

    class Meta:
        model = Appointment
        fields = ['selected_person']





class CompostInquiryForm(forms.ModelForm):
    full_name = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "First Name", "class": "form-control"}))
    email = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Email", "class": "form-control"}))
    phone = forms.IntegerField(widget=forms.NumberInput(attrs={"placeholder": "Phone", "class": "form-control"}))
    quantity = forms.IntegerField(widget=forms.NumberInput(attrs={"placeholder": "Quantity in KG(Kilo Gram) ", "class": "form-control"}))
    message = forms.CharField(widget=forms.Textarea(attrs={"placeholder": "Message Of only 200 characters are allowed...", "class": "form-control", "rows": 4}))

    class Meta:
        model = Compost_inquiry
        fields = ['full_name', 'email', 'phone', 'quantity', 'message']

    def clean_quantity(self):
        quantity = self.cleaned_data['quantity']
        if quantity <= 0:
            raise forms.ValidationError("Quantity must be greater than 0.")
        return quantity


class BlogPostForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Title", "class": "form-control"}))
    image = forms.ImageField(widget=forms.ClearableFileInput(attrs={"class": "form-control"}))
    content = forms.CharField(widget=forms.Textarea(attrs={"placeholder": "Content", "class": "form-control summernote", "rows": 4}))

    class Meta:
        model = BlogPost
        fields = ['title', 'image', 'content']

