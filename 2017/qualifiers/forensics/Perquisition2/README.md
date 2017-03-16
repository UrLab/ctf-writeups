# Perquisition 2

**Forensics, 150 points**

## Problem description

>Damnit, the password you recovered in the perquisition challenge is not the same as the one the terrorist uses for it's encrypted email account.
>
>In the meantime, we found a second computer with more information. Could you help us gain access to his email account ?

## Solution 

Like the first time we will run volatility on the .elf file with `volatility -f dump2.elf imageinfo` and see :

    Volatility Foundation Volatility Framework 2.6
    INFO    : volatility.debug    : Determining profile based on KDBG search...
          Suggested Profile(s) : WinXPSP2x86, WinXPSP3x86 (Instantiated with WinXPSP2x86)
                     AS Layer1 : IA32PagedMemoryPae (Kernel AS)
                     AS Layer2 : VirtualBoxCoreDumpElf64 (Unnamed AS)
                     AS Layer3 : FileAddressSpace (/home/eligoan/Telechargements/chall/dump2.elf)
                      PAE type : PAE
                           DTB : 0x3d7000L
                          KDBG : 0x8054d2e0L
          Number of Processors : 1
     Image Type (Service Pack) : 3
                KPCR for CPU 0 : 0xffdff000L
             KUSER_SHARED_DATA : 0xffdf0000L
           Image date and time : 2017-02-15 16:46:50 UTC+0000
     Image local date and time : 2017-02-15 08:46:50 -0800

So we are still working with the same `WINXPSP2x86` profile. The first thing we need to do is check what processes are running with `volatility -f dump2.elf --profile=WinXPSP2x86 pstree`. That gives us :

    Volatility Foundation Volatility Framework 2.6
	Name                                                  Pid   PPid   Thds   Hnds Time
	-------------------------------------------------- ------ ------ ------ ------ ----
	 0x810af490:System                                      4      0     54    280 1970-01-01 00:00:00 UTC+0000
	. 0x80efa3c0:smss.exe                                 368      4      3     19 2017-02-16 01:45:19 UTC+0000
	.. 0xffb4c8d8:csrss.exe                               544    368     11    411 2017-02-16 01:45:20 UTC+0000
	.. 0xffb4e3a0:winlogon.exe                            576    368     25    524 2017-02-16 01:45:20 UTC+0000
	... 0xffb3b5a8:services.exe                           648    576     16    259 2017-02-16 01:45:20 UTC+0000
	.... 0xffadf220:svchost.exe                          1152    648     15    188 2017-02-15 16:45:23 UTC+0000
	.... 0xffaabb20:svchost.exe                          1536    648      4     88 2017-02-15 16:45:32 UTC+0000
	.... 0xffabd2e8:spoolsv.exe                          1412    648     13    128 2017-02-15 16:45:24 UTC+0000
	.... 0xffb27020:VBoxService.exe                       816    648      8    105 2017-02-16 01:45:20 UTC+0000
	.... 0xffafa020:svchost.exe                           948    648      9    240 2017-02-15 16:45:22 UTC+0000
	.... 0xffa67940:svchost.exe                          2036    648      9     92 2017-02-15 16:45:59 UTC+0000
	.... 0xffa9b628:alg.exe                               196    648      7    104 2017-02-15 16:45:36 UTC+0000
	.... 0xffae5808:svchost.exe                          1100    648      5     60 2017-02-15 16:45:22 UTC+0000
	.... 0xffb1e838:svchost.exe                           860    648     21    213 2017-02-15 16:45:22 UTC+0000
	..... 0xffa4cb20:wmiprvse.exe                         592    860      8    176 2017-02-15 16:46:21 UTC+0000
	.... 0xff9cd620:svchost.exe                           448    648      8    132 2017-02-15 16:46:20 UTC+0000
	.... 0xffaee898:svchost.exe                          1044    648     73   1211 2017-02-15 16:45:22 UTC+0000
	..... 0xffa753b8:wuauclt.exe                         1908   1044      8    135 2017-02-15 16:45:33 UTC+0000
	... 0xffb3a198:lsass.exe                              660    576     26    368 2017-02-16 01:45:20 UTC+0000
	 0xffa74a58:explorer.exe                              868    556     15    424 2017-02-15 16:45:57 UTC+0000
	. 0xff9e34e8:mspaint.exe                              408    868      6    106 2017-02-15 16:46:20 UTC+0000
	. 0xff9fda88:notepad.exe                              304    868      1     35 2017-02-15 16:46:41 UTC+0000
	. 0xffa50418:VBoxTray.exe                            1328    868      7     66 2017-02-15 16:45:58 UTC+0000
	. 0xff9e39e8:cmd.exe                                 1980    868      1     30 2017-02-15 16:46:08 UTC+0000

So we can see that a notepad is open... maybe there is something in there? Let's check with `volatility -f dump2.elf --profile=WinXPSP2x86 notepad`. Good news! We see the following appear :

    Volatility Foundation Volatility Framework 2.6
    Process: 304
    Text:
    My passwords
    ============

    TODO : encrypt the file for better secutiry

    JEUXJEUXJEUX.fr: poeuqbckfhqzs7863fs
    snapchat : uiq!????hklqs
    hidden-mail-service.onion : v6HMxcPh763AFn7J

And here is our flag : v6HMxcPh763AFn7J

FLAGGED!