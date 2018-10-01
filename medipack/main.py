#!/usr/bin/env python3
# PYTHON_ARGCOMPLETE_OK

import sys

from .lib.args import Args
from .lib.meditor import Meditor
from .lib.srbColour import Colour
from .lib.util import Util
from .dependencies.dependency import install_dependencies

'''
run it as:
    medipack inp.mp4 trim -s 0:30 -e 1:40

    to trim
        medipack inp.mp4 trim -s 0:30 -e 1:40 -o output.mp4
    to crop
        medipack inp.mp4 crop -t 10 -l 10 -b 10 -r 20 -o output.mp4
    to change quality/size
        medipack inp.mp4 resize -q 50 -o output.mp4

for audio, please specify output name using -o and extension should be mp3
    medipack inp.mp4 trim -s 0:30 -e 1:40 -o output.mp3
'''


dependency_map = {
    'register-python-argcomplete':{
        'ubuntu':'sudo apt install python-argcomplete',
    },
    'ffmpeg':{
        'ubuntu':'sudo apt install ffmpeg',
    },
}

def main():
    parser = Args.get_parser()
    if(not install_dependencies(dependency_map)):
        print('please install the required dependencies')
        sys.exit(0)

    inp,out = Util.get_io(parser)
    if(parser.action == 'extract'):
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
            trimmer = Util.get_trimmer(parser)
            Meditor.aaudio_cutter(inp,trimmer,out)
        else:
            Colour.print('unknow action',Colour.YELLOW)
            sys.exit(0)

    # video
    if(parser.action == 'trim'):
        trimmer = Util.get_trimmer(parser)
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
