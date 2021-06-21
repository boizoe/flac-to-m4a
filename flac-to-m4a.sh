#!/usr/bin/env bash

caffeinate find . -type f -name *.flac -exec afconvert -v -d aac -f m4af -q 127 -s 3 {} ../mzkDst/{}.m4a \;
