#!/usr/bin/env python3

'''
convert using OS tools and copy tags after it
https://mutagen.readthedocs.io/
'''

import os
#import sys
from mutagen.flac import FLAC
#from mutagen.mp4 import MP4
#from mutagen.mp4 import MP4Tags
#from mutagen.mp4 import MP4Info

#SRC_DIR = 'flac'
#DST_DIR = 'm4a'
# quality: 0-127
# strategy: 0 CBR, 1 ABR, 2 VBR_constrained, 3 VBR
# file:  'mp4f' = MPEG-4 Audio (.mp4), 'm4af' = Apple MPEG-4 Audio (.m4a, .m4r)
#caffeinate find . -type f -name *.flac -exec afconvert -v -d aac -f m4af -q 127 -s 3 {} ../mzkDst/{}.m4a +
#CONVERT_CMD = "afconvert --data aac --file m4af --quality 127 --strategy 3 src-file dst-file"
# %%

#returned_value = os.system(cmd)  # returns the exit code in unix
#print('returned value:', returned_value)
FLACFILE = '01.flac'
M4AFILE = '01.m4a'

# EasyTag       FLAC            M4A
'''
Title           TITLE           ©nam
Artist          ARTIST          ©ART
Album Artist    ALBUMARTIST     aART
Album           ALBUM           alb
CD              DISCNUMBER=01   disk=(1, 1)
CD              DISCTOTAL=01    disk=(1, 1)
Year            DATE=2012       ©day=2011
Track           TRACKNUMBER=01  trkn=(1, 22)
Track           TRACKTOTAL=04   trkn=(1, 22)
Genre           GENRE           ©gen=tag - Genre
Comment         DESCRIPTION     ©cmt
Composer        COMPOSER        ©wrt
Orig.artist     PERFORMER
Copyright       COPYRIGHT       cprt
URL             CONTACT
Encoded by      ENCODED-BY      ©too
'''

def main(flacfile, m4afile):
    '''
    read tags from flac files and copy them to m4a files
    '''
    src = FLAC(flacfile)
    #dst = MP4(m4afile)
    print(src.pprint())


if __name__ == "__main__":
    #main(sys.argv[1:], sys.argv[2])
    main(FLACFILE, M4AFILE)
