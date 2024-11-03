# sample input :GATGGAACTTGACTACGTAAATT


input_dna = 'GATGGAACTTGACTACGTAAATT'
def Dna2rna(input_dna):
    result = input_dna.replace('T', 'U')
    return result

input_dna = 'GATGGAACTTGACTACGTAAATT'
Dna2rna(input_dna)

rst = Dna2rna(input_dna)
print(rst)



       




