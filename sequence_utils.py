def clean_sequence(seq):
    seq = seq.upper().strip()
    valid_nucleotides = {"A", "T", "C", "G"}
    return "".join([n for n in seq if n in valid_nucleotides])


def count_nucleotides(seq):
    counts = {"A": 0, "T": 0, "C": 0, "G": 0}
    for nucleotide in seq:
        counts[nucleotide] += 1
    return counts


def calculate_gc_content(counts):
    total = sum(counts.values())
    return ((counts["G"] + counts["C"]) / total) * 100 if total > 0 else 0


def calculate_at_content(counts):
    total = sum(counts.values())
    return ((counts["A"] + counts["T"]) / total) * 100 if total > 0 else 0