### Problem Statement:
```txt
It looks like our flag.txt file was encrypted with this an RSA public key.
We were able to save the public key key.pub though.

For some reason the public key file looks a little small...

Can we potentially decrypt the flag file even though we don't have the private key?
```

---

### Contents of `flag.txt`:
```txt
���6��[���#S�~b�����v����C&�
```


### Contents of `key.pub`:
```txt
-----BEGIN PUBLIC KEY-----
MDwwDQYJKoZIhvcNAQEBBQADKwAwKAIhAJpIENCYscv/dWgqCp3ahDFRl+tNqlgY
YlYnTANh3OYNAgMBAAE=
-----END PUBLIC KEY-----
```

---


A script similar to `weak_primes.py` may be implemented to decrypt the flag.


---

### Decrypted flag:
	


Link to the challenge: [Weak Primes](https://training.majorleaguecyber.org/challenges#Weak%20Primes-16)
