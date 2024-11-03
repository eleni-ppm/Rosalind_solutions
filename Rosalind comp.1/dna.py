# sample input: AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC
input_DNA = 'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'

def NucleotideOccurences(input_DNA):
    result = []
    count = 0
    newvar = input_DNA
    newlist = []

    substring = 'A'
    c = newvar.count('A',0)
    result = print(c)
    newlist.append(c)

    substring = 'T'
    c = newvar.count('T',0)
    result = print(c)
    newlist.append(c)

    substring = 'G'
    c = newvar.count('G',0)
    result = print(c)
    newlist.append(c)

    substring = 'C'
    c = newvar.count('C',0)
    result = print(c)
    newlist.append(c)

    result = newlist

    return result

input_DNA = 'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'
NucleotideOccurences(input_DNA)


