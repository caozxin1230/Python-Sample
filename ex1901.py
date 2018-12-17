def cheese_and_crackers(cheese_count,boxes_of_crackers):
    print "You have %d cheese!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket. \n"

print "OR, we can collect variables from users:"
amount_of_cheese=int(raw_input("enter the amount_of_cheese: "))
amount_of_crackers=int(raw_input("enter the amount_of_crackers: "))

cheese_and_crackers(amount_of_cheese,amount_of_crackers) 
