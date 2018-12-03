graph1 = {"A" : "X", "B" : "Y", "C" : "Z"}
graph2 = {"A" : "X", "B" : [], "C" : "Z"}
graph3 = {"A" : "X", "B" : [], "C" : []}

pref1 = {"X" : ["A", "B", "C"], "Y" : ["A", "C", "B"], "Z" : ["C", "A", "B"]}
pref2 = {"A" : ["X", "Y", "Z"], "B" : ["Y", "X", "Z"], "C" : ["Z", "X", "Y"]}

def matched(dic):
    for key, value in dic.items():
        if value == []:
            return False
    return True

def find_match(dic, fam):
    for key, value in dic.items():
        if value == fam:
            return key
    return []

def switch(pref, dog, fam, cur_dog):
    return pref[fam].index(dog) < pref[fam].index(cur_dog)

def stable(pref1, pref2):
    dic = {}
    for p1, prefs1 in pref1.items():
        i = 0
        for key, value in dic:
            if value == prefs1:
                if condition:
                    pass
                i++
        dic[p1] = prefs1.pop(i)



print(matched(graph1), matched(graph2))
print(find_match(graph1, "Z"), find_match(graph2, "X"), find_match(graph2, "Y"))
print(switch(pref1, "A", "X", "C"), switch(pref1, "B", "Y", "A"))
