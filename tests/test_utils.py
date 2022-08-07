import pytest

from main.main import api_posts_page
from utils import get_posts_all

# Cписок ключей
correct_keys = {"poster_name", "poster_avatar", "pic", "content ", "views_count", "likes_count", "pk"}

def test_get_posts_all():
    res = api_posts_page()
    type() == list

    assert res.json.get == list, "возвращается не список"
    assert isinstance(res, list) == True
    assert correct_keys == res

# def test_get_posts_all():
#     res = get_posts_all()
#     assert res == res
