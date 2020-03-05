class Contact:
    def __init__(self, firstname = None, middlename = None, lastname = None, nickname = None, title = None, company = None,
                    work_address = None, phone_home = None,
                    phone_mobile = None, phone_work = None, phone_fax = None, email1 = None, email2 = None, email3 = None,
                    webpage = None, bday = None, bmonth = None, byear = None, aday = None,
                    amonth = None, ayear = None, address2 = None, phone2 = None, notes2 = None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.work_address = work_address
        self.phone_home = phone_home
        self.phone_mobile = phone_mobile
        self.phone_work = phone_work
        self.phone_fax = phone_fax
        self.email1 = email1
        self.email2 = email2
        self.email3 = email3
        self.webpage = webpage
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
        self.aday = aday
        self.amonth = amonth
        self.ayear = ayear
        self.address2 = address2
        self.phone2 = phone2
        self.notes2 = notes2