### Discription:
```txt
The password for the next level is stored in the file "data.txt",
where all lowercase (a-z) and uppercase (A-Z) letters have been rotated by 13 positions
```

---

Just like the previous levels we ssh into the server using:
```shell
$ ssh bandit.labs.overthewire.org -l bandit11 -p 2220
```

_You'll need to pass in the password from the previous level, i.e.: `IFukwKGsFW8MOq3IRFqrxE1hxTNEbUPR`_

<br>

The data in the file `data.txt` is encoded using [`ROT13`](https://en.wikipedia.org/wiki/ROT13), which can be decoded using the [`tr`](https://linux.die.net/man/1/tr) and the [`cat`](https://linux.die.net/man/1/cat) commands.

```shell
bandit11@bandit:~$ cat data.txt | tr '[a-zA-Z]' '[N-ZA-Mn-za-m]'
tHE PASSWORD IS 5tE8y4DRGcrFcX8UGDWUex8kfc6K2euU
```

---

##### Password for next level:
    5tE8y4DRGcrFcX8UGDWUex8kfc6K2euU

---

Link to the level: [Level 11 ➙ Level 12](https://overthewire.org/wargames/bandit/bandit12.html)
