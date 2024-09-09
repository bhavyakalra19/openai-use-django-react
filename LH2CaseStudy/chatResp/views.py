from django.shortcuts import render
import os
from openai import OpenAI
from dotenv import load_dotenv
# from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *


load_dotenv()

api_key = os.getenv("OPENAI_KEY",None)
client = OpenAI(api_key=api_key)

@api_view(['POST'])
def chatbot(request):
    dest_obj = []
    if request.data is not None:
        dest_obj = DestinationData.objects.filter(dest_name = request.data['name'])
        if dest_obj:
            print(dest_obj)
            serializer = DestSerializer(dest_obj, many = True)
            return Response({'status': 200, 'message': serializer.data})

        if api_key is not None:
            chatbot_resp = None
            user_input = request.data['name']
            prompt = [
                    {"role": "system", "content":"You are a travel agent"},
                    {"role":"user", "content":"Give me Top 5 destinations in %s" % user_input},
                ],
            chatbot_resp = client.chat.completions.create(
                model="gpt-3.5-turbo-1106", 
                messages=prompt,
                max_tokens=50,
                temperature=0.7
            )
            if chatbot_resp is not None:
                serl_data = {
                    "dest_name": user_input,
                    "dest_desc": chatbot_resp
                }
                serializer = DestSerializer(data = serl_data)
                if not serializer.is_valid():
                    print(serializer.errors)
                    return Response({'status': 403, 'message': serializer.errors})
                serializer.save()
                return Response({'status': 200, 'message': serializer.data})
        else:
            Response({'status': 200 ,"message":"Api key is not set"})
    else:
        Response({'status': 200 ,"message":"Please enter destination"})
    print(chatbot_resp)
    return Response(chatbot_resp,status=status.HTTP_200_OK)