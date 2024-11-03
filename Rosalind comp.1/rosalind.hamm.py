def hamm(string1, string2):
    distance = 0
    assert len(string1) == len(string2)
    for i in range(len(string1)):
        if string1[i] != string2[i]:
            distance += 1
    return distance

string1 = 'GAGCCTACTAACGGGAT'
string2 = 'CATCGTAATGACGGCCT'

print(hamm(string1, string2))