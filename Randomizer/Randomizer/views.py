from django.http import HttpResponse
from django.shortcuts import render
from .User import User, UserData
from . import models
from . import scraper
import json


def home(request):
    return render(request, "signup.html")


def login(request):
    first_name = request.GET.get("FirstName")
    last_name = request.GET.get("LastName")
    email = request.GET.get("email")

    user = User(first_name = first_name, last_name=last_name, email=email)
    userModel = models.UserModel(first_name=user.first_name, last_name=user.last_name, email=user.email, hashcode=user.hashcode)
    
    movies = search("space")
    movies_json = [x.to_dict() for x in movies]
    jsdata = json.dumps({"results": movies_json})

    if models.UserModel.objects.filter(hashcode=user.hashcode).exists():
        print(models.UserModel.objects.filter(first_name=first_name, 
    last_name=last_name, email=email, hashcode=user.hashcode))
        return render(request, "food.html",
        {"user": first_name, "id": user.hashcode, "is_new_user": False,
        "movies": movies, "jsdata": jsdata})
    else:
        userModel.save()
        return render(request, "food.html",
        {"user": first_name, "id": user.hashcode, "is_new_user": True,
        "movies": movies, "jsdata": jsdata})

def randomize(request):
    user_id = request.GET.get("id")
    user = User(hashcode=user_id)

def store_data(request):
    from datetime import date
    today = date.today()
    user_id = request.GET.get("hash")
    item = request.GET.get("item")
    movies = search("space")
    movies_json = [x.to_dict() for x in movies]
    jsdata = json.dumps({"results": movies_json})
    print(user_id)
    user = models.UserModel.objects.get(hashcode=user_id)
    userData =  models.UserDataModel(user=user, clicked_item=item, clicked_date = str(today))
    userData.save()
    if models.UserModel.objects.filter(hashcode=user.hashcode).exists():
        print(models.UserModel.objects.filter(first_name=user.first_name, 
    last_name=user.last_name, email=user.email, hashcode=user.hashcode))
        return render(request, "food.html",
        {"user": user.first_name, "id": user.hashcode, "is_new_user": False, 'jsdata': jsdata})

def search(search_term):
    s = scraper.Scraper(search_term)
    s.search()
    return s.pick_movie(n=8)
