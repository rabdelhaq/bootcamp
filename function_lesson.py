def ratio (x,y):
    """The ratio of 'x' to 'y'."""
    return x/y

def answer_to_the_ultimate_question_of_life():
    """simpler program"""
    return 42

def complement_base(base, material='DNA'):
    """Return the Watson-Crick complement of a base"""
    if base in 'Aa':
        if material =='DNA':
            return 'T'
        elif material=='RNA':
            return 'U'
        else:
            raise RuntimeError('invalid material')
    elif base in 'TtUu':
        return 'A'
    elif base in 'Gg':
        return 'C'
    else:
        return 'G'

def reverse_complement(seq, material='DNA'):
    """Compute reverse complement of a nucleic acid sequence."""

    #Initialize empty string
    rev_comp=''

    #loop through and add new rev comp bases
    for base in reversed(seq):
        rev_comp += complement_base(base, material=material)

    return rev_comp
