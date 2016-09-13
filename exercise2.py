
#Question 2.2

#opening fasta file
f=open('data/salmonella_spi1_region.fna', 'r')
my_file=f.read()

#storing sequence as a string with no gaps
sequences=[]
with open ('data/salmonella_spi1_region.fna', 'r') as f:
    sequence=""
    for line in f:
        if line.startswith('>'):
            sequences.append(line)
        else:
            sequence +=line.rstrip('\n')
    print (sequence)


#Question 2.3a

def gc_blocks(seq,block_size):
    """function that divides a sequence into blocks and returns GC content"""
    seq=seq.upper()
    n=block_size
    x=(len(seq)-(n-1))
    new_seq=[seq[i:i+n] for i in range(0, x, block_size)]
    print (new_seq)

    gc_count=()
    #count number of Gs and Cs in each block and convert to tuple
    for item in new_seq:
        gc_count +=tuple(str(item.count('G')+item.count('C')))

    #print (gc_count)

    #converting strings in my tuple to integers
    gc_count_int=tuple(map(int,gc_count))
    print (gc_count_int)


    gc_content=tuple(i/n for i in gc_count_int)
    print (gc_content)




#Question 2.3b
def gc_map(seq,block_size, gc_thresh):
    """function where every base in block is in lower case if 'GC'
    threshold is not met"""

    n=block_size
    x=(len(seq)-(n-1))
    new_seq=[seq[i:i+n] for i in range(0, x, block_size)]
    print (new_seq)

    new_seq_copy=new_seq

    gc_count=()
    #count number of Gs and Cs in each block and convert to tuple
    for item in new_seq:
        gc_count +=tuple(str(item.count('G')+item.count('C')))

    #print (gc_count)

    #converting strings in my tuple to integers
    gc_count_int=tuple(map(int,gc_count))
    print (gc_count_int)


    gc_content=tuple(i/n for i in gc_count_int)
    print (gc_content)

    #separate blocks of bases into separate tuples to evaluate if GC level
    #is above threshold

    #zip to correlate gc_content with gc_thresh and block bases

    for new_seq_copy, gc_content, in zip(new_seq_copy,gc_content):
        seq3= new_seq_copy, gc_content
        print (seq3)


    for block in new_seq:
        if gc_content >= gc_thresh:
            print (block.upper())
    for block in new_seq:
        if gc_content <= gc_thresh:
            print (block.lower())


#Question 2.3c-done, dont need to write coded
    #code: gc_blocks(sequence, 1000)


#Question 2.4a
def longest_orf(sequence):
    """function that takes a DNA sequnce and finds the longest open reading frame
    ORF"""
    
