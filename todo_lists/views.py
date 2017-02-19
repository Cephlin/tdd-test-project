from django.shortcuts import render
from django.http import HttpResponse


def homepage(request):
    return HttpResponse(("<!DOCTYPE html>\n",
        "<html>\n",
        #"<head>\n",
        "<title>To-Do lists</title>\n",
        #"</head>\n")),
        "</html>"))
