from genome import *

def test_find_kmer():
    sequence = "ATGTCTGTCTGAA" # Define a sequence
    k = 3 # Define a value for K
    please_work = { # Calculated predicted dct values using GPT and double-checked.
        "ATG": ["TCT"],
        "TGT": ["CTG", "CTG"],
        "GTC": ["TCT"],
        "TCT": ["GTC", "GAA"]
    }
    assert find_kmer(sequence, k) == please_work

def test_all_kmers():
    filename = "../../shared/439539/reads.fa"
    k = 3 # Define a value for K
    please_work = { # Calculated predicted dct values using GPT and double-checked.
        "ATG": {"TCT": ["CTG"]},
        "TGT": {"CTG": ["TCT"], "CTG": ["GAA"]},
        "GTC": {"TCT": ["CTG"]},
        "TCT": {"GTC": ["TCT"], "GAA": []}
    }
    assert all_kmers(filename, k) == please_work

def test_smallest_k():
    filename = "../../shared/439539/reads.fa"
    k = 3 # Define a value for K
    assert smallest_k(filename, k) == 2