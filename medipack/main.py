#!/usr/bin/env python3
# PYTHON_ARGCOMPLETE_OK

import sys

from . import __mod_name__, __version__

from .dependencies.dependencies import dependency_map
from .dependencies.dependency import install_dependencies
from .lib.args import Args
from .lib.meditor import Meditor
from .lib.srbColour import Colour
from .lib.util import Util

'''
run it as:
    medipack trim inp.mp4 -s 0:30 -e 1:40

    to trim
        medipack trim inp.mp4 -s 0:30 -e 1:40 -o output.mp4
    to crop
        medipack crop inp.mp4 -t 10 -l 10 -b 10 -r 20 -o output.mp4
    to change quality/size
        medipack resize inp.mp4 -q 50 -o output.mp4
        medipack resize inp.mp4
    to extract audio
        medipack extract --audio inp.mp4 -o out.mp3
    to extract video
        medipack extract --video inp.mp4 -o out.mp4

for audio output, please specify ensure mp3 in output name
    medipack extract --audio inp.mp4 -o out.mp3             (WORKS)
    medipack extract --audio inp.mp4 -o out.mp4             (WILL FAIL)
    medipack trim inp.mp3 -s 0:30 -e 1:40 -o output.mp3     (WORKS)
'''


def main():
    parser = Args.get_parser()
    if(not install_dependencies(dependency_map)):
        print('please install the required dependencies')
        sys.exit(1)

    if parser.version:
        print(__mod_name__+'=='+__version__)
        sys.exit()


    inp,out = Util.get_io(parser)
    if(parser.action == 'extract'):
        if(inp.split('.')[-1] == 'mp3'):
            message = parser.action + ' not supported for audio inpput'
            Colour.print(message,Colour.RED)
            sys.exit(0)
        if(parser.audio):
            Meditor.extract_audio(inp,out)
        if(parser.video):
            Meditor.extract_video(inp,out)
        sys.exit(0)

    # audio
    if(out.split('.')[-1] == 'mp3'):
        if (parser.action in ['crop','resize']):
            message = parser.action + ' not supported for mp3 output'
            Colour.print(message,Colour.RED)
            sys.exit(0)
        elif(parser.action == 'trim'):
            trimmer = Util.get_trimmer(parser,inp)
            Meditor.aaudio_cutter(inp,trimmer,out)
        else:
            Colour.print('unknow action',Colour.YELLOW)
            sys.exit(0)

    # video
    if(parser.action == 'trim'):
        trimmer = Util.get_trimmer(parser,inp)
        Meditor.video_trimmer(inp,trimmer,out)
    elif(parser.action == 'crop'):
        filters = Util.get_filters(parser)
        Meditor.video_cropper(inp,filters,out)
    elif(parser.action == 'resize'):
        resizer = Util.get_resizer(parser)
        Meditor.video_resizer(inp,resizer,out)
    else:
        Colour.print('unknow action',Colour.YELLOW)

if(__name__=="__main__"):
    main()
