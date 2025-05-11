## Level 0

```
ssh -p 2220 bandit0@bandit.labs.overthewire.org 
```
**Password**: bandit0

---

### Level 0 → Level 1

**Task**: Read the file named `readme` in the home directory.

```bash
cat readme
```
**Password**: ZjLjTmM6FvvyRnrb2rfNWOZOTa6ip5If

---

### Level 1 → Level 2

**Task**: Read a file named `-`.
**Soln**: Write full address of file starting with ./
```bash
cat ./-
```
**Password**: 263JGJPfgU6LtdEvgfWU1XP5yac29mFx

---

### Level 2 → Level 3

**Task**: Read a file named `spaces in this filename`.
**Soln**: Write file name within quotes.
```bash
cat "spaces in this filename"
```
**Password**: MNk8KNH3Usiio41PRUEoDFPqfxLPlSmx

---

### Level 3 → Level 4

**Task**: Read a hidden file in the `inhere` directory.
**Soln**: use ls -a to list *all* files/directories.
```bash
cd inhere
ls -a
cat .hidden
```
**Password**: 2WmrDFRmJIq3IPxneAaMGhap0pFhF3NJ

---

### Level 4 → Level 5

**Task**: Find a human-readable file (not executable, not a directory).
**Soln**: Use file ./* to run file command on all files in given directory, file of type ASCII text contains password.
```bash
cd inhere
file ./*
cat ./-file07
```
**Password**: 4oQYVPkxZOOEOO5pTW81FB8j8lxXGUQw

---

### Level 5 → Level 6

**Task**: Find a file of 1033 bytes, human-readable, not executable.
**Soln**: find file of given size which is *not* executable. Note: Bytes is represented using 'c'.
```bash
find . -type f -size 1033c ! -executable
cat ./inhere/maybehere07/.file2
```
**Password**: HWasnPhtq9AVKe0dmk45nxy20cvUa6EG

---

### Level 6 → Level 7

**Task**: Find a file owned by `bandit7`, group `bandit6`, and size 33 bytes.
**Soln**: use find / to start search from root directory, add the user and group names along with mentioned size.
```bash
find / -user bandit7 -group bandit6 -size 33c
cat /var/lib/dpkg/info/bandit7.password
```
**Password**: morbNTDkSW6jIlUc0ymOdMaLnOlFVAaj

---

### Level 7 → Level 8

**Task**: Find the password next to the word `millionth`.
**Soln**: Use grep to search for millionth in file and print corresponding line.
```bash
grep "millionth" data.txt
```
**Password**: dfwvzFQi4mU0wfNbFOe9RoWskMLg7eEc

---

### Level 8 → Level 9

**Task**: Find the only line that appears once.
**Soln**: uniq only scans for lines unique among its neighbours therefore precede it by sorting the data so that similar lines become neighbours.
```bash
sort data.txt | uniq -u
```
**Password**: 4CKMh1JI91bUIZZPXDqGanal4xvAg0JM

---

### Level 10 → Level 11

**Task**: Find human-readable string preceded by multiple =.
**Soln**: Use strings to get all human readable lines followed by grep "==" to output all lines preceded by more than one =
```bash
strings data.txt | grep "=="
```
**Password**: FGUW5ilLVJrxX9kMYMmlN4MgbpfMiqey

---

### Level 10 → Level 11

**Task**: Decode a base64-encoded file.
**Soln**: Use base64 -d to decode data.
```bash
base64 -d data.txt
```
**Password**: dtR173fZKb0RRsDFSGsg2RWnpNVj3qRr

---

