def get_complement(seq):
    complement_map = {"A": "T", "T": "A", "C": "G", "G": "C"}
    return "".join([complement_map[n] for n in seq])


def get_reverse_complement(seq):
    return get_complement(seq)[::-1]
