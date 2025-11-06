import matplotlib.pyplot as plt


def plot_nucleotide_frequencies(counts):
    bases = ["A", "T", "C", "G"]
    total = sum(counts.values())
    freqs = [(counts[base] / total) * 100 for base in bases]

    plt.figure(figsize=(6,4))
    plt.bar(bases, freqs, color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728'])
    plt.title("Nucleotide Frequencies (%)")
    plt.xlabel("Nucleotide")
    plt.ylabel("Percentage (%)")
    plt.ylim(0, 100)
    for i, v in enumerate(freqs):
        plt.text(i, v + 1, f"{v:.2f}%", ha='center')

    plt.show(block=False)
