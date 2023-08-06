from FileEntity import Entity
from datetime import date


class Contact(Entity):
    def __init__(
        self, name, last_name, tel, mail, street, ext, int, town, area, city, state
    ):
        super().__init__(type(self).__name__)
        self.name = name
        self.last_name = last_name
        self.tel = tel
        self.mail = mail
        self.street = street
        self.ext = ext
        self.int = int
        self.town = town
        self.area = area
        self.city = city
        self.state = state
        self.created_at = date.today().isoformat()
