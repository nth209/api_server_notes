from django.shortcuts import render
from django.http import JsonResponse
from config.config import config_status
from service import service
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
    if request.is_ajax():

        return JsonResponse(result_data(status['200'], message['200'], ))
    else:
        return JsonResponse(result_data(status['000'], message['000'], ))


