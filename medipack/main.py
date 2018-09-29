#!/usr/bin/env python3
# PYTHON_ARGCOMPLETE_OK

import sys

from .lib.args import Args
from .lib.medipack import Medipack
from .lib.srbColour import Colour
from .lib.util import Util

'''
run it as:
    medipack inp.mp4 trim -s 0:30 -e 1:40

    to trim
        medipack inp.mp4 trim -s 0:30 -e 1:40 -o output.mp4
    to crop
        medipack inp.mp4 crop -w 50 -l 50 -x 50 -y 50 -o output.mp4
    to change quality/size
        medipack inp.mp4 qual -q 50 -o output.mp4

for audio, please specify output name using -o and extension should be mp3
    medipack inp.mp4 trim -s 0:30 -e 1:40 -o output.mp3
'''

def main():
    Util.verify_dependencies()
    parser = Args.get_parser()
    inp,out = Util.get_io(parser)

    # audio
    if(out.split('.')[-1] == 'mp3'):
        if (parser.action in ['crop','resize']):
            message = parser.action + ' not supported for mp3 output'
            Colour.print(message,Colour.RED)
            sys.exit(0)
        elif(parser.action == 'trim'):
            trimmer = Util.get_trimmer(parser)
            Medipack.aaudio_cutter(inp,trimmer,out)
        else:
            Colour.print('unknow action',Colour.YELLOW)
            sys.exit(0)

    # video
    if(parser.action == 'trim'):
        trimmer = Util.get_trimmer(parser)
        Medipack.video_trimmer(inp,trimmer,out)
    elif(parser.action == 'crop'):
        filters = Util.get_filters(parser)
        Medipack.video_cropper(inp,filters,out)
    elif(parser.action == 'resize'):
        resizer = Util.get_resizer(parser)
        Medipack.video_resizer(inp,resizer,out)
    else:
        Colour.print('unknow action',Colour.YELLOW)

if(__name__=="__main__"):
    main()
