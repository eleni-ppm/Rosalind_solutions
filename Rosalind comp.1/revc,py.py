my_string = 'AAAACCCGGT'

def DNAstrand(my_string):
    strand = ""
    for i in my_string[::-1]:
        if i == "A":
            strand += "T"
        if i == "T":
            strand += "A"
        if i == "C":
            strand += "G"
        if i == "G":
            strand += "C"
    return strand

strand = DNAstrand(my_string)
print(strand)

my_string = 'AAAACCCGGT'
DNAstrand(strand)