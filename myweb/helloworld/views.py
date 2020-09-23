from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from json import dumps 
from .Yelp import *
def hello(request):
    if(request.method=="POST"):
        location1 = request.POST.get('location')
        restaurants = locateuser(location1)
        restaurantlist = listofr(location1)
        dataJSON = dumps(restaurantlist)
        return render(request,'landing.html',{'num' : restaurants, 'listofr':dataJSON})
    return render(request,'landing.html',{'num' : locateuser('modesto')})
def finder(request):
    return render(request,'finder.html')

