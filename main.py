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
        is_manual_input = False  # Mark batch as non-manual input

        # FASTA file input
        if user_input.lower().endswith(('.fasta', '.fa')):
            if not os.path.isfile(user_input):
                print(f"\nFile '{user_input}' does not exist.")
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
            is_manual_input = True  # Mark batch as manual input
            result = analyze_sequence(user_input)
            if not result:
                continue
            batch_results.append(result)

        # Offer to save batch results to CSV
        if batch_results:
            save_choice = input("\nSave results to CSV? (y/n): ").strip().lower()
            if save_choice == "y":

                # Ask for name only if input is manually entered
                if is_manual_input:
                    label = input("\nEnter a name for this sequence (or press Enter for 'Sequence'): ").strip()
                    batch_results[0]["Label"] = label if label else "Sequence"
                    
                save_to_csv(batch_results)


if __name__ == "__main__":
    main()
