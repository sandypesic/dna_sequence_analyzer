def read_fasta(filepath):
    sequences = {}
    header = None
    seq = []

    try:
        with open(filepath, 'r') as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                if line.startswith('>'):
                    if header:
                        sequences[header] = ''.join(seq)
                    header = line[1:]
                    seq = []
                else:
                    seq.append(line)
            if header:
                sequences[header] = ''.join(seq)
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
    except Exception as e:
        print(f"Error reading FASTA file: {e}")

    return sequences
