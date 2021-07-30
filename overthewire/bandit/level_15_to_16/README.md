### Discription:
```txt
The password for the next level can be retrieved by submitting the password of
the current level to port 30001 on localhost using SSL encryption.

Helpful note: Getting “HEARTBEATING” and “Read R BLOCK”? Use -ign_eof and read
the “CONNECTED COMMANDS” section in the manpage. Next to ‘R’ and ‘Q’, the ‘B’
command also works in this version of that command…
```

---

Just like the previous levels we ssh into the server using:
```console
$ ssh bandit.labs.overthewire.org -l bandit15 -p 2220
```

_You'll need to pass in the password from the previous level, i.e.: `BfMYroe26WYalil77FoDi9qh59eK5xNr`_

<br>


Since the password is SSL encrypted, we can use [`openssl`](https://linux.die.net/man/1/openssl) to retrieve the password:


```console
bandit15@bandit:~$ openssl s_client -ign_eof -connect localhost:30001
CONNECTED(00000003)
depth=0 CN = localhost
verify error:num=18:self signed certificate
verify return:1
depth=0 CN = localhost
verify return:1
---
Certificate chain
 0 s:/CN=localhost
   i:/CN=localhost
---
Server certificate
-----BEGIN CERTIFICATE-----
MIICBjCCAW+gAwIBAgIEfftLGTANBgkqhkiG9w0BAQUFADAUMRIwEAYDVQQDDAls
b2NhbGhvc3QwHhcNMjEwNDEzMDgzODA3WhcNMjIwNDEzMDgzODA3WjAUMRIwEAYD
VQQDDAlsb2NhbGhvc3QwgZ8wDQYJKoZIhvcNAQEBBQADgY0AMIGJAoGBAMLfXBVa
jVKDHlA3U+S0hBMJMJlfue3xKECpmx1Ajp4/khUuWwvPB7+wLjqasBO2WfFYJzcq
z9t7FfAPIlYjgvOTQs5X4vQ1aGzanvnNn+1VknpOnFAJQBSFq6ZD3ipWrhwm9XZq
8CgFhTGp9IPthZp8Y0B7OgobhlMtXD/zLaTbAgMBAAGjZTBjMBQGA1UdEQQNMAuC
CWxvY2FsaG9zdDBLBglghkgBhvhCAQ0EPhY8QXV0b21hdGljYWxseSBnZW5lcmF0
ZWQgYnkgTmNhdC4gU2VlIGh0dHBzOi8vbm1hcC5vcmcvbmNhdC8uMA0GCSqGSIb3
DQEBBQUAA4GBAMFH9rsZovwnb5k71/MpyCnXEwGlIhixUu6qfi1kiFvhJ6lJCvaO
weOYxV4oJy1OEB0LSEAQOnSPfzC8dDasijFcdVhuIGGPuQ2GZ05nCiiIZUNnrMRB
0z2RuRxgxMVjOvcSIJyvwyjVH4jY4I434fMyldePLxO1POLd1cxoKNTO
-----END CERTIFICATE-----
subject=/CN=localhost
issuer=/CN=localhost
---
No client certificate CA names sent
Peer signing digest: SHA512
Server Temp Key: X25519, 253 bits
---
SSL handshake has read 1019 bytes and written 269 bytes
Verification error: self signed certificate
---
New, TLSv1.2, Cipher is ECDHE-RSA-AES256-GCM-SHA384
Server public key is 1024 bit
Secure Renegotiation IS supported
Compression: NONE
Expansion: NONE
No ALPN negotiated
SSL-Session:
    Protocol  : TLSv1.2
    Cipher    : ECDHE-RSA-AES256-GCM-SHA384
    Session-ID: 450E885F6B84798C22324799E81F19C723D57794CA27339EAE50E94D0A061CC2
    Session-ID-ctx:
    Master-Key: 1CF063B4810CB6015BEB7C1119017B67CC799AC8948DEF67A0C642F23F2D30CC0E2D30081A1DBA455AAD856887A0FA84
    PSK identity: None
    PSK identity hint: None
    SRP username: None
    TLS session ticket lifetime hint: 7200 (seconds)
    TLS session ticket:
    0000 - f2 5b 83 7e f0 ca 58 ca-aa f3 8f 83 b9 65 d5 23   .[.~..X......e.#
    0010 - 5e f3 75 ac 52 a9 6c 03-91 f0 cc b5 4b 06 d0 9c   ^.u.R.l.....K...
    0020 - ec 38 c6 6d 47 7d 58 73-0c da 74 9e 77 90 db 26   .8.mG}Xs..t.w..&
    0030 - 42 97 dd de 7d c8 b4 41-85 50 04 a5 86 db 1a fa   B...}..A.P......
    0040 - 4a 44 e9 47 70 18 fd 10-06 05 d4 be 75 5b 6a a6   JD.Gp.......u[j.
    0050 - 17 b8 c8 cd 54 41 f9 c3-8e 63 49 2e c7 fb 71 d5   ....TA...cI...q.
    0060 - 3a c1 31 b0 a5 eb 7e c2-02 ee fc 7f 22 d3 50 ae   :.1...~.....".P.
    0070 - 0a 36 c3 21 72 14 06 1e-e6 d1 94 74 cf 23 14 06   .6.!r......t.#..
    0080 - 03 5c 74 32 b4 58 17 9f-63 ed 8c 6d 7a 32 19 84   .\t2.X..c..mz2..
    0090 - a9 91 e6 8d 9d 0d a9 1c-ad 40 9d c8 96 d1 75 23   .........@....u#

    Start Time: 1627627058
    Timeout   : 7200 (sec)
    Verify return code: 18 (self signed certificate)
    Extended master secret: yes
---
BfMYroe26WYalil77FoDi9qh59eK5xNr
Correct!
cluFn7wTiGryunymYOu4RcffSxQluehd

closed
```

---

##### Password for next level:
    cluFn7wTiGryunymYOu4RcffSxQluehd

---

Link to the level: [Level 15 ➙ Level 16](https://overthewire.org/wargames/bandit/bandit16.html)
