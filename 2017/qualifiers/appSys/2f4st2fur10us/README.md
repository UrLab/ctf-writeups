# 2f4st2fur10us

## Problem description

We are on a remote server and we want to read the content of a file "flag.txt". Unfortunately we do not have the needed rights to read the corresponding
file directly (e.g. cat flag.txt). But there is a script (I forgot the exact name of this script) that can process this file.

## Howto

First we need to analyse the content of the script that is allowed to process the file "flag.txt". We can do so via:

cat [the_script_name_I_forgot.sh]

We will see that the script is principally doing the following:
 - copy the file into the temp folder
 - make the copied file readable for everyone
 - sleep for the fraction of some milliseconds
 - delete the copy in the temp folder

As can be seen everyone can access the file for the fraction of some milliseconds. So we need to execute the command and then (via a race condition)
access the copy in the tmp folder - like so:

sudo -u solution2_solved [the_script_name_I_forgot.sh] & for i in {1..25}; do cat /tmp/[the_hidden_tmp_file_name]; done
