from django.shortcuts import render
import json
from service import service
from config.config import config_status

from django.core import serializers
from django.contrib.auth.models import User
from django.contrib import auth
from django.http import JsonResponse
from django.forms.models import model_to_dict

from api.models import userDetail

status, message = config_status()


def checkType(request):
    if request.is_ajax():
        return 0
    else:
        return 1


def result_data(status, message, data='' ):
    result_data = {
        'status': status,
        'messgae': message,
        'data_result': data
    }
    return result_data


def apiViewsLogin(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        usr = body['username']
        pwd = body['password']
        user = auth.authenticate(username=usr, password=pwd)
        if user is not None:
            auth.login(request, user)
            id = request.user.id
            thongtin = userDetail.objects.filter(id_user=id)
            tmpJson = serializers.serialize("json", thongtin)
            tmpObj = json.loads(tmpJson)
            data = {
                'code': '001',
                'id': id,
                'thongtin':  tmpObj,
                'ten': request.user.first_name
            }
            respone = result_data(status['200'], message['200'],data)
            return JsonResponse(respone)
        else:
            return JsonResponse(result_data(status['000'], message['000'], ''))

    else:
        return JsonResponse(result_data(status['000'], message['000'],'' ))



