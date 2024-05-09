#!/usr/bin/env python3

# Q1. Define a function to identify all substrings of size k.

def find_kmer(sequence, k):
    
    """

    This function identifies all substrings of size k and their subsequent substrings.
    
    Arguments:
      sequence (str): Provided sequence of genetic data for analysis.
      k (int): Size of the substring.
      
    Return:
      dict: A dictionary of all substrings and their subsequent substrings

    Usage:
      find_kmer('ATGTCTGTCTGAA', 3) Which would find all substrings of size 3 and their subsequent substrings.
          
    """

    kmers = {} # Create a dictionary to store the substrngs 
    for i in range(len(sequence) - k): # Iterate over range, which is length of the input, agaubst the size of the substring
        kmer = sequence[i:i+k] # Substring is the sequence from i to i+k which accounts for the size of the substring and the subsequent substring
        if kmer not in kmers: # and if the substring is not in the dictionary...
            kmers[kmer] = [] # add it to the dictionary!
        kmers[kmer].append(sequence[i+k:i+k+k]) # Then, compared to the original substring, add the subsequent substring to the dictionary. Calculated by adding the size of the substring to the end of the original substring.
    return kmers # Return output.

# Q2. Define a function that uses the prior function to identify all possible substrings 
#     and their subsequent substrings for all sequences read from a file.

def all_kmers(filename, k):
    
    """

    This function identifies all possible substrings and their subsequent substrings for all text read from provided filename below.
    
    Arguments:
      filename (str): File containing the sequences.
      k (int): Size of the substring.
      
    Return:
      dict: A dictionary of all substrings and their subsequent substrings for all text read from provided file.
      
    """

    kmers = {}
    with open(filename, 'r') as f: # Opening file, reading as F.
        for line in f: # Iterating over each line in file F.
            sequence = line.strip() # Get rid of filler/spaces in order to iterate as one large string, makes easier.
            kmers[sequence] = find_kmer(sequence, k) # Adds onto old dicationary, new dictionary of all substrings + subsequent substrings
    return kmers # Return output.

# Q3. Define a function to identify the smallest value using the prior functions.

def smallest_k(filename, k):
    
    """
    
    This function identifies the smallest value using the prior functions.
    
    Arguments:
      filename (str): File containing the sequences.
      k (int): Size of the substring.
      
    Return:
      int: the smallest possible value that k could be, where "at least one value of k [in which] every substring has only one possible substring that follows it.
      
    """

    kmers = all_kmers(filename, k)
    smallest = float('inf') # Set smallest to infinity, had to determine between this or sys.maxsize which is the largest possible value for a provided variable.
    for sequence in kmers: # Iterate over the sequences in the dictionary from all_kmers function.
        for kmer in kmers[sequence]: 
            if len(kmers[sequence][kmer]) == 1: # Find values where each substring has only one possible substring tfollowing it.
                if k < smallest: # Place this K value as the smallest K value first identified.
                    smallest = k #Update the smallest value to be the smallest K, and then continue to iterate over the rest of the sequences.
    return smallest # Return output.
  
# Q7

if __name__ == '__main__':
    import sys # Import sys module
    filename = sys.argv[1] # Assign first argument to the filename.
    k = smallest_k(filename, 2) # Assign second variable to k in the smallest_k function, while reading first argument.
    print(k) # Print the smallest value of k.