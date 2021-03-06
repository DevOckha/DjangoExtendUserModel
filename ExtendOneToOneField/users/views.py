from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import UserForm, ProfileForm
from django.db import transaction
from django.contrib import messages
from django.utils.translation import gettext as _

@login_required
@transaction.atomic
def update_profile(request):
    
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, _('Your profile was successfuly updated'))
            return redirect('settings:profile')
        
        else:
            messages.error(request, _('Please correct the error below'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    
    return render(request, 'profiles/profile.html', context={
        'user_form':user_form,
        'profile_form':profile_form
    })
    


# @login_required
# @transaction.atomic
# def update_profile(request):
    
#     if request.method == 'POST':
#         user_form = UserForm(request.POST, instance=request.user)
#         profile_form = ProfileForm(request.POST, instance=request.user.profile)
        
#         if user_form.is_valid() and profile_form.is_valid():
#             user_form.save()
#             profile_form.save()
#             messages.success(request, _('Your profile was successfuly updated'))
#         else:
#             messages.error(request, _('Please correct the error below'))
#     else:
#         user_form = UserForm(instance=request.user)
#         profile_form = ProfileForm(instance=request.user.profile)

#     return render(request, 'profiles/profile.html', context={
#         'user_form':user_form,
#         'profile_form':profile_form
#     })
        

#hi