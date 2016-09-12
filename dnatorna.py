""""Convert DNA sequences to RNA."""

def rna(seq):
    """Convert a DNA sequence to RNA."""

    #convert to uppercase
    seq=seq.upper()

    return seq.replace('T', 'U')
