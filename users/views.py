from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy

class SignUpView(CreateView):
  form_class = SingUpForm
  template_name = 'users/signup.html'
  success_url = reverse_lazy('core:home')