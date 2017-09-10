from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.base import TemplateView
from posts.models import Post


class HomeView(ListView):
    template_name = 'home/index.html'
    model = Post
    queryset = Post.objects.order_by('-date_published')[:10]

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['heading_img'] = 'img/home-bg.jpg'
        return context

class AboutView(TemplateView):
    template_name = 'home/about.html'

    def get_context_data(self, **kwargs):
        kwargs['heading_img'] = 'img/about-bg.jpg'
        return kwargs

class ContactView(TemplateView):
    template_name = 'home/contact.html'

    def get_context_data(self, **kwargs):
        kwargs['heading_img'] = 'img/contact-bg.jpg'
        return kwargs
