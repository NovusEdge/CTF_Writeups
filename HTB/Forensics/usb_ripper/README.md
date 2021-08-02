### CTF Discription:
```txt
There is a sysadmin, who has been dumping all the USB events on his Linux host
all the year... Recently, some bad guys managed to steal some data from his
machine when they broke into the office. Can you help him to put a tail on the
intruders? Note: once you find it, "crack" it.
```

---

Unzipping the given file:
```zsh
$ unzip "USB Ripper.zip"
```

_Pass in `hackthebox` as the password when prompted._

Once we unzip the archive, we get 2 files: `usb-ripper/auth.json` and `usb-ripper/syslog`


Both are rather **large** files, as can be seen after using [`wc`](https://linux.die.net/man/1/wc) to inspect them.

```zsh
$ wc usb-ripper/auth.json
 300007   300011 11734103 usb-ripper/auth.json

$ wc usb-ripper/syslog
 900000 12000000 85784244 usb-ripper/syslog
```



---

### The Flag:



Link to the challenge: [USB Ripper](https://app.hackthebox.eu/challenges/usb-ripper)
