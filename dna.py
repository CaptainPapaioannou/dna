import csv
import sys


def main():

    # Check for command-line usage
    if len(sys.argv) != 3:
        print("INVALID USAGE")
        sys.exit(1)

    # list to store wich STRs we are looking for
    STRs = []
    # list to store the whole database to use for identification later
    profiles = []

    # Read database file into a variable
    with open(sys.argv[1], "r") as database:
        # read with Dict reader to get a list of dictionaries for each person
        DBreader = csv.DictReader(database)

        # we use the field names function to get the STRs (keys) and we use [1:] because .fieldnames[0] is 'names'
        STRs = DBreader.fieldnames[1:]
        # copy database into profiles
        for row in DBreader:
            profiles.append(row)

    # create a dictionary that hase all the strs as keys and set counts to 0 for all of them
    STR_counts = dict.fromkeys(STRs, 0)

    # Read DNA sequence file into a variable
    with open(sys.argv[2], "r") as dna:
        # readline function reads the first line and the sequence is all in the first line
        sequence = dna.readline()

    # Find longest match of each STR in DNA sequence
    for STR in STRs:
        # using the given function
        STR_counts[STR] = longest_match(sequence, STR)

    # Check database for matching profiles
    for profile in profiles:

        matches = 0

        for STR in STRs:
            if int(profile[STR]) != STR_counts[STR]:
                continue

            matches += 1

        # if we have a match for all strs it means we have a sequence from a certain person
        if matches == len(STRs):
            print(profile['name'])
            sys.exit(0)

    # otherwise no match
    print("No match")
    sys.exit(0)

    return


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


# call main
main()
