from django.shortcuts import  render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from django.conf import settings
from around.forms import SearchForm
from django.views.decorators.csrf import csrf_exempt
import requests
import json

#BUSINESSES = {'schools': [{u'distance': u'0.4', u'name': u'Bishop Marrocco-Thomas Merton', u'Deal': None, u'address': {u'city': u'Toronto', u'pcode': u'M6P1A3', u'street': u'1515 Bloor St W', u'prov': u'ON'}, u'geoCode': {u'latitude': u'43.656857', u'longitude': u'-79.449874'}, u'type': u'REGULAR', u'id': u'5912827'}, {u'distance': u'0.4', u'name': u'Howard Jr PS', u'Deal': None, u'address': {u'city': u'Toronto', u'pcode': u'M6R1T2', u'street': u'30 Marmaduke St', u'prov': u'ON'}, u'geoCode': {u'latitude': u'43.650256', u'longitude': u'-79.451646'}, u'type': u'REGULAR', u'id': u'792847'}, {u'distance': u'0.4', u'name': u'Park Place LINC Centre', u'Deal': None, u'address': {u'city': u'Toronto', u'pcode': u'M6R1X7', u'street': u'2299 Dundas St W', u'prov': u'ON'}, u'geoCode': {u'latitude': u'43.655515', u'longitude': u'-79.452229'}, u'type': u'REGULAR', u'id': u'5896244'}, {u'distance': u'0.4', u'name': u'West Park Secondary School', u'Deal': None, u'address': {u'city': u'Toronto', u'pcode': u'M6P1A3', u'street': u'1515 Bloor St W', u'prov': u'ON'}, u'geoCode': {u'latitude': u'43.656857', u'longitude': u'-79.449874'}, u'type': u'REGULAR', u'id': u'5870112'}, {u'distance': u'0.5', u'name': u'Kikkawa College & Teaching Clinic', u'Deal': None, u'address': {u'city': u'Toronto', u'pcode': u'M6P4A9', u'street': u'2340 Dundas St W', u'prov': u'ON'}, u'geoCode': {u'latitude': u'43.656793', u'longitude': u'-79.45257'}, u'type': u'REGULAR', u'id': u'4141028'}, {u'distance': u'0.5', u'name': u'Kikkawa College & Teaching Clinic ICT Schools(www.ICTSchools.com)', u'Deal': None, u'address': {u'city': u'Toronto', u'pcode': u'M6P4A9', u'street': u'2340 Dundas St W', u'prov': u'ON'}, u'geoCode': {u'latitude': u'43.656793', u'longitude': u'-79.45257'}, u'type': u'REGULAR', u'id': u'5884405'}, {u'distance': u'0.5', u'name': u'Trebas Institute', u'Deal': None, u'address': {u'city': u'Toronto', u'pcode': u'M6P4A9', u'street': u'2340 Dundas St W', u'prov': u'ON'}, u'geoCode': {u'latitude': u'43.656793', u'longitude': u'-79.45257'}, u'type': u'REGULAR', u'id': u'3770146'}, {u'distance': u'0.6', u'name': u'Conseil scolaire de district catholique Centre-Sud', u'Deal': None, u'address': {u'city': u'Toronto', u'pcode': u'M6H3Y1', u'street': u'330 Lansdowne Ave', u'prov': u'ON'}, u'geoCode': {u'latitude': u'43.65286', u'longitude': u'-79.440749'}, u'type': u'REGULAR', u'id': u'7950019'}, {u'distance': u'0.8', u'name': u'Brock Jr PS', u'Deal': None, u'address': {u'city': u'Toronto', u'pcode': u'M6H3S4', u'street': u'93 Margueretta St', u'prov': u'ON'}, u'geoCode': {u'latitude': u'43.652835', u'longitude': u'-79.438094'}, u'type': u'REGULAR', u'id': u'2140157'}, {u'distance': u'0.8', u'name': u'High Park Gardens Montessori School', u'Deal': None, u'address': {u'city': u'Toronto', u'pcode': u'M6R1S8', u'street': u'35 High Park Gdns', u'prov': u'ON'}, u'geoCode': {u'latitude': u'43.649031', u'longitude': u'-79.456491'}, u'type': u'REGULAR', u'id': u'6262838'}], 'day cares': [{u'distance': u'0.4', u'name': u'West End Child Care Services', u'Deal': None, u'address': {u'city': u'Toronto', u'pcode': u'M6P3L4', u'street': u'1411 Bloor St W', u'prov': u'ON'}, u'geoCode': {u'latitude': u'43.657372', u'longitude': u'-79.447341'}, u'type': u'REGULAR', u'id': u'1702119'}, {u'distance': u'0.4', u'name': u'Candy Factory Child Care Center', u'Deal': None, u'address': {u'city': u'Toronto', u'pcode': u'M6P3L4', u'street': u'1411 Bloor St W', u'prov': u'ON'}, u'geoCode': {u'latitude': u'43.657372', u'longitude': u'-79.447341'}, u'type': u'REGULAR', u'id': u'299622'}, {u'distance': u'0.4', u'name': u"Howard Park Children's Centre", u'Deal': None, u'address': {u'city': u'Toronto', u'pcode': u'M6R1T2', u'street': u'30 Marmaduke St', u'prov': u'ON'}, u'geoCode': {u'latitude': u'43.650256', u'longitude': u'-79.451646'}, u'type': u'REGULAR', u'id': u'792885'}, {u'distance': u'0.6', u'name': u'Kids Zone Daycare', u'Deal': None, u'address': {u'city': u'Toronto', u'pcode': u'M6R1S6', u'street': u'76 Constance St', u'prov': u'ON'}, u'geoCode': {u'latitude': u'43.64907', u'longitude': u'-79.453577'}, u'type': u'REGULAR', u'id': u'3264800'}, {u'distance': u'0.8', u'name': u'Brock Early Learning Centre', u'Deal': None, u'address': {u'city': u'Toronto', u'pcode': u'M6H3S4', u'street': u'93 Margueretta St', u'prov': u'ON'}, u'geoCode': {u'latitude': u'43.652835', u'longitude': u'-79.438094'}, u'type': u'REGULAR', u'id': u'2140149'}, {u'distance': u'0.8', u'name': u'My School Co-Op Nursery', u'Deal': None, u'address': {u'city': u'Toronto', u'pcode': u'M6R1M2', u'street': u'116 Fermanagh Ave', u'prov': u'ON'}, u'geoCode': {u'latitude': u'43.646913', u'longitude': u'-79.446081'}, u'type': u'REGULAR', u'id': u'1104139'}, {u'distance': u'0.8', u'name': u'Network Child Care Service Of Metropolitan Toronto Inc', u'Deal': None, u'address': {u'city': u'Toronto', u'pcode': u'M6H3Y5', u'street': u'544 Lansdowne Ave', u'prov': u'ON'}, u'geoCode': {u'latitude': u'43.6595', u'longitude': u'-79.443129'}, u'type': u'REGULAR', u'id': u'2430614'}, {u'distance': u'0.8', u'name': u'Sunnyside Day Care', u'Deal': None, u'address': {u'city': u'Toronto', u'pcode': u'M6R1M4', u'street': u'10 High Park Blvd', u'prov': u'ON'}, u'geoCode': {u'latitude': u'43.646095', u'longitude': u'-79.45019'}, u'type': u'REGULAR', u'id': u'4015203'}, {u'distance': u'0.8', u'name': u'Sunshine Child Care Centre', u'Deal': None, u'address': {u'city': u'Toronto', u'pcode': u'M6R1M2', u'street': u'116 Fermanagh Ave', u'prov': u'ON'}, u'geoCode': {u'latitude': u'43.646913', u'longitude': u'-79.446081'}, u'type': u'REGULAR', u'id': u'1530181'}]}

