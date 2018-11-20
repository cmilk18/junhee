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
winrate=0
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
    global c
    global winrate
    json_str = ((request.body).decode('utf-8'))
    received_json_data = json.loads(json_str)
    datacontent = received_json_data['content']


    b = random.randrange(0,3)
    if datacontent == ('시작하기' or '진행')and section == 0:

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
        if datacontent == "가위":
            a = '가위'


            if a == '가위'and c == '보':
                allcounter += 1
                wincounter += 1
                section += 1
                return JsonResponse({
                    'message': {
                        'text': "나는 가위를 냈고 컴퓨터는 보를 냈습니다.\n  이겼어\n"
                    },
                    'keyboard': {
                        'type': 'buttons',
                        'buttons': ['진행']
                    }
                })
            elif a == '가위' and c == '바위':
                allcounter += 1
                losecounter += 1
                section += 1
                return JsonResponse({
                    'message': {
                        'text': "나는 가위를 냈고 컴퓨터는 바위를 냈습니다.\n졌엉 ㅠㅜㅠㅜㅠㅜㅠㅜ\n"
                    },
                    'keyboard': {
                        'type': 'buttons',
                        'buttons': ['진행']
                    }
                })

            elif a == '가위' and c == '가위':
                allcounter += 1
                drawcounter += 1
                section += 1
                return JsonResponse({
                    'message': {
                     'text': "나는 가위를 냈고 컴퓨터도 가위를 냈습니다.\n비겼습니다.~~~~\n"
                    },
                    'keyboard': {
                        'type': 'buttons',
                        'buttons': ['진행']
                    }
                })


        if datacontent == "바위":
            a='바위'

            if a == '바위'and c == '가위':
                allcounter += 1
                wincounter += 1
                section += 1
                return JsonResponse({
                    'message': {
                        'text': "나는 바위를 냈고 컴퓨터는 가위를 냈습니다.\n이겼습니다~~!\n"
                    },
                    'keyboard': {
                        'type': 'buttons',
                        'buttons': ['진행']
                    }
                })

            elif a == '바위' and c == '바위':
                allcounter += 1
                drawcounter += 1
                section += 1
                return JsonResponse({
                    'message': {
                     'text': "나는 바위를 냈고 컴퓨터도 바위를 냈습니다.\n비겼습니다~~!\n"
                        },
                    'keyboard': {
                        'type': 'buttons',
                        'buttons': ['진행']
                    }
                })

            elif a == '바위' and c == '보':
                allcounter += 1
                losecounter += 1
                section += 1
                return JsonResponse({
                    'message': {
                        'text': "나는 바위를 냈고 컴퓨터도 보를 냈습니다.\n졌어요ㅠㅜㅠㅜ\n"
                        },
                    'keyboard': {
                        'type': 'buttons',
                        'buttons': ['진행']
                    }
                })

        if datacontent == "보":
            a = '보'

            if a == '보'and c == '가위':
                allcounter += 1
                losecounter += 1
                section += 1
                return JsonResponse({
                    'message': {
                        'text': "나는 보를 냈고 컴퓨터는 가위를 냈습니다.\n졌어유ㅜㅠㅜㅠㅜㅠㅜ\n"
                    },
                    'keyboard': {
                        'type': 'buttons',
                        'buttons': ['진행']
                    }
                })

            elif a == '보' and c == '바위':
                allcounter += 1
                wincounter += 1
                section += 1
                return JsonResponse({
                    'message': {
                        'text': "나는 보를 냈고 컴퓨터는 바위를 냈습니다.\n이겼다리\n"
                        },
                    'keyboard': {
                        'type': 'buttons',
                        'buttons': ['진행']
                    }
                })

            elif a == '보' and c == '보':
                allcounter += 1
                drawcounter += 1
                section += 1
                return JsonResponse({
                    'message': {
                        'text': "나는 보를 냈고 컴퓨터는 보를 냈습니다.\n비겼습니다\n"
                    },
                    'keyboard': {
                        'type': 'buttons',
                        'buttons': ['진행']
                    }
                })

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
                'text': "전체"+str(allcounter)+"game\n WIN : "+str(wincounter)+"\n LOSE : "+str(losecounter)+"\nDRAW : "+str(drawcounter)+"입니다.\n 승률 : "+str(winrate)+"% "
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['진행']
            }
        })


