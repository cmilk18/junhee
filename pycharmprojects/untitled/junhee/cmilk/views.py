from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json

import requests


def keyboard(request):

    return JsonResponse({
        "type": "buttons",
        "buttons": ["시작하기"]

    })

@csrf_exempt
def answer(request):

    json_str = ((request.body).decode('utf-8'))
    received_json_data = json.loads(json_str)
    datacontent = received_json_data['content']

    if datacontent == '시작하기'
        from bs4 import BeautifulSoup
        req=requests.get('https://www.naver.com/')
        html = req.text
        soup = BeautifulSoup(html,'html.parser')
        title_list = soup.select('.PM_CL_realtimeKeyword_rolling span[class*=ah_k]')

        for idx, title in enumerate(title_list, 1):
            return JsonResponse({
                'message': {
                    'text': "idx, title.text"
                }})
