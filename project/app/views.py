from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

# Create your views here.   
def dict(req):
    data={'name':'abc' ,'age':20}
    return JsonResponse(data)



def std(req):
    d={'name':'abc' , 'age':21 , 'place':'vkm'}
    return HttpResponse (d)

