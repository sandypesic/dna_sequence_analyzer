import matplotlib.pyplot as plt


def plot_nucleotide_frequencies(counts):
    """
    Generate a bar chart of nucleotide frequencies for a DNA sequence:
    - Dictionary with keys 'A', 'T', 'C', 'G' and their counts
    - Calculate percentage frequencies for each nucleotide
    - Plot a bar chart with colored bars and percentage labels above each bar
    - Use non-blocking plotting so program can continue after showing chart
    """

    # Define nucleotides and calculate percentages
    bases = ["A", "T", "C", "G"]
    total = sum(counts.values())
    freqs = [(counts[base] / total) * 100 for base in bases]

    # Create a figure and plot bars
    plt.figure(figsize=(6,4))
    plt.bar(bases, freqs, color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728'])
    plt.title("Nucleotide Frequencies (%)")
    plt.xlabel("Nucleotide")
    plt.ylabel("Percentage (%)")

    # Add text labels above bars
    # Slightly offset the text above the bar to avoid overlap
    for i, v in enumerate(freqs):
        plt.text(i, v + 0.25, f"{v:.2f}%", ha='center')

    # Show the plot without blocking the program
    plt.show(block=False)
