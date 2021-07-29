We have been given a file `challenge_21.gz`. Which we can extract data from using the `gzip` command:


```console
$ gzip --decompress challenge_21.gz
$ ls
challenge_21
```

Now that we've decompressed the file, we can use the `file` command to check what we're dealing with.


```console
$ file challenge_21
challenge_21: POSIX tar archive (GNU)
```

<br>

We can decompress this using `tar`:

```console
$ tar -xf challenge_21
$ ls
challenge_21  image
```

<br>

This has decompressed `challenge_21` to `image`
Let's check what this is:

```console
$ file image
image: directory
```

Furthermore:

```console
$ cd image
$ ls
challenge

$ file challenge
challenge: directory

$ cd challenge
$ ls
challenge

$ file challenge
challenge: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 2.6.32, BuildID[sha1]=1c86fc6fe1662
d8037294b634c1cd0011bb304cb, stripped
```

We can see that the file `image/challenge/challenge` is an executable. Let's try and run it:
