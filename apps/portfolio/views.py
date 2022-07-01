from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, UpdateView, DeleteView, View
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.forms import modelformset_factory, ModelForm, forms
from django.contrib.auth.decorators import login_required
# import the models that will be used
from .models import Portfolio, Project
# import the forms that are needed
from .forms import UserForm


# Create your views here.
class IndexView(TemplateView):
    template_name = "portfolio/index.html"

##########################################################################
# CUSTOMIZED VIEWS BELOW:
##########################################################################
"""
Basic View Setup using CBV

class IndexView(TemplateView):
    template_name = "portfolio/index.html"
    model = Portfolio # Model the view is based on
    context_object_name = model_object

"""

# EVENTUALLY I WILL MAKE IT TO WHERE THE USER MUST BE LOGGED IN
# class PortfolioView(View, LoginRequiredMixin, UserPassesTestMixin):
#     model = Portfolio
#     context_object_name = 'portfolio'
#     template_name = "portfolio/portfolio.html"

class PortfolioView(DetailView):
    model = Portfolio
    context_object_name = 'portfolio'
    template_name = "portfolio/portfolio.html"


# Create a basic FBV for user registration:
def register(response):
    if response.method == 'POST':
        form = RegisterForm(response.POST)
