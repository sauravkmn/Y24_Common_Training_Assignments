opened lvl0 using ssh bandit0@bandit.labs.overthewire.org -p 2220 pwd was already provided as bandit0 used cat readme to find pwd for next lvl

opened lvl1 using ssh bandit1@bandit.labs.overthewire.org -p 2220 pwd is NH2SXQwcBdpmTEzi3bvBHMM9H66vVXjL then used cat ./- to open the file - in the home directory pwd for lvl 2 is rRGizSaX8Mk1RTb1CNQoXTcYZWU6lgzi

opened lvl2 using ssh bandit2@bandit.labs.overthewire.org -p 2220 after putting pwd opened the file spaces in the filename by using \ in front every space cat spaces\ in\ this\ filename pwd aBZ0W5EmUfAf7kHTQeOwd8bauFJ2lAiG for lvl3

opened lvl3 ssh bandit3@bandit.labs.overthewire.org -p 2220 cd inhere find ./ (to find the hidden directory) cat .hidden (to open the hidden directory) 2EW7BBsr6aMMoJ2HjW067dm8EgX26xNe

lvl4 ssh bandit3@bandit.labs.overthewire.org -p 2220 cd inhere file ./* (gives the description of the data present in the file) then we found that the ./-file07 has ASCII values which must be only human readable cat ./-file07 lrIWWI6bB37kxfiCQZqUdOIYfr6eEeqR

lvl5 ssh bandit5@bandit.labs.overthewire.org -p 2220 cd inhere find . -readable -size 1033c ! -executable (this find us the files that are readable and have size 1033 bytes(c stands for bytes) and not executable (! stands for executable) cat ./maybehere07/.file2 P4L4vucdmLnm8I7Vl7jG1ApGSfjYKqJU

lvl6 ssh bandit6@bandit.labs.overthewire.org -p 2220 find / -user bandit7 -group bandit6 -size 33c (lets us find the file with required given info) /var/lib/dpkg/info/bandit7.password this was the file that was found cat /var/lib/dpkg/info/bandit7.password to open the file z7WtoNQU2XfjmMtWA8u5rN4vzqu4v99S

lvl7 ssh bandit7@bandit.labs.overthewire.org -p 2220 ls cat data.txt grep millionth data.txt (it searches for the millionth and prints the whole line in which it was present since the password was just beside the word millionth it also got printed with it) TESKZC0XvTetK0S9xNwm25STk5iWrBvP

lvl8 ssh bandit8@bandit.labs.overthewire.org -p 2220 first we need to sort the file and then apply the uniq -u to find the only line that is unique in the data.txt but the thing is that sort data.txt does not change the input file so to find the output required we can find it by seperating the commands by | in the required order they need to be implemented sort data.txt | uniq -u (if we write data.txt again on uniq -u then it does not work so do not do so)

lvl9 ssh bandit9@bandit.labs.overthewire.org -p 2220 strings data.txt (this helps us eliminate the binary data and gives us the only human readable data there we can easily locate the data) (or to locate it we can also use the syntax strings data.txt | grep == to find the consecutive == in the strings found by the prev command ) G7w8LIi6J3kTb8A7j9LgrywtEUlyyp6s

lvl10 ssh bandit10@bandit.labs.overthewire.org -p 2220 base64 -d data.txt (this decodes the file data from base64 lang) 6zPeziLdR2RKNdNYFNb6nVCKzphlXHBM