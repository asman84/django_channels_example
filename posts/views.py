from django.shortcuts import render

# Create your views here.
from django.views import generic


class PostListView(generic.TemplateView):
    template_name = 'base.html'