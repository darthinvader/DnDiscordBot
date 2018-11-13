class DnDPlayer:
    def __init__(self, name_id, name, initiative=-1):
        self.id = name_id
        self.name = name
        self.initiative = initiative

    def set_initiative(self, initiative):
        self.initiative = initiative

    def has_initiative(self):
        return self.initiative != -1

    def get_initiative(self):
        return self.initiative

    def get_name(self):
        return self.name

    def get_id(self):
        return self.id
