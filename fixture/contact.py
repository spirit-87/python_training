from selenium.webdriver.support.ui import Select
from model.contact import Contact
import re


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_newcontact_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def create(self, contact):
        wd = self.app.wd
        self.open_newcontact_page()
        # fill in contact form
        self.change_contact_info(contact)
        # submit contact creation
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.app.return_to_home_page()

        self.contact_cashe = None

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

        self.contact_cashe = None

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        # select first contact = click first checkbox
        self.open_contacts_page()
        self.select_contact_by_index(index)
        # submit contact deletion
        wd.find_element_by_css_selector("input[value='Delete']").click()
        # accept dialog window
        wd.switch_to_alert().accept()
        self.app.return_to_home_page()

        self.contact_cashe = None

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        # select first contact = click first checkbox
        self.open_contacts_page()
        self.select_contact_by_id(id)
        # submit contact deletion
        wd.find_element_by_css_selector("input[value='Delete']").click()
        # accept dialog window
        wd.switch_to_alert().accept()
        self.app.return_to_home_page()

        self.contact_cashe = None

    def open_contacts_page(self):
        wd = self.app.wd
        # select first group = click first checkbox

        if not wd.current_url.endswith("/index.php") > 0:
            wd.find_element_by_link_text("home").click()

    def select_first_contact(self):
        self.select_contact_by_index(0)

    def select_contact_by_index(self, index):
        wd = self.app.wd
        # select first contact = click first checkbox
        wd.find_elements_by_name("selected[]")[index].click()

    def select_contact_by_id(self, id):
        wd = self.app.wd
        # select first contact = click first checkbox
        wd.find_element_by_css_selector("input[value='%s']" % id ).click()

    def change_contact_info(self, contact):
        wd = self.app.wd
        # fill in names of new contact
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)

        # fill in job information of new contact

        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)

        # fill in phones of new contact

        self.change_field_value("home", contact.phone_home)
        self.change_field_value("mobile", contact.phone_mobile)
        self.change_field_value("work", contact.phone_work)
        self.change_field_value("fax", contact.phone_fax)

        # fill in emails of new contact

        self.change_field_value("email", contact.email1)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)

        # fill in webpage of new contact
        self.change_field_value("homepage", contact.webpage)

        # fill in birth dates of new contact
        self.change_date_value("bday", contact.bday)
        self.change_date_value("bmonth", contact.bmonth)
        self.change_field_value("byear", contact.byear)

        # fill in anniversary dates of new contact
        self.change_date_value("aday", contact.aday)
        self.change_date_value("amonth", contact.amonth)
        self.change_field_value("ayear", contact.ayear)

        # fill in secondary info of new contact
        self.change_field_value("address2", contact.address2)
        self.change_field_value("phone2", contact.phone2)
        self.change_field_value("notes", contact.notes2)

        self.contact_cashe = None

    def edit_first_contact(self, new_contact_data):
        self.edit_contact_by_index(0)

    def edit_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        self.select_contact_edit_by_index(index)
        # edit contact
        self.change_contact_info(new_contact_data)
        # submit contact edition
        wd.find_element_by_xpath("//input[@value='Update']").click()
        self.app.return_to_home_page()

        self.contact_cashe = None

    def edit_contact_by_id(self, id, new_contact_data):
        wd = self.app.wd
        self.select_contact_edit_by_id(id)
        # edit contact
        self.change_contact_info(new_contact_data)
        # submit contact edition
        wd.find_element_by_xpath("//input[@value='Update']").click()
        self.app.return_to_home_page()

        self.contact_cashe = None

    def select_first_contact_edit(self):
        self.select_contact_by_index(0)

    def select_contact_edit_by_index(self, index):
        wd = self.app.wd
        self.app.return_to_home_page()
        # init contact edition of first edit link
        wd.find_elements_by_css_selector("img[src='icons/pencil.png']")[index].click()

    def select_contact_edit_by_id(self, id):
        wd = self.app.wd
        self.app.return_to_home_page()
        # init contact edition of first edit link
        wd.find_element_by_css_selector("a[href='edit.php?id=%s']" % id).click()

    def select_contact_view_by_index(self, index):
        wd = self.app.wd
        self.app.return_to_home_page()
        # init contact view of first edit link
        wd.find_elements_by_css_selector("img[src='icons/status_online.png']")[index].click()

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def change_date_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            Select(wd.find_element_by_name(field_name)).select_by_visible_text(text)

    def count(self):
        wd = self.app.wd
        self.open_contacts_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cashe = None

    def get_contact_list(self):
        if self.contact_cashe is None:
            wd = self.app.wd
            self.open_contacts_page()
            self.contact_cashe = []

            for row in wd.find_elements_by_name("entry"):
                cells = row.find_elements_by_tag_name("td")
                id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                lastname = cells[1].text
                firstname = cells[2].text
                address = cells[3].text
                all_emails = cells[4].text
                all_phones = cells[5].text

                self.contact_cashe.append(Contact(firstname=self.clear_extra_spaces(firstname), lastname=self.clear_extra_spaces(lastname), id=id,
                                                  address=self.clear_extra_spaces(address),
                                                  all_phones_from_home_page = all_phones,all_emails_from_home_page = all_emails))
            # mine decision
            # inputs = wd.find_elements_by_css_selector("#maintable .center input")
            # first_names = wd.find_elements_by_css_selector("#maintable td:nth-child(3)")
            # last_names = wd.find_elements_by_css_selector("#maintable td:nth-child(2)")
            # for i in range(0, len(inputs)):
            #     id = inputs[i].get_attribute("value")
            #     first_name = first_names[i].text
            #     last_name = last_names[i].text
            #     self.contact_cashe.append(Contact(firstname=first_name, lastname=last_name, id=id))

        return list(self.contact_cashe)

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.select_contact_edit_by_index(index)

        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")

        phone_home = wd.find_element_by_name("home").get_attribute("value")
        phone_mobile = wd.find_element_by_name("mobile").get_attribute("value")
        phone_work = wd.find_element_by_name("work").get_attribute("value")
        phone2 = wd.find_element_by_name("phone2").get_attribute("value")

        email1 = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")

        address = wd.find_element_by_name("address").text

        contact_edit = Contact(firstname=firstname, lastname=lastname, id=id, phone_home=phone_home, phone_mobile=phone_mobile,
                        phone_work=phone_work, phone2=phone2, email1 = email1, email2 = email2, email3 = email3, address = address)
        contact_edit.all_phones_from_home_page = self.merge_phones_like_on_home_page(contact_edit)
        contact_edit.all_emails_from_home_page = self.merge_emails_like_on_home_page(contact_edit)
        return contact_edit

    def get_contact_info_from_view_page(self, index):
        wd = self.app.wd
        self.select_contact_view_by_index(index)

        text = wd.find_element_by_id("content").text
        phone_home = re.search("H: (.*)", text).group(1)
        phone_mobile = re.search("M: (.*)", text).group(1)
        phone_work = re.search("W: (.*)", text).group(1)
        phone2 = re.search("P: (.*)", text).group(1)

        return Contact(phone_home=phone_home, phone_mobile=phone_mobile,
                         phone_work=phone_work, phone2=phone2)



    def clear_extra_spaces(self, s):
        return re.sub("  ", " ", s.strip())

    def clear(self, s):
        return re.sub("[() -]", "", s)

    def merge_phones_like_on_home_page(self, contact):
        #filter - удаляем элементы None, map - чистим контакты от лишних символов, filter - выбираем только не пустые значения
        return "\n".join(filter(lambda x: x != "",
                                map(lambda x: self.clear(x),
                                    filter(lambda x: x is not None,
                                           [contact.phone_home, contact.phone_mobile, contact.phone_work, contact.phone2]))))

    def merge_emails_like_on_home_page(self, contact):
    #filter - удаляем элементы None, map - чистим контакты от лишних символов, filter - выбираем только не пустые значения
        return "\n".join(filter(lambda x: x != "",
                                map(lambda x:self.clear(x),
                                    filter(lambda x: x is not None,
                                           [contact.email1, contact.email2, contact.email3]))))