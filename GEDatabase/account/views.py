# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import LoginForm
from .models import Profile

@login_required
def dashboard(request):
    return render(request,
           'account/dashboard.html',
           {'section': 'dashboard'})