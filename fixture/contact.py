from selenium.webdriver.support.ui import Select


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

    def delete_first_contact(self):
        wd = self.app.wd
        # select first contact = click first checkbox
        self.select_first_contact()
        # submit contact deletion
        wd.find_element_by_css_selector("input[value='Delete']").click()
        # accept dialog window
        wd.switch_to_alert().accept()
        self.app.return_to_home_page()


    def select_first_contact(self):
        wd = self.app.wd
        # select first group = click first checkbox

        if not wd.current_url.endswith("/index.php") > 0:
            wd.find_element_by_link_text("home").click()

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
        self.change_field_value("address", contact.work_address)

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

    def edit_first_contact(self, new_contact_data):
        wd = self.app.wd
        self.select_first_contact_edit()
        # edit contact
        self.change_contact_info(new_contact_data)
        # submit contact edition
        wd.find_element_by_xpath("//input[@value='Update']").click()
        self.app.return_to_home_page()

    def select_first_contact_edit(self):
        wd = self.app.wd
        # init contact edition of first edit link
        wd.find_element_by_css_selector("img[src='icons/pencil.png']").click()

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
        self.select_first_contact()
        return len(wd.find_elements_by_name("selected[]"))