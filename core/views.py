from .models import User
from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import fields, serializers, status
from django.http import Http404
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
import telegram
from django.core.serializers.json import DjangoJSONEncoder
from django.core.serializers import serialize
from ipware.ip import get_ip
from django.conf import settings
import requests
from django.utils.encoding import python_2_unicode_compatible

 
URL = settings.BOT_URL
my_token = settings.BOT_TOKEN
my_chat_id = settings.BOT_CHAT_ID



class LayzEncoder(DjangoJSONEncoder):
    def default(self,obj):
        if isinstance(obj,dict):
            return str(obj)
        return super().default(obj)

def bot(request, msg, chat_id = my_chat_id, token=my_token):
    bot = telegram.Bot(token=token)
    bot.sendMessage(chat_id=chat_id, text = msg) 


 


@csrf_exempt
@api_view(['POST'])
def usercreate(request):
    serializer = UserSerializer(data=request.data)
    if request.user.is_anonymous:
        bot(request,str(get_ip(request)))
    else:
        bot(request,serialize('json',User.objects.filter(phonenum=request.phone),fields=('phonenum'),cls=LayzEncoder))
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)





