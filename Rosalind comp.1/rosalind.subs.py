
string_1 = "GATATATGCATATACTT"
string_2 = 'ATAT'


def subs(string_1,string_2):
    loc = []
    for i in range(len(string_1)):
        if string_2 == string_1[i: i+len(string_2)]:
            loc.append(i+1)
    return loc

string_1 = "GATATATGCATATACTT"
string_2 = 'ATAT'
loc = subs(string_1, string_2)
for i in loc:
 print(i, end=" ")


    