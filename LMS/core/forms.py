from django import forms
from .models import User, Student, Admin, Book, Category, UserProfile
from django.contrib.auth.forms import UserCreationForm 


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_picture', 'bio']

        

class AdminRegistrationForm(UserCreationForm):
    staff_role = forms.CharField(max_length=50, required=True)

    username=forms.CharField(
        widget = forms.TextInput(
            attrs={
                #'placeholder':"Your username"
            }
        )
    )
    password1=forms.CharField(
        widget = forms.PasswordInput(
            attrs={
                #'placeholder':"Your password1"
            }
        )
    )
    password2=forms.CharField(
        widget = forms.PasswordInput(
            attrs={
                #'placeholder':"Confirm Your password"
            }
        )
    )
    email=forms.CharField(
        widget = forms.TextInput(
            attrs={
                #'placeholder':"Your email"
            }
        )
    )

    class Meta:
        model = User
        fields =('username', 'email','password1','password2', 'staff_role')
        
class StudentRegistrationForm(UserCreationForm):
    
    grade = forms.CharField(max_length=10, required=True)

    username=forms.CharField(
        widget = forms.TextInput(
            attrs={
                #'placeholder':"Your username"
            }
        )
    )
    password1=forms.CharField(
        widget = forms.PasswordInput(
            attrs={
                #'placeholder':"Your password1"
            }
        )
    )
    password2=forms.CharField(
        widget = forms.PasswordInput(
            attrs={
                #'placeholder':"Confirm Your password"
            }
        )
    )
    email=forms.CharField(
        widget = forms.TextInput(
            attrs={
                #'placeholder':"Your email"
            }
        )
    )
    
    
    class Meta:
        model = User
        fields = ('username', 'password1','password2', 'email','grade')

    def clean_student_id(self):
        student_id = self.cleaned_data.get('student_id')
        if Student.objects.filter(student_id=student_id).exists():
            raise forms.ValidationError("This student ID is already in use.")
        return student_id
    

class CustomLoginForm(forms.Form):
    username = forms.CharField(widget = forms.TextInput, max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)
    # You can add any additional fields you need here

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

class BookForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all(), label="Choose a category")
    available_copies = forms.IntegerField(label='New Quantity',min_value=0,)
    
    class Meta:
        model = Book
        fields = ['title', 'author', 'category','available', 'available_copies']  # Add other fields here
        widgets = {
            'available': forms.HiddenInput(),  # Hide the availability field for form submission
            'available_copies':forms.NumberInput(attrs={'class': 'form-control'}),
        }


class BookSearchForm(forms.Form):
    query = forms.CharField(
        label="Search Books",
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Search by Book Name, Author, or Category'}),
    )
class StudentSearchForm(forms.Form):
    search_query = forms.CharField(label='Search by Name or Student ID', max_length=100)


class UpdateAvailabilityForm(forms.Form):
    book_id = forms.IntegerField(widget=forms.HiddenInput)
    new_availability = forms.IntegerField(label='New Availability')





