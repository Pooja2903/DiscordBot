import os

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def startBot(request):
    os.system('python3 bot/searchBot.py')