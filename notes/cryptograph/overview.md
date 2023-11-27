# Public Key Cryptography
In this note we give an overview of the core ideas and techniques in the RSA approach to public key cryptograpy.

The idea is to generate two keys: a public key $k_1$ and a private key $k_2$ and an encryption algorithm $E(k,m)$
which encrypts a message $m$ using the key $k$. The amazing feature of this algorithm is that if you encrypt $m$ with $k_1$ and then encrypt it again with $k_2$, you get your original message back! Moreover, we believe it is
very hard to discover the private key $k_2$ from the public key $k_1$.

## Using RSA to establish a secure connection when a third party can observe all of the communication
Assume we have three players Alice, Bob, and Carl and that Alice and Bob want to have a secret conversation,
but that Bob can hear everything they say.

* Alice and Bob each create their own public/private key pairs $a_1,a_2$ for Alice and $b_1,b_2$ for Bob.
* Alice and Bob exchange their public keys $a_1$ and $b_1$ and Carl can also see the public keys
* Alice then encodes her private message $m_1$ with Bob's private key and sends it to Bob. Carl sees the encoded message, but can't decode it as Carl doesn't have Bob's private key.
* Bob gets the message from Alice encoded with his public key and decodes it with his private key.
* Bob can likewise encode a message $m_2$ using Alice's public key and send it to Alice. Carl sees the encoded message, but can't decode it without the private key.
* Alice gets the message and decodes it with her private key.

