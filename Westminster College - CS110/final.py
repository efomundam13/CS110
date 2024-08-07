#Programmer: Manny Fomundam
#Date: March 6, 2023
#Professor: John Bonomo

#Problem 1
def inside(s, t):
    for t in s:
        if s.contains(t):
            return True
        else:
             return False

#Problem 2
def set_ops(list1, list2):
    userInput = int(input('What do you want to do: \n 1. Union \n 2. Intersection \n 3. Difference'))

    newlist = {}
    if userInput == 1:
        newlist = list1 + list2
        return newlist
    elif userInput == 2:
        for i in list1:
            for j in list2:
                if list1[i] != list2[j]:
                    newlist = list1 + list2
                    return newlist
                else:
                    return newlist
            return newlist
    elif userInput == 3:
        for i in list1:
            for j in list2:
                if list1[i] == list2[j]:
                    list1.split(i)
                    list2.split(j)
                    newlist = list1 + list2
                    return newlist
                else:
                    return newlist
        return newlist
    else:
        return "Invalid Input"
                        
#Problem 3
        def longestWords(fname):
            d = {}
            with open(fname, 'r') as f:
                lines = f.readlines().lower()
                for word in lines:
                    count(len(words))
                    for i in words
                        if d[i] = len(words):
                            d[i] += words
                            return d
                        else:
                            return d
