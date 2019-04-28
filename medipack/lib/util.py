import os
import subprocess as sp
import sys

from .args import Args
from .meditor import Meditor
from .srbColour import Colour
from .time import Time

class Util:
    def get_filters(parser):
        filters = " "
        if(not parser.action == 'crop'):
            return filters

        Args.validate_crop_args(parser)

        crop_args = {}

        crop_args['x_point'] = str(parser.left/100)
        crop_args['y_point'] = str(parser.top/100)

        crop_args['width'] = str(1- (parser.left/100) - (parser.right/100))
        crop_args['height'] = str(1 - (parser.top/100) - (parser.down/100))

        filters = ' -filter:v "crop=in_w*'+crop_args['width']+':in_h*'+crop_args['height']+ \
            ':in_w*'+crop_args['x_point']+':in_h*'+crop_args['y_point']+'" '

        return filters

    def get_io(parser):
        if(not parser.inp):
            inp = input('Please enter input video file path : ')
            if(not os.path.exists(inp)):
                Colour.print('File diesnot exist',Colour.RED)
                sys.exit(0)
        else:
            inp = parser.inp

        if(not parser.output):
            if(parser.action == 'extract' and parser.audio):
                out = ''.join(inp.split('.')[:-1]) + '_output.mp3'
            else:
                out = ''.join(inp.split('.')[:-1]) + '_output.' + inp.split('.')[-1]
        else:
            out = parser.output

        if(os.path.exists(out)):
            Colour.print('[Warning] '+out+' file already exists',Colour.YELLOW)

        if(parser.action == 'extract'):
            out_ext = out.split('.')[-1]
            if(parser.video and out_ext == 'mp3'):
                Colour.print('[Warning] video output file with .mp3 extension',Colour.YELLOW)
                sys.exit(0)
            if(parser.audio and out_ext == 'mp4'):
                Colour.print('[Warning] audio output file with .mp4 extension',Colour.YELLOW)
                sys.exit(0)

        if(inp.split('.')[-1] == 'mp3' and out.split('.')[-1] == 'mp4'):
            Colour.print('[Warning] input file audio output file video',Colour.YELLOW)
            sys.exit(0)

        return inp,out

    def get_trimmer(parser,inp):
        trimmer = ' '
        if(not parser.action == 'trim'):
            return trimmer

        if(not parser.start):
            st = input('Please enter start-time in format hh:mm:ss or mm:ss : (default 00:00:00) : ')
            st.strip()
            if(st == ''):
                st = '00:00:00'
        else:
            st = parser.start
        st = Time.get_time(st)
        if(not st):
            Colour.print('Wrong format for start-time',Colour.RED)
            sys.exit(0)

        if(parser.time):
            t = parser.time
        else:
            if(parser.end):
                et = parser.end
            else:
                len_file = Meditor.getLength(inp)
                et = input('Please enter end-time in format hh:mm:ss or mm:ss : (default '+len_file+') : ')
                et.strip()
                if(et == ''): et = len_file
            et = Time.get_time(et)
            if(not et):
                Colour.print('Wrong format for end-time',Colour.RED)
                sys.exit(0)
            t = Time.get_relative_time(st,et)
            if(not t):
                Colour.print('end-time should be greater than start-time',Colour.RED)
                sys.exit(0)

        t = Time.get_time(t)
        if(not t):
            Colour.print('Wrong format for time duration',Colour.RED)
            sys.exit(0)

        trimmer = " -ss " +str(st)+ " -t " +str(t)
        return trimmer

    def get_resizer(parser):
        resizer = ' '
        if(not parser.action == 'resize'):
            return resizer

        if(parser.quality > 150):
            Colour.print('maximum value of quality is 150',Colour.RED)
            sys.exit(0)

        if(parser.quality < 0):
            Colour.print('quality cant be negative',Colour.RED)
            sys.exit(0)

        qual = parser.quality/100
        qual = 51 - qual*33
        '''
        actual crf (libx264) scale is from 0 to 51. normally 0 - 18 increase size so they are useless
        we will choose range from 18 to 51
        '''
        resizer = ' -crf ' + str(qual) + ' '
        return resizer
