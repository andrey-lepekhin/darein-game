import random  # line:1
import numpy as np  # line:2
from collections import Counter  # line:3
from darwin_game.models.player import Action, Player, PlayerNumber, TurnResult  # line:4


class Clippy(Player):  # line:7
    name = "Clippy"  # line:8
    state = None  # line:9

    def make_turn(
        O00OO0OO0OOO00OO0,
        O0OO0O0O0O000O000: list[TurnResult],
        O0O0OOOO0000OO000: PlayerNumber,
    ) -> Action:  # line:13
        O000000000OOO0OOO = [
            O0000OOOO0OOO00O0.actions[O0O0OOOO0000OO000]
            for O0000OOOO0OOO00O0 in O0OO0O0O0O000O000
        ]  # line:15
        OOO0O0OO000OOO0OO = [
            O0O0OO00OOOOOOOOO.actions[1 - O0O0OOOO0000OO000]
            for O0O0OO00OOOOOOOOO in O0OO0O0O0O000O000
        ]  # line:16
        OOO0OOO00O0000O00 = len(O0OO0O0O0O000O000) + 1  # line:18
        if all(
            [O00OOO0O00OOO0OO0 in [2, 3] for O00OOO0O00OOO0OO0 in OOO0O0OO000OOO0OO]
        ):  # line:20
            if OOO0OOO00O0000O00 < 4:  # line:21
                O00OO0OO0OOO00OO0.state = "sub4"  # line:22
                return random.choice([2, 3])  # line:23
            if OOO0OOO00O0000O00 == 4:  # line:25
                O00OO0OO0OOO00OO0.state = "4"  # line:26
                if hash(str(O000000000OOO0OOO)) > hash(
                    str(OOO0O0OO000OOO0OO)
                ):  # line:27
                    return 3  # line:28
                else:  # line:29
                    return 2  # line:30
            if (OOO0OOO00O0000O00 > 4) and all(
                [
                    sum(OO00O0O0OO00000O0.actions) == 5
                    for OO00O0O0OO00000O0 in O0OO0O0O0O000O000[3:]
                ]
            ):  # line:33
                O00OO0OO0OOO00OO0.state = "post4"  # line:34
                if hash("clippy" + str(OOO0OOO00O0000O00)) % 2 == 0:  # line:35
                    return O000000000OOO0OOO[-1]  # line:36
                else:  # line:37
                    return OOO0O0OO000OOO0OO[-1]  # line:38
        if O000000000OOO0OOO[:-1] == OOO0O0OO000OOO0OO[1:]:  # line:40
            O00OO0OO0OOO00OO0.state = "mirror"  # line:41
            if O000000000OOO0OOO[-1] == 3:  # line:42
                return 5  # line:43
            if O000000000OOO0OOO[-1] == 5:  # line:44
                return 1  # line:45
            if O000000000OOO0OOO[-1] == 1:  # line:46
                return 0  # line:47
            if O000000000OOO0OOO[-1] == 0:  # line:48
                return 5  # line:49
        OOO00O00OO0OOOO0O = Counter(OOO0O0OO000OOO0OO[-10:])  # line:51
        OO00O00O0O000O0OO = 10  # line:52
        O0OO0OO0OOOOOO0OO = {
            OO0OOOO0OO000OO00: OOO00O00OO0OOOO0O.get(OO0OOOO0OO000OO00, 0)
            for OO0OOOO0OO000OO00 in range(6)
        }  # line:54
        O0O00OOOO00OOO000 = {
            OO00O00O0O0O0O0O0: OOO00OO000OOO0OO0 / OO00O00O0O000O0OO
            for OO00O00O0O0O0O0O0, OOO00OO000OOO0OO0 in O0OO0OO0OOOOOO0OO.items()
        }  # line:56
        O0OOO00OOOOOO00O0, O0OO0OO00000O0O0O = OOO00O00OO0OOOO0O.most_common(1)[
            0
        ]  # line:59
        OO0OO00O0O0O00000 = O0OO0OO00000O0O0O / OO00O00O0O000O0OO  # line:60
        if OO0OO00O0O0O00000 > 0.5 and O0OOO00OOOOOO00O0 < 3:  # line:62
            O00OO0OO0OOO00OO0.state = "bully"  # line:63
            return 5 - int(O0OOO00OOOOOO00O0)  # line:64
        O000O0OO0O0O00OOO = sum(
            [
                O00OOOOOO0OOO0000
                for OOOO0O00OOOOOOO0O, O00OOOOOO0OOO0000 in O0O00OOOO00OOO000.items()
                if OOOO0O00OOOOOOO0O < 3
            ]
        )  # line:66
        O00OO0OO0OOO00OO0.state = "halve_sub3"  # line:67
        if np.random.random() < (O000O0OO0O0O00OOO * 0.5):  # line:68
            return 2  # line:69
        else:  # line:70
            return 3  # line:71
