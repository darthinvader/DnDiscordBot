import dnd_player
import dnd_monster
import embed_creator as ec

class DnDSystem:
    def __init__(self):
        self.players = dict()
        self.monsters = dict()
        self.monster_id = 0

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

    def set_monster_initiative(self, monster_name, initiative):
        self.monsters[self.monster_id] = dnd_monster.DnDMonster(self.monster_id, monster_name, initiative)
        self.monster_id +=1

    def get_all_initiatives(self):
        inits = list()
        for p in self.players:
            player = self.players[p]
            inits.append((player.get_name(), player.get_initiative()))
        for m in self.monsters:
            monster = self.monsters[m]
            inits.append((monster.get_name(), monster.get_initiative()))
        return inits

    def get_all_initiatives_in_order_embed(self):
        inits = self.get_all_initiatives()
        sort_inits = sorted(inits, key=lambda x: x[1], reverse=True)
        embed = ec.initiative_sorted_embed(sort_inits)
        return embed


    def make_inits_embeds(self, inits):
        inits = self.get_all_initiatives()

    def clear_inits(self):
        for p in self.players:
            player = self.players[p]
            player.set_initiative(-1)
        self.monsters = dict()
        self.monster_id = 0