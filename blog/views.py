# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.template import loader, context
from django.http import HttpResponse
from blog.models import BlogPost

"""..."""


def first(request):
    polka = BlogPost.objects.all()
    t = loader.get_template('first.html')
    c = context({'posts': polka})
    return HttpResponse(t.render(c))
