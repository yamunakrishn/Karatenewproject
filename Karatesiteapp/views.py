from atexit import register
import json
from .models import *
from django.http import BadHeaderError
from django.shortcuts import redirect, render
from urllib import request
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth import authenticate ,login, logout
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.http import HttpResponse
from django.core.mail import send_mail,BadHeaderError
from django.views.decorators.csrf import csrf_exempt




def homepage(request):
    return render(request,'index.html')


def affiliation(request):
    return render(request, 'affiliation.html')

def member(request):
    return render(request,'member.html')
