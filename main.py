from sequence_utils import clean_sequence, count_nucleotides, calculate_gc_content, calculate_at_content
from complement_utils import get_complement, get_reverse_complement
from visualize import plot_nucleotide_frequencies


def main():
    while True:
        input_sequence = input("Enter a DNA sequence: ")
        seq = clean_sequence(input_sequence)
        counts = count_nucleotides(seq)
        total_length = sum(counts.values())

        if total_length == 0:
            print("No valid nucleotides found in the input sequence.")
        else:
            break
    
    gc_content = calculate_gc_content(counts)
    at_content = calculate_at_content(counts)
    complement_seq = get_complement(seq)
    reverse_complement_seq = get_reverse_complement(seq)
    
    print(f"\n=== DNA Sequence Analysis ===")
    print(f"Sequence length: {total_length}")
    for base in "ATCG":
        print(f"{base} count: {counts[base]}")
    print(f"GC content: {gc_content:.2f}%")
    print(f"AT content: {at_content:.2f}%")
    print(f"Complement: {complement_seq}")
    print(f"Reverse complement: {reverse_complement_seq}")

    plot_nucleotide_frequencies(counts)


if __name__ == "__main__":
    main()