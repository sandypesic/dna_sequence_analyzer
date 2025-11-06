import os
import csv
from sequence_utils import clean_sequence, count_nucleotides, calculate_gc_content, calculate_at_content
from complement_utils import get_complement, get_reverse_complement
from visualize import plot_nucleotide_frequencies
from fasta_utils import read_fasta


def analyze_sequence(seq, label="Sequence"):
    seq = clean_sequence(seq)
    counts = count_nucleotides(seq)
    total_length = sum(counts.values())

    if total_length == 0:
        print(f"\n{label}: No valid nucleotides found.")
        return None

    gc_content = calculate_gc_content(counts)
    at_content = calculate_at_content(counts)
    complement = get_complement(seq)
    reverse_complement = get_reverse_complement(seq)

    print(f"\n=== Analysis for {label} ===")
    print(f"Sequence length: {total_length}")
    for base in "ATCG":
        print(f"{base} count: {counts[base]}")
    print(f"GC content: {gc_content:.2f}%")
    print(f"AT content: {at_content:.2f}%")
    print(f"Complement: {complement}")
    print(f"Reverse complement: {reverse_complement}")

    plot_nucleotide_frequencies(counts)

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


def save_to_csv(results, filename="dna_analysis_results.csv"):
    if not results:
        print("No results to save.")
        return

    fieldnames = [
        "Label", "Length", "A", "T", "C", "G",
        "GC_Content(%)", "AT_Content(%)", "Complement", "Reverse_Complement"
    ]

    file_exists = os.path.isfile(filename)

    try:
        with open(filename, mode="a", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            if not file_exists:
                writer.writeheader()
            writer.writerows(results)
        print(f"\nResults saved to '{filename}'")
    except Exception as e:
        print(f"Error saving to CSV: {e}")


def main():
    while True:
        user_input = input("\nEnter a DNA sequence or FASTA file path (or type 'end' to quit): ").strip()
        if user_input.lower() in ("end", ""):
            print("\nGoodbye!")
            break

        batch_results = []

        if user_input.lower().endswith(('.fasta', '.fa')):
            if not os.path.isfile(user_input):
                print(f"\nError: File '{user_input}' does not exist.")
                continue

            fasta_data = read_fasta(user_input)
            if not fasta_data:
                print(f"\nNo sequences found in the FASTA file '{user_input}'.")
                continue

            for header, sequence in fasta_data.items():
                result = analyze_sequence(sequence, label=header)
                if result:
                    batch_results.append(result)

        else:
            result = analyze_sequence(user_input)
            if result:
                batch_results.append(result)

        if batch_results:
            save_choice = input("\nSave results to CSV? (y/n): ").strip().lower()
            if save_choice == "y":
                save_to_csv(batch_results)


if __name__ == "__main__":
    main()
