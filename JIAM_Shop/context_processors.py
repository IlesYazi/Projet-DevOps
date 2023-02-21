
from store.models import Category


def all_category(request):
    categories = Category.objects.all()
    if categories:
        return {'categories': categories }
