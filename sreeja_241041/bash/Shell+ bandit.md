
## Shells
Shell is the outer layer that helps the user interact with the kernel.
In general, shell can be classified as Command Line Interface and Graphical User Interface

## Cmd(Command Prompt):
This is the default shell of windows

Use cases:
- For performing simple file operations like copy, move, delete
- For running batch scripts(text files that contain list of commands executed in order by the shell)
- Launching applications
- Troubleshooting

Commands:
dir, cd, del, copy, move

Power: low, as it does not support piping(way of connecting commands) with complex logic, variable manipulation

## bash(Bourne Again Shell):
Default shell of linux/ macOS

Use Cases:
- General system automation and scripting in linux/mac
- For writing bash scripts(.sh)
- Managing processes, pipelines, text processing
- Widely used in DevOps and server environments

Commands:
- Supports redirection, piping, functions, arrays, etc.


Power: 
- High, extremely flexible; supports complex scripting, task automation, environment configuration

## PowerShell:
- Advanced windows shell
- Also available on linux/macOS

Use cases:
- System administration on Windows
- Automating tasks using .NET objects
(.NET objects: They are structured blocks of data created using the .NET framework, which is Microsoft’s platform for building applications.)
- Since PowerShell is built on NET, it gives structured data which can be easily manipulated, like filtering and sorting
- Managing Windows services, registry, users, etc.

Commands:
- Verb-Noun syntax
- Handles objects

Power: 
Very high, Designed for automation and complex system management; full access to Windows internals and .NET


## Anaconda Prompt:
Use cases:
- Specifically for Python and data science workflows
- Managing conda(tool to manage Python packages and create clean, separate environments for each project.) environments and packages
- Running Jupyter notebooks, Spyder, etc.

Commands;
- Conda commands
- Regular shells commands

Power: Medium, useful within data sci ecosystem

## Bandit

## Level 0


Using ssh command to connect to the host on port 2220 with username bandit0. 
```bash
$ ssh bandit0@bandit.labs.overthewire.org -p 2220 -l bandit0
```

## Level 1
had to use cd, ls and less to change directory,view directory and read the readme text file respectively

## Level 2
to read the '-' file, had to use ./-
```bash
$ cat ./-
```
## Level 3
```bash
$ ls "spaces in this filename"
```
## Level 4
had to use ls -a to view the hidden file and then used cat to read it
```bash
$ cat $(ls -a)
```
## Level 5
had to use '--' after cat so that -f was not taken as a function and tried for all the files present to see which one had the human readable text
```bash
$ cat -- -file07
```
## Level 6
none of the visible files was of 1033 bytes so had to check the hidden ones also by doing:
```bash
$ls -l */.* |grep 1033 
```
which gave that .file2 in maybehere07 satisfied the conditions, so had to view the file through:
```bash
$ cat -- maybehere07/.file2
```
## Level 7
to find the file that satisfied the given conditions, used:
```bash
$ find / -user bandit7 -group bandit6 -size 33c 
```
there was only 1 file for which there was permission so read into the file to get the password
```bash
$cat /var/lib/dpkg/info/bandit7.password
```
## Level 8
to search for the word millionth, simply used grep command
```bash
$ data.txt|grep millionth
```
## Level 9
to get the unique line in the data file, used the sort and uniq command
```bash
$sort data.txt|uniq -u
```
## Level 10
on using the strings command, the string of continuous '=' was visible
```bash
$strings data.txt 
```

