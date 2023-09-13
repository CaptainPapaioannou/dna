# dna-profiler
Program that identifies to whom a sequence of DNA belongs. (CS50 problem set)

## Overview

This is a simple python program takes a sequence of DNA and a CSV file containing STR counts for a list of individuals and then output to whom the DNA (most likely) belongs.

### Theory behind dna identification:
DNA is really just a sequence of molecules called nucleotides, Every human cell has billions of nucleotides arranged in sequence. Each nucleotide of DNA contains one of four different bases: adenine (A), cytosine (C), guanine (G), or thymine (T). Some portions of this sequence (i.e., genome) are the same, or at least very similar, across almost all humans, but other portions of the sequence have a higher genetic diversity and thus vary more across the population. One place where DNA tends to have high genetic diversity is in Short Tandem Repeats (STRs). An STR is a short sequence of DNA bases that tends to repeat consecutively numerous times at specific locations inside of a person’s DNA. The number of times any particular STR repeats varies a lot among individuals. Using multiple STRs, rather than just one, can improve the accuracy of DNA profiling. If the probability that two people have the same number of repeats for a single STR is 5%, and the analyst looks at 10 different STRs, then the probability that two DNA samples match purely by chance is about 1 in 1 quadrillion (assuming all STRs are independent of each other). So if two DNA samples match in the number of repeats for each of the STRs, the analyst can be pretty confident they came from the same person. CODIS the FBI'S database for dna identification uses 20 different STRs as part of its DNA profiling process.


## How to Use
 **Compile and run the Program**: 
We have multiple DNA databases in the sipmplest form possible, csv files. 
The program requires as its first command-line argument the name of a CSV file containing the STR counts for a list of individuals and should require as its second command-line argument the name of a text file containing the DNA sequence to identify.

for exapmle:
  ```
    python dna.py databases/large.csv sequences/5.txt
  ```

This will output that the person that this DNA sequence most likely belongs is Levander


## NOTES
**This is a CS50 problem set solution**
