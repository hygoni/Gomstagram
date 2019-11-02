# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def index(req):
    return render(req, 'index.html')
# Create your views here.
