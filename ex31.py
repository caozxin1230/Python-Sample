print "You enter a dark room with two doors. Do you go through door #1 or door #2?"

door = raw_input("> ")

if door == "1":
    print "There's a giant bear here eating a cheese cake. What do you do?"
    print "1, Take the cake."
    print "2, Scream at the bear."

    bear = raw_input("> ")

    if bear == "1":
        print "The bear eats your face off. Good job!"
    elif bear =="2":
        print "The bear eats  your legs off. Good job!"
    else:
        print "Well, doing %s is probably better. Bear runs away." % bear
        print "\nAfter the bear run away, a elf comes to you through the %s door. " % bear
        print "\tHe asks: I have two pockets, which one you want?"
        print "\t1, a red pocket with a hen"
        print "\t2, a blue pocket with gold coins."

        pocket=raw_input("> ")

        if pocket == "1":
            print "After you come home, you found out the hen is a magic hen."
            print "The hen can make one golden egg everyday. Good job!"
        elif pocket=="2":
            print "After you spent all coins. You become a begger. Good job!"
        else:
            print "The elf said you are not a greedy people. He comes home with you."
            print "And becomes your servent. Good job!"

elif door == "2":
    print "You stare into the endless abyss at Cthulhu's retina."
    print "1. Blueberries."
    print "2, Yellow jacket clothespins."
    print "3, Understanding revolvers yelling melodies."

    insanity =raw_input("> ")

    if insanity =="1" or insanity == "2":
        print "Your body survives powered by a mind of jello. Good job!"
    else:
        print "The insanity rots your eyes into a pool of muck. Good job!"

else:
    print "You stumble around and fall on a knife and die. Good job!"
