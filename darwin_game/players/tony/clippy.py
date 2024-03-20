import random  # line:1
import numpy as np  # line:2
from collections import Counter  # line:3
from darwin_game.models.player import Action, Player, PlayerNumber, TurnResult  # line:4


class Clippy(Player):  # line:7
    name = "Clippy"  # line:8

    def make_turn(
        O0OOO0OOOOO00OOO0,
        O00O0OOO000O00000: list[TurnResult],
        OOOO00OO000OO0OOO: PlayerNumber,
    ) -> Action:  # line:12
        OOO0000OO000O00O0 = [
            O00OO0O0000000000.actions[OOOO00OO000OO0OOO]
            for O00OO0O0000000000 in O00O0OOO000O00000
        ]  # line:14
        OO0O00O0O000O0OOO = [
            O0OOOOOO000OOOOOO.actions[1 - OOOO00OO000OO0OOO]
            for O0OOOOOO000OOOOOO in O00O0OOO000O00000
        ]  # line:15
        OOOOOO00O00OO0OO0 = len(O00O0OOO000O00000)  # line:17
        if OOOOOO00O00OO0OO0 < 3:  # line:19
            return random.choice([2, 3])  # line:20
        O00OO0OOOOO00O000 = all(
            [
                OOOOOO0000O0O0OOO in [2, 3]
                for OOOOOO0000O0O0OOO in OO0O00O0O000O0OOO[-3:]
            ]
        )  # line:22
        if OOOOOO00O00OO0OO0 < 7 and O00OO0OOOOO00O000:  # line:25
            if OOO0000OO000O00O0[-1] == 3 and OO0O00O0O000O0OOO[-1] == 2:  # line:26
                return 2  # line:27
            elif OOO0000OO000O00O0[-1] == 2 and OO0O00O0O000O0OOO[-1] == 3:  # line:29
                return 3  # line:30
            else:  # line:32
                return random.choice([2, 3])  # line:33
        if O00OO0OOOOO00O000:  # line:36
            if OOOOOO00O00OO0OO0 == 7:  # line:37
                if (
                    OOO0000OO000O00O0[-1] == OO0O00O0O000O0OOO[-2]
                    and OOO0000OO000O00O0[-2] == OO0O00O0O000O0OOO[-3]
                ):  # line:41
                    return OOO0000OO000O00O0[-1]  # line:42
            if OOOOOO00O00OO0OO0 == 8:  # line:44
                if (
                    OOO0000OO000O00O0[-1] == OOO0000OO000O00O0[-2]
                    and OO0O00O0O000O0OOO[-1] == OO0O00O0O000O0OOO[-2]
                    and OOO0000OO000O00O0[-2] == OO0O00O0O000O0OOO[-3]
                ):  # line:49
                    return OO0O00O0O000O0OOO[-1]  # line:50
            O0O000OOOOO0O0000 = (
                OO0O00O0O000O0OOO[-1] == OO0O00O0O000O0OOO[-2]
                and OO0O00O0O000O0OOO[-2] != OO0O00O0O000O0OOO[-3]
            )  # line:55
            OO0OOOOOO0O0O0O0O = (
                OO0O00O0O000O0OOO[-1] != OO0O00O0O000O0OOO[-2]
                and OO0O00O0O000O0OOO[-2] == OO0O00O0O000O0OOO[-3]
            )  # line:59
            if O0O000OOOOO0O0000:  # line:61
                return OO0O00O0O000O0OOO[-1]  # line:62
            if OO0OOOOOO0O0O0O0O:  # line:64
                return OOO0000OO000O00O0[-1]  # line:65
        if OOO0000OO000O00O0[-6:-1] == OO0O00O0O000O0OOO[-5:]:  # line:67
            if OOO0000OO000O00O0[-1] == 3:  # line:68
                return 5  # line:69
            if OOO0000OO000O00O0[-1] == 5:  # line:70
                return 1  # line:71
            if OOO0000OO000O00O0[-1] == 1:  # line:72
                return 0  # line:73
            if OOO0000OO000O00O0[-1] == 0:  # line:74
                return 5  # line:75
        if all(
            [O00000000O0O000OO == 2 for O00000000O0O000OO in OO0O00O0O000O0OOO[-5:]]
        ):  # line:77
            return 3  # line:78
        O0OO00OOOO0O0O0OO = Counter(OO0O00O0O000O0OOO)  # line:80
        O000OOOOOOOOOO0O0 = len(OO0O00O0O000O0OOO)  # line:81
        O0OO0OOOOOO0000O0 = {
            OO0O00O0O000OOOOO: O0OO00OOOO0O0O0OO.get(OO0O00O0O000OOOOO, 0)
            for OO0O00O0O000OOOOO in range(6)
        }  # line:83
        OO00OOO0O0O0O0OOO = {
            OOO00O0O0O0OO0OO0: OOO0O000O00OOO0OO / O000OOOOOOOOOO0O0
            for OOO00O0O0O0OO0OO0, OOO0O000O00OOO0OO in O0OO0OOOOOO0000O0.items()
        }  # line:85
        O00OO00O00O0O00OO, OO0OOOO0O00O00O0O = O0OO00OOOO0O0O0OO.most_common(1)[
            0
        ]  # line:88
        OO0O00OO0O0OOO00O = OO0OOOO0O00O00O0O / O000OOOOOOOOOO0O0  # line:89
        OOO000OOOOO0OO00O = sum(
            OO00OOO0O0O0O0OOO[OO0OO0OOO000000OO] for OO0OO0OOO000000OO in range(3)
        )  # line:92
        if OO0O00OO0O0OOO00O > 0.5 and O00OO00O00O0O00OO < 3:  # line:94
            return 5 - int(O00OO00O00O0O00OO)  # line:95
        if OOO000OOOOO0OO00O > 0.5:  # line:97
            return 3  # line:98
        if np.random.random() > 0.66:  # line:100
            return 2  # line:101
        else:  # line:102
            return 3  # line:103
