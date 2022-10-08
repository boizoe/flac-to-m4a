#!/usr/bin/env python3

'''
convert using OS tools and copy tags after it
https://mutagen.readthedocs.io/
'''

import os
from mutagen.flac import FLAC
from mutagen.mp4 import MP4
from mutagen.mp4 import MP4Cover

# %%

content = {}

def convert_flac_to_m4a(src, dst):
    '''
    search and convert from src to dst
    '''
    for root, dirs, files in os.walk(src):
        for file in files:
            if file.endswith('.flac'):
                newfile = os.path.splitext(file)[0] + '.m4a'
                newroot = dst + '/' + '/'.join(root.split('/')[1:])
                if not os.path.isdir(newroot):
                    os.makedirs(newroot)
                content[os.path.join(root, file)] = os.path.join(newroot, newfile)
    for item in content.items():
        if not os.path.isfile(item[1]):
            # quality: 0-127
            # strategy: 0 CBR, 1 ABR, 2 VBR_constrained, 3 VBR
            # file:  'mp4f' = MPEG-4 Audio (.mp4), 'm4af' = Apple MPEG-4 Audio (.m4a, .m4r)
            afconvert = "afconvert --data aac --file m4af --quality 127 --strategy 3 " + '"' + item[0] + '" "' + item[1] + '"'
            returned_value = os.system(afconvert) # returns the exit code in unix
            if returned_value != 0:
                print(afconvert)
            else:
                print('converting of ' + '"' + item[0] + '"' + ' succeed, copying tags')
                mtgn_copy_tags(item[0], item[1])


def mtgn_copy_tags(src, dst):
    '''
    read tags from flac files and copy them to m4a files
    '''
    src = FLAC(src)
    dst = MP4(dst)
    if 'TITLE' in src.tags:
        dst.tags['\xa9nam'] = src.tags['TITLE'][0]
    if 'ARTIST' in src.tags:
        dst.tags['\xa9ART'] = src.tags['ARTIST'][0]
    if 'ALBUMARTIST' in src.tags:
        dst.tags['aART'] = src.tags['ALBUMARTIST'][0]
    if 'ALBUM' in src.tags:
        dst.tags['\xa9alb'] = src.tags['ALBUM'][0]
    if 'GENRE' in src.tags:
        dst.tags['\xa9gen'] = src.tags['GENRE'][0]
    if 'DESCRIPTION' in src.tags:
        dst.tags['\xa9cmt'] = src.tags['DESCRIPTION'][0]
    if 'COMPOSER' in src.tags:
        dst.tags['\xa9wrt'] = src.tags['COMPOSER'][0]
    if 'COPYRIGHT' in src.tags:
        dst.tags['cprt'] = src.tags['COPYRIGHT'][0]
    if 'ENCODED-By' in src.tags:
        dst.tags['\xa9too'] = src.tags['ENCODED-BY'][0]
    if 'DATE' in src.tags:
        dst.tags['\xa9day'] = src.tags['DATE'][0]
    if 'TRACKNUMBER' in src.tags:
        if 'TRACKTOTAL' in src.tags:
            dst.tags['trkn'] = [(int(src.tags['TRACKNUMBER'][0]), int(src.tags['TRACKTOTAL'][0]))]
        else:
            dst.tags['trkn'] = [(int(src.tags['TRACKNUMBER'][0]), 0)]
    if 'DISCNUMBER' in src.tags:
        if 'DISCTOTAL' in src.tags:
            dst.tags['disk'] = [(int(src.tags['DISCNUMBER'][0]), int(src.tags['DISCTOTAL'][0]))]
        else:
            dst.tags['disk'] = [(int(src.tags['DISCNUMBER'][0]), 0)]
    if len(src.pictures) > 0:
        #probably I should check format
        #if f.pictures[0].mime == 'image/jpeg':
        dst.tags['covr'] = [MP4Cover(src.pictures[0].data)]
    dst.save()

def main():
    """
    main
    """
    convert_flac_to_m4a('mzkSrc', 'm4a')

if __name__ == "__main__":
    #main(sys.argv[1:], sys.argv[2])
    main()

# %%
