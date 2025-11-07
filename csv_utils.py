import os
import csv


def save_to_csv(results, filename="dna_analysis_results.csv"):
    """
    Save a list of sequence analysis dictionaries to a CSV file:
    - Append to the file if it exists
    - Write a header if the file does not exist
    - Print a confirmation message on success
    """

    if not results:
        print("No results to save.")
        return

    # Define the CSV column order
    fieldnames = [
        "Label", "Length", "A", "T", "C", "G",
        "GC_Content(%)", "AT_Content(%)", "Complement", "Reverse_Complement"
    ]

    file_exists = os.path.isfile(filename)

    try:
        # Open CSV in append mode
        with open(filename, mode="a", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            # Write header only if file does not exist
            if not file_exists:
                writer.writeheader()

            # Write all rows
            writer.writerows(results)

        print(f"\nResults saved to '{filename}'.")
    except Exception as e:
        # Catch any exception that occurs while opening/writing the file
        print(f"Error saving to CSV: '{e}'.")