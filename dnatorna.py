""""Convert DNA sequences to RNA."""

def rna(seq):
    """Convert a DNA sequence to RNA."""
    if seq==seq.upper():
        print ("this sequence is uppercase")
    else:
        print ("this sequence is lowercase") 

    #convert to uppercase
    seq=seq.upper()

    return seq.replace('T', 'U')
