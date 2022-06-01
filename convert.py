#!/usr/bin/env python3

import os
from mutagen.flac import FLAC
from mutagen.mp4 import MP4 MP4Tags MP4Info

srcDir = 'flac'
dstDir = 'm4a'
# quality: 0-127
# strategy: 0 CBR, 1 ABR, 2 VBR_constrained, 3 VBR
# file:  'mp4f' = MPEG-4 Audio (.mp4), 'm4af' = Apple MPEG-4 Audio (.m4a, .m4r)
cmd = "afconvert --data aac --file m4af --quality 127 --strategy 3 src-file dst-file"
# %%

#returned_value = os.system(cmd)  # returns the exit code in unix
#print('returned value:', returned_value)

class mutagen.mp4.MP4(filething):
