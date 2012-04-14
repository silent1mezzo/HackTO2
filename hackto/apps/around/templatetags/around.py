from django import template
register = template.Library()

ICONS = {
    'movers': 'http://www.google.com/intl/en_us/mapfiles/ms/micons/red-dot.png',
    'decorator': 'http://www.google.com/intl/en_us/mapfiles/ms/micons/red-dot.png',
    'insurance': 'http://www.google.com/intl/en_us/mapfiles/ms/micons/red-dot.png',
    'lawn': 'http://www.google.com/intl/en_us/mapfiles/ms/micons/red-dot.png',
    'post offices': 'http://www.google.com/intl/en_us/mapfiles/ms/micons/red-dot.png',
    'telcos': 'http://127.0.0.1:8000/static/img/icons/telephone.png',
    'banks': 'http://127.0.0.1:8000/static/img/icons/bank.png',
    'dry cleaners': 'http://127.0.0.1:8000/static/img/icons/drycleaner.png',
    'grocery stores': 'http://127.0.0.1:8000/static/img/icons/grocery.png',
    'schools': 'http://127.0.0.1:8000/static/img/icons/school.png',
    'day cares': 'http://127.0.0.1:8000/static/img/icons/daycare.png',
    'churches': 'http://127.0.0.1:8000/static/img/icons/church.png',
    'gas stations': 'http://127.0.0.1:8000/static/img/icons/gasstation.png',
    'hospitals': 'http://127.0.0.1:8000/static/img/icons/hospital.png',
    'mechanics': 'http://127.0.0.1:8000/static/img/icons/mechanic.png',
    'restaurants': 'http://127.0.0.1:8000/static/img/icons/food.png',
    'shopping': 'http://127.0.0.1:8000/static/img/icons/plaza.png',
    'hair dressers': 'http://127.0.0.1:8000/static/img/icons/hair.png',
    'pharmacy': 'http://127.0.0.1:8000/static/img/icons/pharmacy.png',
    'default': 'http://www.google.com/intl/en_us/mapfiles/ms/micons/red-dot.png',
}


def do_icon(parser, token):
    try:
        # split_contents() knows not to split quoted strings.
        tag_name, category = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError("%r tag requires a category type" % token.contents.split()[0])
    return Icon(category)

class Icon(template.Node):
    def __init__(self, category):
        self.category = template.Variable(category)
        
    def render(self, context):
        category = self.category.resolve(context)
        path = ICONS.get(category, None)
        if path:
            return path
        else:
            return ICONS.get('default')

register.tag('icon', do_icon)