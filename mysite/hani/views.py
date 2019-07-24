from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
import json
from .models import *
import requests
import os,sys
# Create your views here.
@csrf_exempt
def api(request):
	jsob={}
	log=[]
	if request.method == "POST":
		try:
			data = request.POST["data"]
			received = json.loads(data)
			jsob.update(received)

			cityname = jsob["cityname"]
			

			url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid=c9ba4c2460210fd1b8a75eb000c65d12".format(cityname)
			response = requests.get(url).text
			dic = {}
			dic = json.loads(response)
			return JsonResponse("Weather: %s" %  dic.get('weather'),safe=False)
			

		except Exception as e:
			exc_type, exc_obj, exc_tb = sys.exc_info()
			other = sys.exc_info()[0].__name__
			fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
			errorType = str(exc_type)
			return JsonResponse({"isError": True, "error":str(e), "errorType":errorType, "function":fname, "line":exc_tb.tb_lineno, "log":log})
	else:
		return HttpResponse("<h1>ONLY POST REQUESTS</h1>")