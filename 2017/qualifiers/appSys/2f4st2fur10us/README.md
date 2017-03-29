# 2f4st2fur10us
**AppSys, 150 points**
## Problem description

We SSH into a remote server and we want to read the content of a file "flag.txt". Unfortunately we do not have the needed rights to read the corresponding file directly (e.g. cat flag.txt).

## Solution
Luckily for us, we also notice that there is a script that does have the necessary permissions to interact with this file.
First we need to analyse the content of the script that is allowed to aceess the file "flag.txt". We can do so via:

    cat race_condition.sh

This shows us that the script is primarily doing the following:
 - copy the file containing the flag into the temp folder
 - make the copied file readable for everyone
 - sleep for a fraction of a second
 - delete the copy in the temp folder

Basically, after executing the script, the flag is readable by everyone but for a very short period of time making it impossible to access and read manually. However, we have the ability to run our own bash commands as we please. Hence, a simple solution springs to mind:
1. Execute race_condition.sh
2. Simultaneously have a loop that tries to print the contents of the (currently non-existant) flag file in the temp folder.

Here's an example of the code that does exactly that:

    sudo -u solution2_solved race_condition.sh & for i in {1..25}; do cat /tmp/flag.txt; done


After some errors due to the fact that the temp file does not exist in the beginning, eventually the *cat* command succeeds and we have the flag printed out to us!
Ta-da: `I think i'll take another nap {zzZzzZzzzZzzZzZzzzZ}`