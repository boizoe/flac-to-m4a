# flac-to-m4a
convert flacs from source directory to m4a in destination directory and copy metadata and album art


python script takes 2 arguments 'src-dir' and 'dst-dir'.

1. convert 'src-dir's FLACs to 'dst-dir's M4As with afconvert or fdk_aac
2. copy metadata and album art FLACs to M4As

Notes:
a. 'src-dir' could contain any files, only dirs with FLACs are used
b. 'dst-dir' could not be empty. Script shouldn't overwrite any file/directory without asking
c. maybe it's better to scan src and dst beforehand
d. script should be able to write "logfile"
