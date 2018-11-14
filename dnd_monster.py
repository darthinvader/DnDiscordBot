class DnDMonster:
    def __init__(self, monster_id, monster_name, initiative=-1):
        self.monster_id = monster_id
        self.monster_name = monster_name
        self.initiative = initiative

    def set_initiative(self, initiative):
        self.initiative = initiative

    def has_initiative(self):
        return self.initiative != -1

    def get_initiative(self):
        return self.initiative

    def get_name(self):
        return self.monster_name

    def get_id(self):
        return self.monster_id
