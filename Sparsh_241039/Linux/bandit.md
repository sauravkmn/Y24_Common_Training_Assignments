# Writeup

## Level 0


Using ssh command to connect to the host on port 2220 with username bandit0. 
```bash
$ ssh bandit0@bandit.labs.overthewire.org -p 2220 
```
And then typing password on being prompted

## Level 1
Now we look for a file called readme
```bash
$ ls
```
and then
```bash
$ cat readme
```
This gives us the password: ZjLjTmM6FvvyRnrb2rfNWOZOTa6ip5If
<br>
Alternatively, we could have used `pico` or `vi`
## Level 2
Now we need to access a file named -
so we type
```bash
$ cat ./-
```
This gives us the password: 263JGJPfgU6LtdEvgfWU1XP5yac29mFx

Typing `cat -` simply would make it read from `stdin`, so we need to disambiguate


## Level 3
Next we need to access a filename with spaces in it, so we just put '' around it.
```bash
$ cat ./'spaces in this filename'
```
This gives us the password. MNk8KNH3Usiio41PRUEoDFPqfxLPlSmx
## Level 4
Now we access the inhere directory first using
```bash
$ cd inhere/
```
Then we need to see the hidden file, so we use
```bash
$ ls -a
```
Finally to get the password we do
```bash
$ cat ./...Hiding-From-You
```
This gives us the password: 2WmrDFRmJIq3IPxneAaMGhap0pFhF3NJ
## Level 5
First we go to the inhere directory
```bash
$ cd inhere/
```
Now we want to check type of all files present in the directory
We can use this command
```bash
$ find . -type f | xargs file
```
We find that file07 is containing ASCII text
So we check its contents and get the password.
```bash
$ cat ./-file07
```
This gives us the password: 4oQYVPkxZOOEOO5pTW81FB8j8lxXGUQw
## Level 6
Now we need to find a file satisfying a few conditions
First we go to the inhere directory
```bash
$ cd inhere/
```

Now we apply the conditions
```bash
$ find -type f ! -executable -size 1033c
```
Then we access the file contents
```bash
$ cat ./maybehere07/.file2
```
This gives us the password: HWasnPhtq9AVKe0dmk45nxy20cvUa6EG
## Level 7
Now we need to search the server(/)
```bash
$ find / -type f -user bandit7 -group bandit6 -size 33c
```
We get which file has the password.
```bash
$ cat /var/lib/dpkg/info/bandit7.password
```
This gives us the password: morbNTDkSW6jIlUc0ymOdMaLnOlFVAaj
## Level 8
Now to find a word we use the grep command
```bash
$ strings data.txt | grep "millionth"
```
This gives us the password: dfwvzFQi4mU0wfNbFOe9RoWskMLg7eEc
## Level 9
This file has a lot of repeated lines, so we use the uniq function along with sort to find which lines occurs only once
```bash
$ sort data.txt | uniq -c
```
This gives us the password: 4CKMh1JI91bUIZZPXDqGanal4xvAg0JM
## Level 10
Now we need to check the lines containing a bunch of = signs
We use the following command
```bash
$ strings data.txt | grep '=='
```
This gives us the password: FGUW5ilLVJrxX9kMYMmlN4MgbpfMiqey
## Level 11
Now the password is encoded in base64 so we use the base64 command to decode it
```bash
$ base64 -d data.txt
```
This gives us the password: dtR173fZKb0RRsDFSGsg2RWnpNVj3qRr
## Level 12
Now the password is encoded with rot13 cipher, we use tr command to decode it
```bash
$ cat data.txt | tr 'A-Za-z' 'N-ZA-Mn-za-m'
```
This gives us the password: 7x16WNeHIi5YkIhWsfFIqoognUTyj9Q4
