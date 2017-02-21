# I hate russian hackers

## Problem description

You have an encrypted *.jpg image which you want to decrypt.

## Howto

It is known that the header of *.jpg files has a more or less long 0x01 block. Now when we use

    hd challenge.jpg | less

we can see that this block is gone:

    00000020  4d 35 39 41 42 55 47 0b  54 73 4d 35 39 41 42 55  |M59ABUG.TsM59ABU|
    00000030  47 0b 54 73 4d 35 39 41  42 55 47 0b 54 73 4d 35  |G.TsM59ABUG.TsM5|
    00000040  39 41 42 55 47 0b 54 73  4d 35 39 41 42 55 47 0b  |9ABUG.TsM59ABUG.|
    00000050  54 73 4d 35 39 41 42 55  47 f5 8e 72 0f 35 39 41  |TsM59ABUG..r.59A|
    00000060  42 55 47 0b 54 73 4d 35  39 41 42 55 47 0b 54 73  |BUG.TsM59ABUG.Ts|
    00000070  4d 35 39 41 42 55 47 0b  54 73 4d 35 39 41 42 55  |M59ABUG.TsM59ABU|
    00000080  47 0b 54 73 4d 35 39 41  42 55 47 0b 54 73 4d 35  |G.TsM59ABUG.TsM5|

Instead, the repeated occurence of 0x54 0x73 0x4d 0x35 0x39 0x41 0x42 0x55 0x47 0x0b can be noticed. So the image is encrypted by using
the very simplistic vignere encryption algorithm (with the key 0x54^0x01 0x73^0x01 0x4d^0x01 0x35^0x01 0x39^0x01 0x41^0x01 0x42^0x01 0x55^0x01 0x47^0x01, 0x0b^0x01
since we expect 0x01 to be at the corresponding positions). So to decrypt these images we can write a script like:

    key = [ 85, 114, 76, 52, 56, 64, 67, 84, 70, 10 ]
    
    chs = []
    with open("challenge.jpg", "rb") as inF:
        string = inF.read()
        for i, c in enumerate(string):
            chs.append(chr(key[i % len(key)] ^ ord(c)))
    
    with open("chEn.jpg", "wb") as outF:
        for c in chs:
            outF.write(c)

