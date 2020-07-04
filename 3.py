string = ["cat",  "tac"]
for i in string:
    for j in string:
        if len(i) == len(j) and i != j:
            for item in range(len(i)):
                for items in range(len(j)):
                    if i[item] == j[items]:
                        result = j
    print("The anagram of {} is:".format(i), result)