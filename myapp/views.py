from django.http import HttpResponse, HttpResponsePermanentRedirect, HttpResponseRedirect, JsonResponse, HttpResponseNotFound
from django.shortcuts import render
from datetime import datetime
from django.core.handlers.wsgi import  WSGIRequest
# Create your views here.


all_posts_db = [
    {
        'title': 'Пост 1',
        'id': 1,
        'date_of_pub': datetime(2022, 10, 1),
        'likes': 10,
        'comments': ['efa', 'rgdgrd', 'grdg']
    },
    {
        'title': 'Пост 2',
        'id': 2,
        'date_of_pub': datetime(2022, 10, 15),
        'likes': 34,
        'comments': ['ilul', 'sef', 'w']
    },
    {
        'title': 'Пост 3',
        'id': 3,
        'date_of_pub': datetime(2022, 10, 2),
        'likes': 98,
        'comments': ['hfm', 'rdg', 'sebsr']
    },
    {
        'title': 'Пост 4',
        'id': 4,
        'date_of_pub': datetime(2022, 10, 6),
        'likes': 12,
        'comments': ['tfh', 'gyj', 'thths']
    },
]


f_str = "<h2>{id}. {title}</h2><p>{likes} лайков</p><p>Дата публикации: {date_of_pub}</p>"


def pop_posts(request: WSGIRequest):
    posts = sorted(all_posts_db, key=lambda item: item['likes'])[::-1][:2]
    return HttpResponse('<hr>'.join([ f_str.format(**i) for i in posts]))

def las_posts(request: WSGIRequest):
    posts = sorted(all_posts_db, key=lambda item: item['date_of_pub'])[::-1][:2]
    return HttpResponse('<hr>'.join([ f_str.format(**i) for i in posts]))

def all_posts(request: WSGIRequest):
    posts = all_posts_db
    return HttpResponse('<hr>'.join([ f_str.format(**i) for i in posts]))

def get_likes(request: WSGIRequest, post: int):
    post_obj = list(filter(lambda item: item['id']==post, all_posts_db))[0]
    return HttpResponse(post_obj['likes'])

def get_comments(request: WSGIRequest, post: int):
    post_obj = list(filter(lambda item: item['id']==post, all_posts_db))[0]
    return HttpResponse('<br>'.join(post_obj['comments']))

def get_login(request: WSGIRequest, login: str, password: str):
    return HttpResponse(f'{login}:{password}')

def get_access(request: WSGIRequest, login: str, password: str):
    if login == 'admin' and password == 'admin':
        return HttpResponse('Все норм')
    return HttpResponse(f'Не норм')

def temp_redirect(req: WSGIRequest):
    return HttpResponseRedirect('/about/')

def const_redirect(req: WSGIRequest):
    return HttpResponsePermanentRedirect('/contacts/')

def req_json(req: WSGIRequest):
    return JsonResponse(req.GET)

def not_found(req: WSGIRequest):
    return HttpResponseNotFound('Загрузка страницы была завершена ошибкой')

def set_cook(req: WSGIRequest, key, value):
    site = HttpResponse(f'{key}:{value}')
    site.set_cookie(key, value)
    return site

def get_cook(req: WSGIRequest, key):
    return HttpResponse(f'{key}:{req.COOKIES[key]}')
