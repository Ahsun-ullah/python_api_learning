from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def testing_first(req):
    api_value = {'value':'api is not working fine'}
    for_loor = {'value':['ami','tumi','baccha']}
    return render(req,'api_learning/hello.html',context=for_loor)
