from django.shortcuts import render
from django.http import HttpResponse
from .models import PhonesHandled


# Create your views here.


def comments_info(request):
    comments = PhonesHandled.objects.all()
    # return HttpResponse("Here is the comments_info view!")

    # 正向数量
    queryset = PhonesHandled.objects.values('sentiments')
    condtions = {'sentiments__gte': 0.5}
    plus = queryset.filter(**condtions).count()

    # 负向数量
    queryset = PhonesHandled.objects.values('sentiments')
    condtions = {'sentiments__lt': 0.5}
    minus = queryset.filter(**condtions).count()

    return render(request, 'result.html', locals())
