from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import UserForm
from vendor.forms import VendorForm
from .models import User, UserProfile

# Create your views here.
def register_user(request):
    if request.method == 'POST':
        print(request.POST)
        form = UserForm(request.POST)
        if form.is_valid():
            # Create the user using the form
            # password = form.cleaned_data['password']
            # user = form.save(commit=False)
            # user.set_password(password)
            # user.role = User.CUSTOMER
            # user.save()

            # Create the user using create_user method
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
            user.role = User.CUSTOMER
            user.save()     
            messages.success(request=request, message="Your account has been registered sucessfully!!")       
            return redirect('register_user')
        else:
            print('invalid form')
            print(form.errors)

    else:
        form = UserForm()
    context = {'form': form,}
    return render(request=request, template_name='accounts/register_user.html', context=context)

def register_vendor(request):
    if request.method == 'POST':
        # store the data and create the user
        form = UserForm(data=request.POST)
        v_form = VendorForm(data=request.POST, files=request.FILES)

        if form.is_valid() and v_form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
            user.role = User.VENDOR
            user.save()
            vendor = v_form.save(commit=False)
            vendor.user = user
            user_profile = UserProfile.objects.get(user=user)
            vendor.user_profile = user_profile
            vendor.save()
            messages.success(request=request, message="Your account has been registered sucessfully! Please wait for approval")       
            return redirect('register_vendor')
        else:
            print('Invalid Form')
            print(form.errors)

    else:
        form = UserForm()
        v_form = VendorForm()
    context = {'form': form, 'v_form': v_form}
    return render(request=request, template_name='accounts/register_vendor.html', context=context)