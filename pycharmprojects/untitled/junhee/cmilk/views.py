from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
import random


바위 = 1
가위 = 0
보 = 2
wincounter=0
losecounter=0
drawcounter=0
allcounter=0
section = 0

def keyboard(request):

    return JsonResponse({
        "type": "buttons",
        "buttons": ["시작하기"]

    })

@csrf_exempt
def answer(request):
    global section
    global 바위
    global 가위
    global 보
    global wincounter
    global losecounter
    global drawcounter
    global allcounter
    json_str = ((request.body).decode('utf-8'))
    received_json_data = json.loads(json_str)
    datacontent = received_json_data['content']


    b = random.randrange(0,3)
    if datacontent == '시작하기'and section == 0:

        if b == 1:
            c = '바위'
        if b == 0:
            c = '가위'
        if b == 2:
            c = '보'

        section += 1
        return JsonResponse({
            'message': {
                'text': "무엇을 낼지 골라주세요,종료하고 싶으면 종료를 눌러주세요"
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['가위', '바위', '보', '종료']
            }
            })

    if section == 1:
        section += 1
        if datacontent == "가위":
            a = '가위'


            if a == '가위'and b == 보:
                allcounter += 1
                wincounter += 1
                section += 1
                return JsonResponse({
                    'message': {
                        'text': "나는 가위를 냈고 컴퓨터는 보를 냈습니다.\n  이겼어\n"
                    },
                })
            elif a == '가위' and b == 바위:
                allcounter += 1
                losecounter += 1
                section += 1
                return JsonResponse({
                    'message': {
                        'text': "나는 가위를 냈고 컴퓨터는 바위를 냈습니다.\n졌엉 ㅠㅜㅠㅜㅠㅜㅠㅜ\n"
                    }})

            elif a == '가위' and b == 가위:
                allcounter += 1
                drawcounter += 1
                section += 1
                return JsonResponse({
                    'message': {
                     'text': "나는 가위를 냈고 컴퓨터도 가위를 냈습니다.\n비겼습니다.~~~~\n"
                    }})


        if datacontent == "바위":
            a='바위'

            if a == '바위'and b == 가위:
                allcounter += 1
                wincounter += 1
                section += 1
                return JsonResponse({
                    'message': {
                        'text': "나는 바위를 냈고 컴퓨터는 가위를 냈습니다.\n이겼습니다~~!\n"
                    }})

            elif a == '바위' and b == 바위:
                allcounter += 1
                drawcounter += 1
                section += 1
                return JsonResponse({
                    'message': {
                     'text': "나는 바위를 냈고 컴퓨터도 바위를 냈습니다.\n비겼습니다~~!\n"
                        }})

            elif a == '바위' and b == 보:
                allcounter += 1
                losecounter += 1
                section += 1
                return JsonResponse({
                    'message': {
                        'text': "나는 바위를 냈고 컴퓨터도 보를 냈습니다.\n졌어요ㅠㅜㅠㅜ\n"
                        }})

        if datacontent == "보":
            a = '보'

            if a == '보'and b == 가위:
                allcounter += 1
                losecounter += 1
                section += 1
                return JsonResponse({
                    'message': {
                        'text': "나는 보를 냈고 컴퓨터는 가위를 냈습니다.\n졌어유ㅜㅠㅜㅠㅜㅠㅜ\n"
                    }})

            elif a == '보' and b == 바위:
                allcounter += 1
                wincounter += 1
                section += 1
                return JsonResponse({
                    'message': {
                        'text': "나는 보를 냈고 컴퓨터는 바위를 냈습니다.\n이겼다리\n"
                        }})

            elif a == '보' and b == 보:
                allcounter += 1
                drawcounter += 1
                section += 1
                return JsonResponse({
                    'message': {
                        'text': "나는 보를 냈고 컴퓨터는 보를 냈습니다.\n비겼습니다\n"
                    }})

            if datacontent == "종료":
                section += 1
                return JsonResponse({
                    'message': {
                        'text': "고생하셨습니다.\n"
                    }})

    if section == 2:
        section = 0
        winrate = wincounter / allcounter * 100
        return JsonResponse({
            'message': {
                'text': "=============================== \n전체"+str(allcounter)+"에서"+str(wincounter)+"번 이겼고"+str(losecounter)+"번 졌어요.비긴건"+str(drawcounter)+"입니다.\n승률은"+str(winrate)+"% 입니다\n===============================\n"
            }})
