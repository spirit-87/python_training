# -*- coding: utf-8 -*-
import pytest
from contact import Contact
from application_c import Application_c
   

@pytest.fixture
def app_c(request):
    fixture = Application_c()
    request.addfinalizer(fixture.destroy)  # fixture destroy
    return fixture

def test_add_contact(app_c):
    app_c.login("admin", "secret")
    app_c.create_contact(Contact("fn", "mn", "ln", "nn", "t", "c", "address", "5", "6", "7", "8", "e1", "e2", "e3",
                               "www", "31", "May", "1234", "3", "July", "5678", "address", "6", "test"))
    app_c.logout()
