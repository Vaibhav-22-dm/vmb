import pytest
from django.urls import reverse
from vmb.users.forms import UserCreationForm
from django.contrib.auth import get_user_model
from allauth.account.models import EmailAddress
from tos.models import *
from vmb.matrimony.models.profiles import *
import datetime
from vmb.matrimony.tests.factories import *

pytestmark = pytest.mark.django_db

def test_in_index_view(client):

    # Without Login

    response = client.get(reverse('matrimony:index'), follow=True)

    assert response.status_code == 200
    assert 'account/login.html' in (t.name for t in response.templates)

    # With Login

    user = UserCustomFactory()
    profile = MatrimonyFactory(user=user, profile_id=user.username)
    EmailAddress.objects.create(user=profile.user, email=profile.user.email, primary=True, verified=True)
    tos = TermsOfService.objects.create(active=True, content="This is the new TOS.")
    UserAgreement.objects.create(user=profile.user,terms_of_service=tos)

    client.login(username=user.username, password='wordpass123')
    response = client.get(reverse('matrimony:index'), follow=True)

    assert response.status_code == 200
    assert 'matrimony/profile_edit.html' in (t.name for t in response.templates)



    