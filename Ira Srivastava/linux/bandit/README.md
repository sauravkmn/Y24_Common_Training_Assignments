# Bandit Wargames Notes

---

## Level 0  
Use the ssh command to connect to the host on port 2220 with username `bandit0`.

```bash
ssh bandit0@bandit.labs.overthewire.org -p 2220 -l bandit0

Level 1

List files and read the readme:

ls
cat readme

Password: ZjLjTmM6FvvyRnrb2rfNWOZOTa6ip5If
Level 2

Using ls and cat - doesn’t work. So instead, use:

cat ./-

Password: 263JGJPfgU6LtdEvgfWU1XP5yac29mFx
Level 3

To open a file with spaces in its name:

cat spaces\ in\ this\ filename

Password: MNk8KNH3Usiio41PRUEoDFPqfxLPlSmx
Level 4

Hidden file in the inhere directory:

ls
cd inhere/
ls -a
cat .hidden

Password: 2WmrDFRmJIq3IPxneAaMGhap0pFhF3NJ
Level 5

Check file types, look for ASCII text:

ls
cd inhere/
ls
file ./*
cat ./-file07

Password: 4oQYVPkxZOOEOO5pTW81FB8j8lxXGUQw
Level 6

Find a file that's 1033 bytes, readable, and not executable:

find . -size 1033c -readable ! -executable
cat ./inhere/maybehere07/.file2

Password: HWasnPhtq9AVKe0dmk45nxy20cvUa6EG
Level 7

Find a 33-byte file owned by bandit7 and group bandit6:

find / -type f -size 33c -user bandit7 -group bandit6 2>/dev/null
cat /var/lib/dpkg/info/bandit7.password

Password: morbNTDkSW6jIlUc0ymOdMaLnOlFVAaj
Level 8

Look for the word "millionth":

grep -w "millionth" data.txt

Password: dfwvzFQi4mU0wfNbFOe9RoWskMLg7eEc
Level 9

Sort the data and look for a line that occurs only once:

sort data.txt | uniq -u

Password: 4CKMh1JI91bUIZZPXDqGanal4xvAg0JM
Level 10

Find printable strings that include ==:

strings data.txt | grep "=="

Password: FGUW5ilLVJrxX9kMYMmlN4MgbpfMiqey

