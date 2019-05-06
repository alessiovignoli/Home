#!bin/bash

for i in `cat nonhuman_kunitz_ids.txt`; do awk -v a=$i '$0~a {do {print  $0; getline} while($0 !~ /^>/); exit}' uniprot_sprot.fasta >> nonhuman_kunitz.fasta; done

# change name of the file in input in output and on which you search
# remember that this function because the file in inpit is just a list of indexes
