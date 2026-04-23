# Public Key Cryptology / PKI #
Done with Asymmetric Encryption, requires a public and private key! <br>
Private Key acts as a digital signature, provides proof that the message came from a designated source! <br>

## RSA ##
specifically for generating and using public and private keys <br>
worth 20 points on the final! <br>
invented by three ppl! <br>

Step 1:
- choose two very Large Prime Numbers    (ex     P=3    Q=11)
Step 2:
- calculate N --->   N=P*Q               (ex  N=33)
Step 3:
- 0(n) (phi)     0(n) = (p-1)*(q-1)       0(n) = 2 * 10 = 20
Step 4:
- choose a public key (E)     1 < E < 0(n), e should be a coprime of 0(n) --> gcd(e,0(n)) = 1          E=7
Step 5:
- find private key  D = ( 1 + K 0(n) ) / E     D must be whole number, test for K           1+1*20 / 7  = 3 -->   D=3

How to Write: <br>
Public Key = (E,N) = (7,33) <br>
Private Key = (D,N) = (3,33) <br>

_will need a calculator for final!_ <br>

How to Test! <br>
M = E <br>
Encryption: M^E mod N = C
Decryption: C^D mod N = M

## Diffle-Helman ##
Specifically for Public Key Exchange! To exchange a SYMMETRIC key over a insecure channel! <br> 
solves the big problem with using symmetric encryption!! <br>

1. Choose a Prime Number:
q=11
2. Choose alpha (a), which is a primative root of q:
a^1 mod q = 1
a^2 mod q = 2
...
a^(q-1) mod q = 4 <br>

a=7 <br>
3. with alpha and q shared ... Party1 will generate Xa, and Party2 will generate Xb, both of them being less the q (these are both private)
Xa = 5 <br>
Xb = 9 <br>

Publically --> (they will exchange)
Ya = a^Xa mod q = 7^5 mod 11 = 10
Yb = a^Xb mod q = 7^9 mod 11 = 8

4. will shared Ya and Yb, time to calculate key
Party1: K = Yb^Xa mod q <br>
Party2: K = Ya^Xb mod q <br>

5. this answer SHOULD be the same on both sides, meaning that they have successfully shared the symmetric key!

### Diffle-Helman MITM Attack ###
Alice       Darth           Bob <br>
a,q         a,q             a,q <br>
Xa          Xd1,Xd2         Xb <br>
Ya          Yd1,Yd2         Yb <br>
Ya -> intercept with Yd1 -> Yb (BAD) <br>
Yd1     <-        x      <- Yb (BAD) <br>

## MAC ##
__def:__ Message Authentication Code <br>
        M     ---- [M]
        |
K --> [MAC]        [MAC] --->
        |            ^
      [MAC]   ----   |

since they both have the same symmetric key, the receiver can verify the legitmacy by doing the same process! <br>

MAC:
1. Integrity
2. Message Authentication

## Digital Signatures ##
if there is a message M, a digital signature will provide the reciever of the message a way of knowing that the message came from the source it claims to be. <br>

                 M ----- [M]
                 |       [ ]
Private Key --> [DS]     [ ] --> 
                 |
                 S ----- [s]

 Digital Signatures Provide:
 1. Integrity
 2. Message Authentication
 3. Non-Repudiation (Proof that a message came from you)

## SSL / PKI ##
me ---> server <br>

1. make request to have access to certain resource
2. response will send a public key certificate from the server! (the public key of the server)
3. you will generate a symmetric key (session key K), encrypted with the public key of the server
4. for the rest of the traffic generated, this symmetric used will be used to encryption the rest of the bulk of the data. 
