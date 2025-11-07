def clean_sequence(seq):
    """
    Clean a DNA sequence:
    - Convert to uppercase
    - Strip leading/trailing whitespace
    - Remove any invalid characters (keep only A/T/C/G)
    Return the cleaned sequence as a string
    """

    seq = seq.upper().strip()
    valid_nucleotides = {"A", "T", "C", "G"}
    return "".join([n for n in seq if n in valid_nucleotides])


def count_nucleotides(seq):
    """
    Count the occurrences of each nucleotide in a sequence
    Return a dictionary with keys 'A', 'T', 'C', 'G'
    """

    counts = {"A": 0, "T": 0, "C": 0, "G": 0}
    for nucleotide in seq:
        counts[nucleotide] += 1
    return counts


def calculate_gc_content(counts):
    """
    Calculate the percentage of G and C nucleotides
    Use the counts dictionary from count_nucleotides
    Return 0 if the total length is 0 to avoid division by zero
    """
     
    total = sum(counts.values())
    return ((counts["G"] + counts["C"]) / total) * 100 if total > 0 else 0


def calculate_at_content(counts):
    """
    Calculate the percentage of A and T nucleotides
    Use the counts dictionary from count_nucleotides
    Return 0 if the total length is 0 to avoid division by zero
    """
        
    total = sum(counts.values())
    return ((counts["A"] + counts["T"]) / total) * 100 if total > 0 else 0
