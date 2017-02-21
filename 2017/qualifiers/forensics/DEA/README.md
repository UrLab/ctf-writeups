# DEA

## Problem description

This challenge consists out of a *.doc document. It is saied that this document was send by a drug dealer. Your job (for the challenge) is to find the city
where the drug dealer is hidding.

## Howto

When we open the *.doc document we can see that it principally contains an image. It should be well known that most cameras nowadays annotate each picture
with the location (GPS-coordinates) where it was taken. So let's check if the cameras the picture was taken with added the corresponding coordinates. To do
so we first need to extract the image of the *.doc document. In libre office this can be done by simply right clicking the image and then choose "Save image
as" (Probably there is a similar way to do it in Word). Once we have this image we have to read out the stored geolocations (they are stored in the EXIF
data header of an image). To do so an online tool like http://exifdata.com/ can be used. The corresponding city for this location coordinates can then be
found via google maps.
