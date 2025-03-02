import abc

from game import Game


class Volume(metaclass=abc.ABCMeta):
    VOLUME = Game.VOLUME
    AUDIO = {"music": VOLUME, "game": VOLUME}

    # DON'T USE THIS METHOD FOR SET VOLUME !!!
    @staticmethod
    def update_volume(v):
        Volume.update_game(v)
        Volume.update_music(v)

    @staticmethod
    def update_music(mv):
        for music in Game.MUSICS:
            Game.MUSICS[music].set_volume(mv)

    @staticmethod
    def update_game(mv):
        for game in Game.GAME_SONG:
            Game.GAME_SONG[game].set_volume(mv)

    @staticmethod
    def set_volume(v: float):
        Volume.VOLUME = v
        Volume.sync_music_and_game_volume()
        Volume.update_volume(Volume.VOLUME)

    @staticmethod
    def sync_music_and_game_volume():
        # Verify if music no more that volume
        if Volume.VOLUME < Volume.AUDIO["music"]:
            Volume.set_music(Volume.VOLUME)
        if Volume.VOLUME < Volume.AUDIO["game"]:
            Volume.set_game(Volume.VOLUME)

    @staticmethod
    def increase_volume(nv):
        Volume.VOLUME += nv
        Volume.adjust_music_volume(nv)
        Volume.adjust_game_volume(nv)

    @staticmethod
    def adjust_music_volume(nv):
        if Volume.AUDIO["music"] - nv < 0:
            Volume.AUDIO["music"] = 0
        elif Volume.AUDIO["music"] + nv > 1:
            Volume.AUDIO["music"] = 1
        else:
            Volume.AUDIO["music"] -= nv
        Volume.update_music(Volume.AUDIO["music"])

    @staticmethod
    def adjust_game_volume(nv):
        if Volume.AUDIO["game"] - nv < 0:
            Volume.AUDIO["game"] = 0
        elif Volume.AUDIO["game"] + nv > 1:
            Volume.AUDIO["game"] = 1
        else:
            Volume.AUDIO["game"] -= nv
        Volume.update_game(Volume.AUDIO["game"])

    @staticmethod
    def reduce_volume(nv):
        Volume.VOLUME -= nv
        Volume.adjust_music_volume(nv)
        Volume.adjust_game_volume(nv)
        Volume.sync_music_and_game_volume()

    @staticmethod
    def mute():
        Volume.VOLUME = 0
        Volume.sync_music_and_game_volume()
        Volume.update_volume(Volume.VOLUME)

    @staticmethod
    def set_music(m):
        Volume.AUDIO["music"] = m
        Volume.sync_music_and_game_volume()
        Volume.update_music(Volume.AUDIO["music"])

    @staticmethod
    def increase_music(nm):
        Volume.AUDIO["music"] += nm
        Volume.sync_music_and_game_volume()
        Volume.update_music(Volume.AUDIO["music"])

    @staticmethod
    def reduce_music(nm):
        Volume.AUDIO["music"] -= nm
        Volume.update_music(Volume.AUDIO["music"])

    @staticmethod
    def mute_music():
        Volume.AUDIO["music"] = 0
        Volume.update_music(Volume.AUDIO["music"])

    @staticmethod
    def set_game(g):
        Volume.AUDIO["game"] = g
        Volume.sync_music_and_game_volume()
        Volume.update_game(Volume.AUDIO["game"])

    @staticmethod
    def increase_game(ng):
        Volume.AUDIO["game"] += ng
        Volume.sync_music_and_game_volume()
        Volume.update_game(Volume.AUDIO["game"])

    @staticmethod
    def reduce_game(ng):
        Volume.AUDIO["game"] -= ng
        Volume.update_game(Volume.AUDIO["game"])

    @staticmethod
    def mute_game():
        Volume.AUDIO["game"] = 0
        Volume.update_game(Volume.AUDIO["game"])

    @staticmethod
    def get_volume():
        return Volume.VOLUME

    @staticmethod
    def get_music():
        return Volume.AUDIO["music"]

    @staticmethod
    def get_game():
        return Volume.AUDIO["game"]