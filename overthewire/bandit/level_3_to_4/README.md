### Discription:
```txt
The password for the next level is stored in a hidden file in the "inhere" directory.
```

---

Just like the previous levels we ssh into the server using:
```shell
$ ssh bandit.labs.overthewire.org -l bandit3 -p 2220
```

Now, as per the discription of the level, we navigate to the `inhere` directory using the `cd` command.

```shell
bandit3@bandit:~$ cd inhere/
bandit3@bandit:~/inhere$
```

Since we've been given the hint that the file is "hidden", we can use the `ls` command with the `-a` flag to display all files within the directory.

```shell
bandit3@bandit:~/inhere$ ls -a
.  ..  .hidden
```

There it is. The hidden file's named: `.hidden`

Once again using the `cat` command we can display the password for the next level:

```shell
bandit3@bandit:~/inhere$ cat ./.hidden
pIwrPrtPN36QITSp3EQaw936yaFoFgAB
```

---

##### Password for Level 3 ➙ Level 4:
    pIwrPrtPN36QITSp3EQaw936yaFoFgAB

---

Link to the level: [Level 3 ➙ Level 4](https://overthewire.org/wargames/bandit/bandit4.html)
