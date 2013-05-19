Consider a set of key-value pairs where each key is sequence id and each value is a string of nucleotides, e.g., GCTTCCGAAATGCTCGAA....


Write a MapReduce query to remove the last 10 characters from each string of nucleotides, then remove any duplicates generated.

You can test your solution to this problem using dna.json:
        python unique_trims.py dna.json
You can verify your solution against unique_trims.json.