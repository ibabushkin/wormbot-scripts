#!/usr/bin/env python
import random
import sys

# Input a project with give arg followed by a short description,
# get one with get argument.
if len(sys.argv) > 2:
    if sys.argv[1] == "give":
        to_add = " ".join(sys.argv[2:])
        text = open("data/idea_box", "a")
        text.write("\n"+to_add)
        print "kthxbye!"
        text.close()
    else:
        print "Not enough content there!"
elif len(sys.argv) > 1:
    if sys.argv[1] == "get":
        text = open("data/idea_box", "r")
        line_text = filter(lambda x: x != "", text.readlines())
        print random.choice(line_text)
        print "Have fun coding this!"
        text.close()
    else:
        print "What do you want?" 
else:
    print "Not enough args!"
