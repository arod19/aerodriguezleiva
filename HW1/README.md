Homework #1

- Description:
This program uses argparse command line tools to prompt the user for a cipher of his/her choice and also if the file
that is input is to be either decrypted or encrypted.

- Features:
It features 5 ciphers: Caesar, Vigenere, Basic Substition, Transposition, and .

- Python Version:
3.6.3

- Libraries used:
argparse: The argparse module makes it easy to write user-friendly command-line interfaces.

The reason for the implementation of this library is that it was required for the assignment and it is a great parsing library.

- Command line help:
. Must have either -d (to decrypt the file) or -e (to encrypt the file) as the first flag, then the first letter of the name
of the desired cipher:

1. -c : Caesar
1. -v : Vigenere
1. -s : Substitution
1. -t : Transpose
1. -l : LeetSpeak

. At the end, input the file of the plain text or encrypted text.
Note: It must be in the same directory as the python file.

- References:
1. "Elements of Cryptanalysis" by William F. Friedman
2. "Serious Cryptography" by Jean-Philippe Aumasson
3. Marcus Chong during TA office hours.
