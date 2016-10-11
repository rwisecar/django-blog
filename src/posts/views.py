from django.http import HttpResponse
from django.shortcuts import render


def post_create(request):
    return HttpResponse("<h1>Hello</h1>")

def post_detail(request):
    return HttpResponse("<h1>Please?</h1>")

def post_list(request):
    return HttpResponse("<h1>ABC</h1>")

def post_update(request):
    return HttpResponse("<h1>Try This:</h1>")

def post_delete(request):
    return HttpResponse("<h1>Exterminate</h1>")
