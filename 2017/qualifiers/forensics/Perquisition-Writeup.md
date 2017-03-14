# Perquisition 1 

**Forensics, 100 points**

## Problem description

> The SWAT just raided a terrorist home and found a computer.
> The sad news is that the hard disk was destroyed during the shooting.
> 
> The only thing our foresics team managed to recover is a dump from the RAM.
> 
> Find the password from the FLAG user account.

## Solution

You have a memorydump, the first thing you should do is pass it to Volatility to see if it's something current or unknown.

When you try to run `volatility -f dump.elf imageinfo`, you see :

    Volatility Foundation Volatility Framework 2.6
    INFO    : volatility.debug    : Determining profile based on KDBG search...
              Suggested Profile(s) : WinXPSP2x86, WinXPSP3x86 (Instantiated with WinXPSP2x86)
                         AS Layer1 : IA32PagedMemoryPae (Kernel AS)
                         AS Layer2 : VirtualBoxCoreDumpElf64 (Unnamed AS)
                         AS Layer3 : FileAddressSpace (/home/eligoan/Telechargements/chall/dump.elf)
                          PAE type : PAE
                               DTB : 0x3d7000L
                              KDBG : 0x8054d2e0L
              Number of Processors : 1
         Image Type (Service Pack) : 3
                    KPCR for CPU 0 : 0xffdff000L
                 KUSER_SHARED_DATA : 0xffdf0000L
               Image date and time : 2017-02-15 16:41:04 UTC+0000
         Image local date and time : 2017-02-15 08:41:04 -0800

You now know that you will be working with the `WinXPSP2x86` profile. Good news is, volatility knows it very well.

We know that we have to find a password. And we even know the username! So let's find all the passwords hashes.

We can create a hashdump of all the user's passwords with `volatility -f dump.elf --profile=WINXPSP2x86 hashdump` to see :

    Volatility Foundation Volatility Framework 2.6
    Administrator:500:b34ce522c3e4c87722c34254e51bff62:fc525c9683e8fe067095ba2ddc971889:::
    Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
    HelpAssistant:1000:9b45eefa50cbd1f779518231c8ae0fb3:8da1ecee0f0c121facdfb869612a33c6:::
    SUPPORT_388945a0:1002:aad3b435b51404eeaad3b435b51404ee:60a8616c6fd013a1aff2d7c3328b4af8:::
    IEUser:1003:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
    FLAG:1004:aad3b435b51404eeaad3b435b51404ee:ef5fdfb64c07b477daafaabe3dd20062:::

## Password cracking

We just need the "FLAG" line, and we run it through John-The-Ripper (Jumbo version) with the given wordlist. So we have `./john hash.txt --wordlist=dict.txt --format=NT`. And finally we can see the password appear

    Using default input encoding: UTF-8
    Loaded 1 password hash (NT [MD4 256/256 AVX2 8x3])
    Press 'q' or Ctrl-C to abort, almost any other key for status
    volutantibusque  (FLAG)
    1g 0:00:00:00 DONE (2017-03-14 16:05) 3.846g/s 7472Kp/s 7472Kc/s 7472KC/s volutantesque..volvantur
    Use the "--show" option to display all of the cracked passwords reliably
    Session completed

And here is our password : volutantibusque

FLAGGED!