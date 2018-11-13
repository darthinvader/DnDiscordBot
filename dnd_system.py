import dnd_player


class DnDSystem:
    def __init__(self):
        self.players = dict()

    def set_player_initiative_name(self, name_id, name, initiative):

        flag = not name_id in self.players
        if flag:
            self.players[name_id] = dnd_player.DnDPlayer(name_id, name, initiative)
            return 'Set initiative to ' + name, 0

        player = self.players[name_id]
        if player.has_initiative():
            return 'player has already rolled', 1

        player.set_initiative(initiative)
        return 'Set initiative to ' + name, 0

    def get_all_initiatives(self):
        inits = list()
        for p in self.players:
            player = self.players[p]
            inits.append((player.get_name(), player.get_initiative()))
        return inits

    def make_inits_embeds(self, inits):
        inits = self.get_all_initiatives()

    def clear_inits(self):
        for p in self.players:
            player = self.players[p]
            player.set_initiative(-1)
