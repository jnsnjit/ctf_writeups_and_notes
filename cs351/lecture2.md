# CS351 - Intro to Cybersecurity - Cryptography #
# Classical Ciphers #
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

### Polygraph Ciphers ###
__Playfair Cipher:__ refer to slides on how it works, utilizes a five-by five grid to encrypt pairs of characters <br>

P L A Y E <br>
I/J R B C D <br>
E G H K M <br>
N O Q S T <br>
U V W X Z <br>

PT: hide the gold in the tree stump <br>
key: playfa(i/j)r <br>

hi de th eg ol di nt he tr ee-->ex es tu mp <br>
bm od zb xd na be ku dm ui      xm mo uv if <br>

kind of tough, needs practice! <br>
https://en.wikipedia.org/wiki/Playfair_cipher

__Polyalphabetic Cipher / Vigenire:__ use a multi letter subsituition for each letter <br>
__key__: deceptive <br>
__PT__: we are discovered save yourself <br>

(d + w)% 26 = ciphertext <br>
a vignerere table can help! <br>

deceptivedeceptivedeceptive <br>
wearediscoveredsaveyourself <br>

first char --> (4+22) = 26 % 26 = 0 = z <br>

__Vernam Cipher:__ choose a keyword that is as long as the plaintext and has no statistical relationship to it, usually done on bits. <br>

PT:  1010010
KEY: 1110111
____________
CT:  0100101
K:   1110111
____________
     1010010

__important:__ key MUST be the size of the plaintext, with transportation of the key and storage being hard. <br>

__One-Time Pad:__ cipher that uses a random key, truly as long as the message, with no repetitions and purely random. <br>
- imagine a 1GB file, making the key for it only will double the size of the file
- computers struggle with truly random number generators
- must continuously share the key over and over and over 

### Transposition Cipher ###
__Railfence Cipher:__ plaintext is written in a sequence of diagonals and read oof as a sequence of rows 
PT: meet me after the toga party <br>
fence depth of 2: <br>
m e m a t r h t g p r y <br>
 e t e f e t e o a a t <br>

\    /\    /    ex of fence of 3 <br>
 \  /  \  /                      <br>
  \/    \/                       <br>

__Row Transposition Cipher:__ <br>
1. write message row-wise
2. read the message column wise, in some specific order

key: 7 4 1 6 3 5 2 <br>
PT:  a n u n a n n <br>
     o u n c e d q <br>
     u i z o n f r <br>
     i d a y x y z <br>

CT: UNZA NQRZ AENX NUID NDFY NCOY AOUI
PT: an unannounced quiz on friday xyz





## Symmetric Encryption ##
__def:__ the same key is used for encryption and decryption <br>
- key distribution is the biggest hurdle to tackle with symmetric encryption!
## Asymmetric Encryption ##
__def:__ utilization of public and private keys in order to maintain encryption and decryption process. <br>


## Stream ##
__def:__ a stream cipher processes messages bit-by-bit

## Block ##
__def:__ a block cipher takes block of messages and encrypts then in groups 

# Modern Ciphers #

## Feistel Cipher ##
Most block ciphers are based on feistel structure:
- Partition input block into two halfs:   64 --> 32 | 32
- perform a substitution on left half of data
- substituition based on round function of right half and subkey
- then have permutation swapping halfs

the more rounds that you can perform these steps, the better you can achieve a "true random" <br>

Things to consider:
1. Block size: larger blocks == greater security
2. Key size: larger key size == greater security
3. Number of rounds == multiple rounds offer increasing security
4. Subkey generation algorithm == greater complexity will lead to greater difficulty of cryptanalysis
5. Fast software encryption/decryption == speed of execution of the algorithm becomes a concern

## DES - Data Encryption Standard ##
most widely used encryption scheme especially in finanicial applications <br>
block cipher --> 64 bits in size, 56 in actually key complexity, 8 bits are used for error checking <br>


Initial Permutation
E-Box
S-Box:
- taking 48 bit input and reducing into 32 bits. There will 8 sboxes, in which each one will take an input of six bits and return 4 bits
row1  .. .. .. .. .. .. .. <br>
row2  .. .. .. .. .. .. .. <br>
row3  .. .. .. .. .. .. .. <br>
row4  .. .. .. .. .. .. .. <br>

1110 - 14 <br>
1100 - 12 <br>

for the exam, know key size, effective key size, structure, ebox and sbox! <br>
when DES was first proposed, a 56 bit key sound secure, but know it is computationally crackable <br>
- temp solution, double the key size to 112 bits, and 2^112 complex
- meet in the middle attack basically negates that idea
- temp temp soluion --> triple DES / 3DES

## Modes of Operations ##
1. Electronic Codebook (ECB)
take p1 plaintext with key --> c1.  if the plaintext is the same, then the output is the same <br>

2. Cipher Block Chaining (CBC)
take p1 plaintext + IV (initialization vector) + XOR --> +key --> c1 --> acts as IV for p2 <br> 
now if the plaintext is the same, then the output is different. <br>

3. Cipher Feedback (CFB)
message is treated as a stream of bits (block cipher acting like stream) <br>
IV (Shift Register) + # of bits (less then 64 to be considered a stream) to make enough to the encrypt step, then decide how many bits to keep, then shift the register to the left <br>

4. Output Feedback (OFB)
very similiar to CFB, but instead of feeding c1 to be the shift register of the next bit, you feed the encryption step, but not the cipher at the end, high network speed <br> 

5. Counter Mode (CTR)
similiar to OFB, but encrypts counter value rather then any feedback value <br>
now the security is only really tied to the key. counters must also be synced between devices

## AES - American Encryption Standard ##
RIJNDAL Cipher <br>
128 bit blocks, with a key size mininum of 128 bits, up to 256bits <br>

review simulation steps in class module <br>



