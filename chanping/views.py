# coding: utf-8
import datetime
from django.shortcuts import get_object_or_404, redirect

from chanping.models import Happy
from myproject.helper import crypt
from myproject.responseHooks import sw_render
from myproject.settings import HASH_KEY


def welcome(request):
    res = {}
    return sw_render(request, 'index.html', res)


def newpage(request):
    ip = request.META['REMOTE_ADDR']
    pwd = crypt(ip, HASH_KEY)
    if Happy.objects.filter(pwd=pwd).exists():
        return redirect("index", pwd=pwd)
    else:
        if request.method == 'POST':
            man = request.POST.get("boy", "")
            human = request.POST.get("girl", "")
            mettingtime = request.POST.get("mettingtime", "")
            newhappy = Happy()
            newhappy.man = man
            newhappy.human = human
            newhappy.mettingtime = mettingtime
            newhappy.pwd = pwd
            newhappy.save()
            return redirect("index", pwd=pwd)
        return sw_render(request, 'newpage.html')


def index(request, pwd=''):
    res = {}
    res['happy'] = get_object_or_404(Happy, pwd=pwd)
    res['now'] = datetime.datetime.now()
    return sw_render(request, 'index.html', res)


# Create your views here.

