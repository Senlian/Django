#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def paginator(request, articles):
    paginator = Paginator(articles, 10, 1)
    cur_page_number = int(request.GET.get('page', 1))
    if cur_page_number < 6:
        if paginator.num_pages <= 10:
            pages = range(1, paginator.num_pages + 1)
        else:
            pages = range(1, 11)
    elif (cur_page_number >= 6) and (cur_page_number <= paginator.num_pages - 5):
        pages = range(cur_page_number - 5, cur_page_number + 5)
    else:
        pages = range(paginator.num_pages - 9, paginator.num_pages + 1)

    try:
        cur_page = paginator.page(cur_page_number)
        articles = cur_page.object_list
    except PageNotAnInteger:
        cur_page = paginator.page(1)
        articles = cur_page.object_list
    except EmptyPage:
        cur_page = paginator.page(paginator.num_pages)
        articles = cur_page.object_list
    finally:
        return {'articles': articles, 'page': cur_page, 'num_pages': paginator.num_pages, 'pages': pages}