from libraries.yellow.yellowbetter import YellowBetterAPI
from libraries.yellow import yellowcache
from libraries.twilio.test_sms import send_message
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
            dict['address'] = address
            #api = YellowBetterAPI(api_key= '', where = address, uid='hackto2', test_mode=False)
            #dict['businesses'] = api.categoriesAndBusinesses()
            dict['businesses'] = yellowcache.getResults(address)
            dict['lat'],dict['lon'] = get_lat_long(address)

            #dict['businesses'] = BUSINESSES
    else:
        form = SearchForm()

    dict['form'] = form
    return render_to_response(
        template_name,
        dict,
        context,
    )

def category(request, category):
    template_name = 'category.html'
    context = RequestContext(request)
    dict = {}
    form = SearchForm(request.GET)
    address = request.GET.get('address')
    dict['address'] = address
    dict['lat'],dict['lon'] = get_lat_long(address)
    dict['businesses'] = yellowcache.getResults(address)[category]
    dict['category'] = category
    dict['form'] = form
    return render_to_response(
        template_name,
        dict,
        context,
    )

def company(request, id):
    template_name = 'search.html'
    context = RequestContext(request)
    dict = {}
    form = SearchForm(request.GET)

    dict['lat'],dict['lon'] = get_lat_long(request.GET.get('address'))
    dict['form'] = form
    return render_to_response(
        template_name,
        dict,
        context,
    )

@csrf_exempt
def send_addresses(request):
    rdict = {'result': 'OK'}
    if request.POST:
        category = request.POST.get('category')
        address = request.POST.get('address')
        send_message(address, category)

    json_data = json.dumps(rdict, ensure_ascii=False)
    return HttpResponse(json_data, mimetype='application/javascript')

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

    lon = results.get('Placemark')[0]['Point']['coordinates'][0]
    lat = results.get('Placemark')[0]['Point']['coordinates'][1]
    return (lat,lon)
