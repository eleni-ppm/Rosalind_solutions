from collections import Counter

# Define the sequences
string_1 = ">Rosalind_6404\nCCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCCTCCCACTAATAATTCTGAGG"
string_2 = ">Rosalind_5959\nCCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCTATATCCATTTGTCAGCAGACACGC"
string_3 = ">Rosalind_0808\nCCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGACTGGGAACCTGCGGGCAGTAGGTGGAAT"

# Combine the sequences into a list
strings = [string_1, string_2, string_3]

def gc_content(strings):
    gc_contents = {}
    
    for entry in strings:
        header, sequence = entry.split("\n")
        sequence = sequence.strip()  # Remove any surrounding whitespace
        gc_count = sequence.count("G") + sequence.count("C")
        gc_content_value = gc_count / len(sequence) * 100
        gc_contents[header] = gc_content_value
    
    # Sort the dictionary by GC content in descending order
    highest_gc = sorted(gc_contents.items(), key=lambda x: x[1], reverse=True)[0]
    return highest_gc

# Get the sequence with the highest GC content
result = gc_content(strings)
print(result)




