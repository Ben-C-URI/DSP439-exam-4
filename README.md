# DSP-439 Exam 4:

### Summary

This script and its test are used to answer questions 1-3 on exam 4 in BIO/DSP 439. This will do the following:
- identify all substrings of a provided genome of provided sizes
- use that vfunction and determine possible substrings, and subsequent substrings for the sequences provided in a text file
- and will then find the smallest value of k where k is the size of a substring, where there is only one possible substring that follows that sized substring

## Usage

To run this script, I used the following command while using my "Python" folder as my running workspace in python.

python3 genome.py ../../shared/439539/reads.fa

However, this can be run as (python3 "PATH-TO"/genome.py "PATH-TO"/reads.fa)

Running the main script on its own will provide an output that determines the "smallest
value" of k "where every substring
has only one possible substring that follows it".