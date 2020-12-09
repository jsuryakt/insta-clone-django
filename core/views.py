from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View
from django.http import HttpResponse
from django.contrib.auth import logout

class FeedView(TemplateView):
    template_name = 'core/feed.html'
