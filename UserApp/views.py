from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .forms import UserProfileForm, UpdatePersonalInfoForm, UpdateAccountInfoForm
from django.contrib.auth import logout


def user_profile(request, username):
    user_profile = UserProfile.objects.get(user__username=username)
    return render(request, 'UserApp/user_profile.html', {'user_profile': user_profile})

@login_required(login_url='AuthenticationApp:login')
def create_profile(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        user_profile = UserProfile(user=request.user)
        user_profile.save()

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('UserApp:user_profile', username=request.user.username)
    else:
        form = UserProfileForm(instance=user_profile)

    return render(request, 'UserApp/create_profile.html', {'form': form})

@login_required(login_url='AuthenticationApp:login')
def edit_profile(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        user_profile = UserProfile(user=request.user)
        user_profile.save()

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('UserApp:user_profile', username=request.user.username)
    else:
        form = UserProfileForm(instance=user_profile)

    return render(request, 'UserApp/edit_profile.html', {'form': form})


@login_required(login_url='AuthenticationApp:login')
def update_account_info(request):
    # Ensure the user has a related UserProfile
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        user_profile = UserProfile(user=request.user)
        user_profile.save()

    if request.method == 'POST':
        form = UpdateAccountInfoForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('UserApp:settings')
    else:
        form = UpdateAccountInfoForm(instance=user_profile)

    return render(request, 'UserApp/update_account_info.html', {'form': form})

@login_required(login_url='AuthenticationApp:login')
def settings(request):
    user_profile = UserProfile.objects.get(user=request.user)

    # Handle form submissions based on the form submitted
    if request.method == 'POST':
        form_name = request.POST.get('form_name')

        # Initialize the forms to None
        personal_info_form = None
        # account_info_form = None

        # Personal Info Form
        if form_name == 'personal_info':
            personal_info_form = UpdatePersonalInfoForm(request.POST, instance=user_profile)
            if personal_info_form.is_valid():
                personal_info_form.save()
                
        # # Account Info Form
        # elif form_name == 'account_info':
        #     account_info_form = UpdateAccountInfoForm(request.POST, instance=request.user.userprofile)
        #     if account_info_form.is_valid():
        #         account_info_form.save()

    else:
        # Initial rendering of the forms
        personal_info_form = UpdatePersonalInfoForm(instance=user_profile)
        # account_info_form = UpdateAccountInfoForm(instance=request.user.userprofile)


    context = {
        'personal_info_form': personal_info_form,
        # 'account_info_form': account_info_form,
    }

    return render(request, 'UserApp/settings.html', context)


