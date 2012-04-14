from django.shortcuts import  render_to_response
from django.template import RequestContext
from django.conf import settings
from around.forms import SearchForm
import requests
import json
from libraries.yellow.yellowbetter import YellowBetterAPI
from libraries.yellow import yellowcache
# Create your views here.
def index(request):
    template_name = 'base.html'
    context = RequestContext(request)
    dict = {}
    dict['form'] = SearchForm()

    return render_to_response(
        template_name,
        dict,
        context,
    )

def search(request):
    template_name = 'search.html'
    context = RequestContext(request)
    dict = {}

    if request.POST:
        form = SearchForm(request.POST)
        if form.is_valid():
            address = form.cleaned_data['address']
            #api = YellowBetterAPI(api_key= '', where = address, uid='hackto2', test_mode=False)
            #dict['businesses'] = api.categoriesAndBusinesses()
            dict['businesses'] = yellowcache.getResults(address)
            dict['lat'],dict['lon'] = get_lat_long(address)
    else:
        form = SearchForm()

    dict['form'] = form
    return render_to_response(
        template_name,
        dict,
        context,
    )

def about(request):
    template_name = 'about.html'
    context = RequestContext(request)
    dict = {}

    return render_to_response(
        template_name,
        dict,
        context,
    )

def get_lat_long(address):
    base_url = 'http://maps.google.com/maps/geo'
    data = {'q': address, 'key': settings.MAPS_API_KEY}
    results = requests.get(base_url, params=data)

    results = json.loads(results.text)
    print results.get('Placemark')[0]
    lon = results.get('Placemark')[0]['Point']['coordinates'][0]
    lat = results.get('Placemark')[0]['Point']['coordinates'][1]
    return (lat,lon)
