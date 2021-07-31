from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from urlshortner.models import UrlData, MaxStoreid
from django.core.exceptions import ObjectDoesNotExist
from infracloud_project import urls

@api_view(['GET'])
def shorten_url(request, original_url):
    final_short_url = None
    try:
        shorten_url = UrlData.objects.get(pk=original_url)
        encoded_url = getattr(shorten_url, 'encode')
        final_short_url = encoded_url
    except ObjectDoesNotExist:
        id_to_allote = fetch_max_id()
        encoded_url = encode(id_to_allote)
        new_url = UrlData(url=original_url, encode=str(encoded_url))
        new_url.save()
        update_max_field(id_to_allote)
        final_short_url = encoded_url
        
    data = {"url" : "tobedone/" + str(final_short_url)}
    return Response(data)

def fetch_max_id():
    maxidobject = MaxStoreid.objects.get()
    max_id = getattr(maxidobject, 'max_id')
    return max_id + 1

def update_max_field(new_id):
    maxidobject = MaxStoreid.objects.update(max_id = new_id)
    
def encode(id):
    # base 62 characters
    characters = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    base = len(characters)
    ret = []
    while id > 0:
        val = id % base  ## remainder
        ret.append(characters[val])
        id = id // base ## quotient
    return "".join(ret[::-1])

@api_view(['GET'])
def shorten_url_next(request, original_url):
    if original_url in urls.dict_hash:
        data = {"shorten_url" : "tobedone/"  + str(urls.dict_hash[original_url])}
        return Response(data)
    max_id_given = urls.max_id
    id_to_allocate = encode(max_id_given+1)
    urls.max_id = urls.max_id + 1
    urls.dict_hash[original_url] = id_to_allocate
    data = {"shorten_url" : "tobedone/"  + str(urls.dict_hash[original_url])}
    return Response(data)
