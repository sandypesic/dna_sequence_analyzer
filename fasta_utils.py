def read_fasta(filepath):
    """
    Read a FASTA file and return a dictionary of sequences:
    - Path to the FASTA file
    - Return a dictionary where:
        - Key = sequence header (without the '>')
        - Value = full DNA sequence as a single string
    - Handle multiple sequences in one file
    - Ignore empty lines
    """

    sequences = {}  # Store sequences as {header: sequence}
    header = None  # Current sequence header
    seq = []  # List to accumulate sequence lines

    with open(filepath, 'r') as f:
        for line in f:
            line = line.strip()  # Remove whitespace/newlines
            if not line:
                continue  # Skip empty lines

            if line.startswith('>'):  # New sequence header
                if header:  # Save previous sequence before starting new one
                    sequences[header] = ''.join(seq)
                header = line[1:]  # Remove the '>' from header
                seq = []  # Reset sequence accumulator
            else:
                seq.append(line)  # Add sequence line
        
        # Save the last sequence after finishing file
        if header:
            sequences[header] = ''.join(seq)

    return sequences
