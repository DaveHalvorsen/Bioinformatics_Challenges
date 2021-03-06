#!/usr/bin/env python
'''
Given: A DNA string t having length at most 1000 nt.
Return: The transcribed RNA string of t (replacing T w/ U).
Sample Dataset
    GATGGAACTTGACTACGTAAATT
Sample Output
    GAUGGAACUUGACUACGUAAAUU
'''

'''
works with the provided sample dataset
line = 'GATGGAACTTGACTACGTAAATT'
transcription = ''
characters = list(line)
untouched_nucleotides = 'A', 'G', 'C'
changing_nucleotides = 'T'
# print(characters)
for character in characters:
    if character in untouched_nucleotides:
        print('UNTOUCHED')
        transcription = transcription + character
    else:
        print('TOUCHED')
        transcription = transcription + 'U'
print(transcription)
'''

file = open('/home/david/Downloads/rosalind_rna.txt', 'r')
output = open('rosalind_rna_answer.txt', 'w')

line = file.readline().rstrip()
transcription = ''
characters = list(line)
untouched_nucleotides = 'A', 'G', 'C'
changing_nucleotides = 'T'
# print(characters)
for character in characters:
    if character in untouched_nucleotides:
        print('UNTOUCHED')
        transcription = transcription + character
    else:
        print('TOUCHED')
        transcription = transcription + 'U'
print(transcription)
