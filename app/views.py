from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from app import models

class get_data(APIView):


    def get(self,request):

        # ret = request.COOKIES.get('age')
        ret = request.get_signed_cookie('age',salt='lllll')
        print(ret)

        return Response(ret)

    def post(self,request):

        res = Response("success")
        res.set_cookie("username", "cox",)
        res.set_signed_cookie("age", "10",salt="lllll")
        return res
