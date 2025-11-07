from sequence_utils import clean_sequence, count_nucleotides, calculate_gc_content, calculate_at_content
from complement_utils import get_complement, get_reverse_complement
from visualize import plot_nucleotide_frequencies


def analyze_sequence(seq, label="Sequence"):
    """
    Analyze a DNA sequence:
    - Clean the sequence (remove invalid characters, make uppercase)
    - Count nucleotides (A/T/C/G)
    - Calculate GC and AT content
    - Generate complement and reverse complement
    - Plot nucleotide frequencies
    - Return a dictionary of results for CSV export
    """

    # Clean sequence and count nucleotides
    seq = clean_sequence(seq)
    counts = count_nucleotides(seq)
    total_length = sum(counts.values())

    # If sequence has no valid nucleotides, print message and return None
    if total_length == 0:
        print(f"\n{label}: No valid nucleotides found.")
        return None

    # Calculate content and complements
    gc_content = calculate_gc_content(counts)
    at_content = calculate_at_content(counts)
    complement = get_complement(seq)
    reverse_complement = get_reverse_complement(seq)

    # Print results to terminal
    print(f"\n=== Analysis for {label} ===")
    print(f"Sequence length: {total_length}")
    for base in "ATCG":
        print(f"{base} count: {counts[base]}")
    print(f"GC content: {gc_content:.2f}%")
    print(f"AT content: {at_content:.2f}%")
    print(f"Complement: {complement}")
    print(f"Reverse complement: {reverse_complement}")

    # Plot nucleotide frequencies using matplotlib (non-blocking)
    plot_nucleotide_frequencies(counts)

    # Return a dictionary of results for potential CSV saving
    return {
        "Label": label,
        "Length": total_length,
        "A": counts["A"],
        "T": counts["T"],
        "C": counts["C"],
        "G": counts["G"],
        "GC_Content(%)": round(gc_content, 2),
        "AT_Content(%)": round(at_content, 2),
        "Complement": complement,
        "Reverse_Complement": reverse_complement
    }