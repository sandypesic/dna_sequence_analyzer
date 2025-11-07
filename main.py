import os
from sequence_analysis import analyze_sequence
from csv_utils import save_to_csv
from fasta_utils import read_fasta


def main():
    """
    Main program loop for DNA sequence analysis:
    - Accept either a DNA sequence or a FASTA file path
    - Analyze sequences and optionally save results to CSV
    - Repeat until the user types 'end' or presses Enter
    """

    while True:
        # Prompt user for input
        user_input = input("\nEnter a DNA sequence or FASTA file path (or type 'end' to quit): ").strip()
        if user_input.lower() in ("end", ""):
            break

        batch_results = []  # Store analysis results for this batch

        # FASTA file input
        if user_input.lower().endswith(('.fasta', '.fa')):
            if not os.path.isfile(user_input):
                print(f"\nError: File '{user_input}' does not exist.")
                continue

            fasta_data = read_fasta(user_input)
            if not fasta_data:
                print(f"\nNo sequences found in the FASTA file '{user_input}'.")
                continue

            # Analyze each sequence in the FASTA file
            for header, sequence in fasta_data.items():
                result = analyze_sequence(sequence, label=header)
                if result:
                    batch_results.append(result)

        # Manual sequence input
        else:
            # Ask for a name for this sequence
            label = input("\nEnter a name for this sequence (or press Enter for 'Sequence'): ").strip()
            if not label:
                label = "Sequence"

            result = analyze_sequence(user_input, label=label)
            if result:
                batch_results.append(result)

        # Offer to save batch results to CSV
        if batch_results:
            save_choice = input("\nSave results to CSV? (y/n): ").strip().lower()
            if save_choice == "y":
                save_to_csv(batch_results)


if __name__ == "__main__":
    main()
