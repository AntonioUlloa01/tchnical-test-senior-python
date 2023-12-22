
# import pytest
# import sys
# from io import StringIO
from app.services.product_order import products_order


# def test__not_found_product(capsys):

#     sys.stdout = StringIO()
#     products = {'apples': 10, 'banana': 5, 'orange': 8, 'grape': 15, 'kiwi': 3}
#     products_order(products)
#     out, err = capsys.readouterr()
#     sys.stdout = sys.__stdout__
#     assert 'found' in out


def test__not_found_product():

    products = {'apples': 10, 'banana': 5, 'orange': 8, 'grape': 15, 'kiwi': 3}
    result = products_order(products)
    assert 'found' in result


def test_not_enough_product():
    products = {'apple': 15, 'banana': 5, 'orange': 8, 'grape': 15, 'kiwi': 3}
    result = products_order(products)
    assert 'enough' in result


def test_complete_order():
    products = {'apple': 10, 'banana': 5, 'orange': 8, 'grape': 15, 'kiwi': 3}

    result = products_order(products)
    assert result is None
