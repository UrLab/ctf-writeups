# Perquisition 3

**Forensics, 300 points**

## Problem description

>Thank you for your help, we could access to his email account. It helped us very much. While analyzing his mailbox, we found a draft of an email. Here it is :
>
>Dear Aleksei,
>
>The bomb is ready and is hidden in New Delhi.
>The only thing you now have to do is to load it with the plutonium.
>You will find the exact position of the bomb on the map joined to this email.
>
>Long live the Tsar !
>
>LYUBOV.
>
>Unfortunately, he did not yet add the attachment. Could you help us to locate the bomb ? Enter it's location in this format : LAT,LON with 6 decimal digits. (Example: "50.811966,4.384604")

## Solution

### Probing with Volatility

So we are looking at the same memory dump as earlier (Cf. Perquisition2), so we already know the profile, and we can take a second look at our pstree : 

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

There is a MSpaint process running too... maybe we can take a look at it? Let's dump it! We can use `volatility -f dump2.elf --profile=WinXPSP2x86 memdump -D . -p 408`, when done, volatility gives us :

    Volatility Foundation Volatility Framework 2.6
	************************************************************************
	Writing mspaint.exe [   408] to 408.dmp


### Find the image with Gimp

Now we can use Gimp to find what image was opened in MSpaint, for that, we first need to rename the `408.dmp` file to a `408.data` file. Then we can open it with Gimp. What we see is the raw data from the process. There is a lot of noise but we can play with the offset and the image width (here the width is 1600 and the offset is around 1560000) and we can see a photoshop screenshot appear with a location!

Here is our flag : 28.612879, 77.230021

FLAGGED!