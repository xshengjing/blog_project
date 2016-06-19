import logging
from django.shortcuts import render
from django.conf import settings
from django.core.paginator import Paginator, InvalidPage, PageNotAnInteger,EmptyPage
from models import *

logger = logging.getLogger('blog.views')
# Create your views here.

def global_setting(request):
    return {
        "SITE_NAME" : settings.SITE_NAME,
        "SITE_DESC" : settings.SITE_DESC,
    }

def index(request):
    try:
        #������Ϣ��ȡ���������ݣ�
        category_list = Category.objects.all()
        #������ݣ�ͬѧ���Լ���ɣ�
        #������������
        article_list = Article.objects.all()
        paginator = Paginator(article_list,10)
        try:
            page = int(request.GET.get('page',1))
            article_list = paginator.page(page)
        except(EmptyPage,InvalidPage,PageNotAnInteger):
            article_list = paginator.page(1)
    except Exception as e:
        logger.error(e)
    return render(request,'index.html',locals())
