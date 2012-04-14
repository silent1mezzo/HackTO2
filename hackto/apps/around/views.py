from django.shortcuts import  render_to_response
from django.template import RequestContext
from around.forms import SearchForm
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
