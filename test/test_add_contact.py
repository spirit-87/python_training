# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)  # fixture destroy
    return fixture

def test_add_contact(app):
    app.session.login("admin", "secret")
    app.contact.create(Contact("fn", "mn", "ln", "nn", "t", "c", "address", "5", "6", "7", "8", "e1", "e2", "e3",
                               "www", "31", "May", "1234", "3", "July", "5678", "address", "6", "test"))
    app.session.logout()
