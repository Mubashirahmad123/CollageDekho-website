# from django import forms
# from django.forms import ModelForm
# from .models import profile
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
# class ProfileForm(forms.ModelForm):
#     class Meta:
#         model = profile
#         fields = "__all__"

#         # fields = ['name', 'age', 'gender', 'occupation']
#         exclude=[ 'date_of_birth', 'user',
#                  ]



# class RegistrationForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']



# def register(request):
#     if request.method =='POST':
#         form =  RegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             # user = form.save(commit=False)
#             # user.is_email_verified = False
#             # user.email_verification_token = str(uuid.uuid4())
#             # user.save()

#             # current_site = get_current_site(request)
#             # mail_subject = 'Activate your account'
#             # activation_link = f"http://{current_site}/app/verify_email/{ user.email_verification_token }/"
#             # message =f"Click the link to activate your account: { activation_link}"
#             # send_mail( mail_subject,message, 'magicfix@gmail.com', [user.email])


#             return redirect('app:login')
#     else:
#         form = RegistrationForm()

#     return render(request, 'app/register.html', {'form':form})


#LOGIN VIEW

# def login_view(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             # if user.is_email_verified:
#             login(request, user)
#             print("tillu")
#             return redirect('app:profile_list')  
        
#             # else:
#                 # messages.error(request, "Please verify  your email")
#                 # return redirect ('App:login')

#     else:
#         form = AuthenticationForm()

#     return render(request, 'app/login.html', {'form': form})
