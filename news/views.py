from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    context = {
        'news_list':[
            {
                "title": "我正在探索到底应该学什么来找实习",
                "content": "目前看到的很多岗位基本都要求两类能力——web开发和数据库使用。",
            },
            {
                "title": "是选择数据库还是选择web？",
                "content": "数据库既可以python也可以java，web也是，我只是对python熟一些，感觉web好上手一点",
            }
        ]
    }
    
    return render(request, 'news/index.html', context)
