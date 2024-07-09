# data structure for guests -- will i need it? who knows?

def reference(id):
    pass


class Guest:
    def __init__(self, guest_name, guest_email):
        self.name = guest_name
        self.email = guest_email
        self.id = None
        self.is_speaker = False
        self.access = True

    # getter methods
    def get_name(self):
        return self.name

    def get_email(self):
        return self.email

    def get_id(self):
        return self.id

    def is_speaker(self):
        return self.is_speaker

    def get_access(self):
        return self.access

    # setter methods
    def set_id(self, id):
        self.id = id

    def set_is_speaker(self, is_speaker):
        self.is_speaker = is_speaker

    def set_access(self, access):
        self.access = access
