from django.db.models import Count

from project.models import *


def list_produkt():
    product = Product.objects.all()
    products_with_lesson_count = Product.objects.annotate(
        lesson_count=Count('lesson_product')
    )
    result_data = []

    for product in products_with_lesson_count:
        product_data = {
            'id': product.id,
            'Имя курса': product.name_product,
            'Дата начала': product.start_date_time_product,
            'Цена': product.price_product,
            'Кол-во курсов': product.lesson_count,
        }
        result_data.append(product_data)

    return result_data


def list_lesson():

    pass
