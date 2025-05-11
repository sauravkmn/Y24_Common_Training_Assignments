# Bandit Wargames

## Level 0


Using ssh command to connect to the host on port 2220 with username bandit0. 
```bash
ssh bandit0@bandit.labs.overthewire.org -p 2220 -l bandit0
```

## Level 1
We use 
```bash
ls
cat readme
```
to read the readme to get the password ZjLjTmM6FvvyRnrb2rfNWOZOTa6ip5If

## Level 2
After using ls and then cat- , we realise that this doesnt work

Then we use 
```
cat ./-
```
to get the password 263JGJPfgU6LtdEvgfWU1XP5yac29mFx

## Level 3
To open such files,
```
cat spaces\ in\ this\ filename
```
For the password MNk8KNH3Usiio41PRUEoDFPqfxLPlSmx

## Level 4
As the file is hidden, we use ls -a inside the directory inhere

```
ls
cd inhere/
ls -a
cat .  .. ...Hiding-From-You
```

And get 2WmrDFRmJIq3IPxneAaMGhap0pFhF3NJ as the password

## Level 5
checking file type of all the files,
```
ls
cd inhere/
ls
file ./-file01
file ./-file02
file ./-file03
file ./-file04
file ./-file05
file ./-file06
file ./-file07
cat ./-file07

```
This gives that the file07 id of ASCII text and others are data files<br>
Password:4oQYVPkxZOOEOO5pTW81FB8j8lxXGUQw


## Level 6
We find that there are many files in the directory, so we use find to satisfy all the conditions
```
find -size 1033c -readable ! -executable
cat ./inhere/maybehere07/.file2
```
Password:HWasnPhtq9AVKe0dmk45nxy20cvUa6EG

## Level 7

```
find / -type f -size 33c -user bandit7 -group bandit6
cat /var/lib/dpkg/info/bandit7.password
```
We get a lot of files after using find and one of them is /var/lib/dpkg/info/bandit7.password which gives us
Password:morbNTDkSW6jIlUc0ymOdMaLnOlFVAaj


## Level 8
Finding for the word millionth in the file
```
grep -w "millionth" data.txt
```
we get the password:dfwvzFQi4mU0wfNbFOe9RoWskMLg7eEc
## Level 9
Sort the data and find which text occurs only once
```
sort data.txt
```
PAssword:4CKMh1JI91bUIZZPXDqGanal4xvAg0JM

## Level 10
After using 
```
strings data.txt | grep "=="
```
We get ========== the<br>
3JprD========== passwordi<br>
~fDV3========== is<br>
D9========== FGUW5ilLVJrxX9kMYMmlN4MgbpfMiqey<br><br>
Hence, the password: FGUW5ilLVJrxX9kMYMmlN4MgbpfMiqey
