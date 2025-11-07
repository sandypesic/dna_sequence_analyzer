def get_complement(seq):
    """
    Return the complement of a DNA sequence
    Each nucleotide is replaced with its complement:
    - A <-> T
    - C <-> G
    Assume the input sequence contains only valid nucleotides (A/T/C/G)
    """

    complement_map = {"A": "T", "T": "A", "C": "G", "G": "C"}
    return "".join([complement_map[n] for n in seq])


def get_reverse_complement(seq):
    """
    Return the reverse complement of a DNA sequence:
    - Get the complement from get_complement
    - Reverse the string
    """
        
    return get_complement(seq)[::-1]
