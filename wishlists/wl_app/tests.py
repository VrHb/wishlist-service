import pytest

from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist


@pytest.mark.django_db
def test_create_and_check_user_in_db():
    User = get_user_model()
    User.objects.create(username='jack', password='some_pass')
    user_from_db = User.objects.filter(username='jack').exists()
    assert user_from_db


@pytest.mark.django_db
def test_raises_nonexist_object_exception():
    User = get_user_model()
    with pytest.raises(ObjectDoesNotExist):
        User.objects.get(username='viti_a')


@pytest.mark.django_db
@pytest.mark.parametrize("user_id", [999, 1000, 1001])
def test_nonexist_user_raises_exception(user_id):
    User = get_user_model()
    with pytest.raises(ObjectDoesNotExist):
        User.objects.get(id=user_id)

