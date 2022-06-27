from django.shortcuts import render
from .forms import UserRegistrationForm
from .models import Profile
# Create your views here.


def register(request):
    user_registration_form = UserRegistrationForm(request.POST or None)
    if user_registration_form.is_valid():
        new_user = user_registration_form.save(commit=False)
        new_user.set_password(
            user_registration_form.cleaned_data['password'])
        new_user.save()
        Profile.objects.create(user=new_user)
        return render(request,
                      'account/user/register_done.html',
                      {'new_user': new_user})
    user_registration_form = UserRegistrationForm()
    return render(request,
                  'account/user/register.html',
                  {'user_registration_form': user_registration_form})
