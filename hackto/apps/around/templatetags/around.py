from django import template
register = template.Library()

ICONS = {
    'movers': 'mover',
    'decorators': 'decorator',
    'insurance': 'insurance',
    'landscaping': 'lawn',
    'post offices': 'postal',
    'telcos': 'telephone',
    'banks': 'bank',
    'dry cleaners': 'dry cleaner',
    'grocery stores': 'grocery',
    'schools': 'school',
    'day cares': 'day care',
    'churches': 'church',
    'gas stations': 'gas station',
    'hospitals': 'hospital',
    'mechanics': 'mechanic',
    'restaurants': 'restaurant',
    'shopping': 'plaza',
    'hair dressers': 'hair',
    'pharmacy': 'pharmacy',
}

def do_icon(parser, token):
    try:
        # split_contents() knows not to split quoted strings.
        tag_name, category = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError("%r tag requires three arguments (Service Date, Departure Start Date, Departure End Date)" % token.contents.split()[0])
    return Icon(category)

class Icon(template.Node):
    def __init__(self, category):
        self.category = template.Variable(category)
        
    def render(self, context):
        category = self.category.resolve(context)

        return ICONS.get(category)

register.tag('icon', do_icon)