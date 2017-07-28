# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
import bcrypt
from validations import validReg, validLogin, validForm
from .models import User, Trip
from datetime import datetime

def index(request):
    return render(request, 'travelApp/index.html')

def register(request):
    #check if requested information is valid
    state=validReg(request.POST)
    if state['isValid']:
        #check to see if user already exists with that username
        notDup=userExist(request.POST['username'])
        if not notDup:
            #hash password
            password = encrypt_password(request.POST['password'])
            User.objects.create(name=request.POST['name'], username=request.POST['username'], password=password)

            request.session['user']=request.POST['username']

            return redirect('/travels')

        else:
            errors=["That username is already taken."]
            context={
                'errors':errors
            }
            return render(request, 'travelApp/index.html', context)
    else:
        errors =  state['errors']
        context={
            'errors':errors
        }
        return render(request, 'travelApp/index.html', context)

def login(request):
    #check if requested information is valid
    state=validLogin(request.POST)
    if state['isValid']:
        #check if user exists
        exists = userExist(request.POST['username'])
        #if exists, check password
        if exists:
            valid = checkPassword(request.POST['username'], request.POST['password'])
            print valid
            #if passwords match, log user in
            if valid:
                request.session['user']=request.POST['username']
                return redirect('/travels')
            else:
                errors=["Your email and password combination was not in our system"]
                context={
                    'errors':errors
                }
                return render(request, 'travelApp/index.html', context)

        else:
            errors=["Your email and password combination was not in our system"]
            context={
                'errors':errors
            }
            return render(request, 'travelApp/index.html', context)
    else:
        errors =  state['errors']
        context={
            'errors':errors
        }
        return render(request, 'travelApp/index.html', context)

def userExist(username):
    dup=False
    user=User.objects.filter(username=username)
    if len(user)==0:
        dup=False
        return dup
    else:
        dup=True
        return dup

def encrypt_password(password):
    salt=bcrypt.gensalt(9)
    password = bcrypt.hashpw(password.encode(), salt)
    return password

def checkPassword(username, password):
    get_password = User.objects.get(username=username)
    validPassword = bcrypt.hashpw(password.encode(), get_password.password.encode())
    if str(validPassword) == str(get_password.password):
        return True
    else:
        return False


def travels(request):

    users = User.objects.all()
    currentUser = User.objects.get(username=request.session['user'])
    trips=Trip.objects.all()
    context={
        'currentUser':currentUser,
        'users':users,
        'trips':trips,
    }
    return render(request, "travelApp/travels.html", context)

def add(request):
    if request.method=='GET':
        return redirect('/')
    return render(request, "travelApp/add.html")

def addPlan(request):

    currentUser = User.objects.get(username=request.session['user'])
    state = validForm(request.POST)
    print state
    print request.POST
    if state['isValid']:
        this_trip=Trip.objects.create(destination=request.POST['destination'], description=request.POST['description'], start_date=request.POST['startDate'], end_date=request.POST['endDate'], created_by=currentUser)

        this_trip.users.add(currentUser)
        this_trip.save()
        return redirect('/travels')
    else:
        errors =  state['errors']
        context={
            'errors':errors
        }
        return render(request, "travelApp/add.html", context)

def destination(request, id):
    trip=Trip.objects.get(id=id)

    context={
        'trip':trip
    }
    return render(request, "travelApp/destination.html", context)

def join(request, id):
    trip=Trip.objects.get(id=id)
    user=User.objects.get(username=request.session['user'])
    trip.users.add(user)
    trip.save()
    return redirect('/travels')

def logoff(request):
    request.session['user']=None
    return redirect('/')
