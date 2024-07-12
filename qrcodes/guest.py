# data structure for guests -- will i need it? who knows? I don't need it actually

def reference(id, guests):
    for guest in guests:
        if guest.get_id == id:
            return guest
    return 1


class Guest:
    def __init__(self, guest_name, guest_email):
        self.name = guest_name
        self.email = guest_email
        self.id = None
        self.is_speaker = False
        self.access = True
        self.arrived = False

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

    def get_arrived(self):
        return self.arrived

    # setter methods
    def set_id(self, id):
        self.id = id

    def set_is_speaker(self, is_speaker):
        self.is_speaker = is_speaker

    def set_access(self, access):
        self.access = access
