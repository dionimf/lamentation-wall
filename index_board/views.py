from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth import login, logout as auth_logout

from index_board.forms import LamentationForm, CounselForm, VisitModel
from index_board.models import *

from django.shortcuts import render_to_response
from django.template.context import RequestContext

import json
from mylib.general import get_client_ip
from datetime import datetime
import time

def index(request):

    form = LamentationForm(prefix='lamentation')

    visit = VisitModel()
    visit.ip = get_client_ip(request)
    visit.date = time.strftime('%Y-%m-%d %H:%M:%S')
    visit.request_method = request.method
    visit.save()

    if request.method == 'POST':
        form = LamentationForm(request.POST, prefix='lamentation')

        print(request.POST.get('text'))

        if form.is_valid():
            form.save(commit=True)
            
            return redirect("/lamentacoes")
        else:
            print(form.errors)

    lamentations = LamentModel.objects.order_by('-id')[:50]
    
    return render(request, 'me/index.djhtml',
                  {'user': request.user,
                   'form': form,
                   'counsel_form': CounselForm(prefix='counsel'),
                   'lamentations': lamentations})

def redirect_to_laments(request):
    return redirect("/lamentacoes")

def cry_together(request):
    try:
        lament = LamentModel.objects.get(id=request.GET.get('id'))
    except:
        lament = None

    if lament:
        lament.cries_together += 1
        lament.save()

        return HttpResponse(lament.cries_together)

def save_counsel(request):
    print('save_counsel')
    if request.method == 'POST':
        form = CounselForm(request.POST, prefix='counsel')

        if form.is_valid():
            form.save(commit=True)
            id = request.POST.get('counsel-lament_id')

            # count how many counsels
            count = LamentModel.objects.get(id=request.POST.get('counsel-lament_id')).count_counsels()

            # return the count for ajax
            response_data = {'count': count, 'lament_id': id}
            return HttpResponse(json.dumps(response_data))

    return HttpResponse(-1)

def list_counsels(request):
    if request.method == 'GET':
        lament_id = request.GET.get('lament')

        counsels = CounselModel.objects.filter(lament_id=lament_id)

        return render(request, 'me/list-counsels.djhtml',
                      { 'counsels': counsels })


def test(request):
    return render(request, 'me/test.djhtml')

def google_login(request):

    context = RequestContext(request,
                             {'user': request.user})
    return render_to_response('me/google-login.djhtml',
                              context_instance=context)

def twitter_auth_complete(request):
    print('auth:')
    print(request.user.is_authenticated())
    context = RequestContext(request, {'request': request,
                                       'user': request.user })
    user = request.user

    login(request, user)


def google_auth_complete(request):
    print('auth:')
    return HttpResponse(1)
    print(request.user.is_authenticated())
    context = RequestContext(request, {'request': request,
                                       'user': request.user })
    user = request.user

    login(request, user)

    # return render_to_response('me/index.djhtml', context_instance=context )

def auth_complete(request):
    return HttpResponse(request.user)

def login(request):
    return HttpResponse(request.user)
    
def logout(request):
    auth_logout(request)
    return redirect('/')
