# Pr1s0n Br34k

## Problem description

Here you are caught in a nasty program (called jail.sh). This program is principally emulating a bash, but you do not have any standard programs to your disposion like
cat, less, more, head, tail, grep, cut, awk, sed ... but only shell build in commands like help, alias, etc.. Furthermore all bash variables are getting deleted (before
the execution of the next line you enter in this shell).

## Howto

You want to list the content of the directory but unfortunately you do not have the ls command. So you have to use a workaround with the "*" buildin like:

for file in *; do echo $file; done

(Or you simply ssh onto the same server via the account of the problem statement 2f4st2fur10us. Once on the server (but with another user) you can find the challenge1
users home directory and lists its content via ls -la (because for this user the ls command is not blocked) ... this gives you the same result.)

Once you have the file list you can see that a file named "flag.txt" exists (Unfortunately due to the permissions of this files you cannot simply read it out via the user
of problem statement 2f4st2fur10us, it would have been to easy). Of course you want to get the file content. There are multiple ways to read out a file content via shell
buildins commands alone. One way is to write a stupid for loop in order to iterate over the file content. But I prefer the much more shorter command:

echo $(<flag.txt)

Once you have read out the file content you are done. The flag is part of the file content.

## Misc

You can execute the command "jail.sh" in the "jail.sh" itself. Every time you enter a new command you will then get the message that jail.sh failed in line 11 because
the sed command is not available ... So the sed command is available (/bin/sed) - it is just you can not execute it.

You can kill the jail.sh by typing "kill [pid of the jail.sh process]". You can get the pid of the jail.sh process by executing "ps aux" when you are logged into a second
terminal on the server via the account of problem statement 2f4st2fur10us. But when you do this the connection to the server gets closed. So like this - unfornuately -
there is no way to kill "jail.sh" and get this files (or the flags) content. 

You may try to close or pause "jail.sh" via Ctrl+D or Ctrl+Z you will only get a message that you cannot escape.

You can write "exec flag.txt" in order to execute the file content. But this will only give you the first word of every line of flag.txt - which is unfortunately not
enough to get the flags content.

## Open questions

After the end of the qualification round I began to wonder if you can bypass the restrictions of the jail.sh by editing the PATH command - via something like:

PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin;cat flag.txt

or even more stupid

/bin/cat flag.txt

(Since I can not try this anymore it would be nice to hear from another group who tried this.)
