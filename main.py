from sequence_utils import clean_sequence, count_nucleotides, calculate_gc_content, calculate_at_content
from complement_utils import get_complement, get_reverse_complement
from visualize import plot_nucleotide_frequencies


def main():
    while True:
        seq = input("Enter a DNA sequence (or type 'end' to quit): ").strip()
        if seq.lower() == "end" or seq == "":
            print("Goodbye!")
            break

        analyze_sequence(seq)


def analyze_sequence(seq):
    seq = clean_sequence(seq)
    counts = count_nucleotides(seq)
    total_length = sum(counts.values())

    if total_length == 0:
        print("No valid nucleotides found in the input sequence.")
        return

    gc_content = calculate_gc_content(counts)
    at_content = calculate_at_content(counts)

    print("\n=== DNA Sequence Analysis ===")
    print(f"Sequence length: {total_length}")
    for base in "ATCG":
        print(f"{base} count: {counts[base]}")
    print(f"GC content: {gc_content:.2f}%")
    print(f"AT content: {at_content:.2f}%")

    complement = get_complement(seq)
    reverse_complement = get_reverse_complement(seq)
    print(f"Complement: {complement}")
    print(f"Reverse complement: {reverse_complement}")

    plot_nucleotide_frequencies(counts)


if __name__ == "__main__":
    main()
