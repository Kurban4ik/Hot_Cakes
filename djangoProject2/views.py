from django.http import HttpResponse
from django.shortcuts import redirect
from dbFunctions.muslim import save_data
import sqlite3
from dbFunctions.ullubiy import host
from django.utils import timezone


def non(request):
    return HttpResponse('asdasda')

now = str(timezone.now())[:-13]
def rethrow_lays(request, transfer):
    print(f'{host}/lays/{transfer}')
    print(now)
    save_data(get_client_ip(request), f'{host}lays/{transfer}', 'lays', now)
    return redirect('https://lays.ru/')


def rethrow_pinterest(request, transfer):
    save_data(get_client_ip(request), f'{host}pinterest/{transfer}', 'pinterest', now)
    return redirect('https://www.pinterest.ru/')


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip