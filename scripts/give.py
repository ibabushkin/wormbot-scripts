#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

# the items we want
items = {"herpes": "I'm sorry... I need to make a confession to you, NICK.",
         "register": "NICK: Go figure it out yourself, you moron!",
         "facebook":
         "NICK: We are not your private squad, nor do we want to grow skids.",
         "fuck": "NICK, look how many fucks I give: none.",
         "dick": "NICK, come here, you are ready for the dick now.",
         "aids": "NICK, now you carry a stigma in 70% of the world"
         }

if __name__ == "__main__":
    if len(sys.argv) == 3:
        nick = sys.argv[1]
        item = sys.argv[2]
        if item in items:
            print(items[item].replace("NICK", nick))
        else:
            print("No such item! Maybe suggest it's addition using :suggest.")
    else:
        s = "Items: "
        for item in items:
            s += item + ", "
        print(s[:-2])
