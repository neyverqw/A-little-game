from django.http import HttpResponse

def index(request):
    line1 = '<h1 style="text-align: center">辛绍威的第一个网站</h1>'
    return HttpResponse(line1)
