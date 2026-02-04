# CS351 - Intro to Cybersecurity - Cryptography #
## Classical Ciphers ##
__cryptography:__ the science of secret and obscured writing <br>
two main components:
1. Encryption: practice of hiding messages so that they can not be read by anyone other then the intended recipient
2. Authentication & Integrity: ensuring that the users data/resources are from who they say they are, and has not be modified

Types of Ciphers:
- Classical: Substitution, Transposition
- Rotor Machines
- Modern: Public Key, Private Key Stream, Private Key Block

Block: blocks of bits will be encrypted <br>
Stream: continuous 1 by 1 bits will be encrypted <br>

### Types of Classical Ciphers: ###
Categories: __Monoalphabetic Ciphers, Polyalphabetic Ciphers, Homophonic Cipher, Polygram Cipher__ <br>
- Monoalphabetic: one to one replacement for a character to another character (frequency analysis breaks this easily)
- Polyalphabetic: for a character, it will cycle through different characters (increased complexity)
- Homophonic: character replacement into symbols
- Polygram: instead of subsituting a single letter, multiple letters can be converted into another character

### Monoalphabetic Ciphers ###
__Caeser Cipher:__
by shifting the letters in the used alphabet, you will get a completely different set of characters as the output <br>
ABCDE --> shift of 2 --> CDEFG <br>
ROME IS THE GREATEST EMPIRE --> shift 7 --> YVTL PZ AOL NYLHALZA LTWPYL <br>
- can be broken by frequency analysis EASILY
- limited to 25 different possible shifts
- known today and easily decipherable
Revealed by Seutonis, a roman cleric <br>

__Reciprocal Cipher:__ if x-->y then y-->x
combination strength: 25x23x21x19x17x15x14x13x11x9x7x5x3x1 <br>
- better, but frequency analysis can signif reduce time

__Random Cipher:__ character assignment is purely random <br>
- no logic behind the key, so how will the other side be able to interept it?
- 26! strength

__Frequency Analysis:__ exploit the regularities of the language to find common letters (language dependent) <br>
- Mono:1, Digram:2, Trigram:3 <br>

## Symmetric Encryption ##
__def:__ the same key is used for encryption and decryption <br>
- key distribution is the biggest hurdle to tackle with symmetric encryption!
## Asymmetric Encryption ##
__def:__ utilization of public and private keys in order to maintain encryption and decryption process. <br>