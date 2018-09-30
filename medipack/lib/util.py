import os
import subprocess as sp
import sys

from .srbColour import Colour
from .time import Time
from .args import Args

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
        crop_args['height'] = str(1 - (parser.top/100) - (parser.right/100))

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
            out = ''.join(inp.split('.')[:-1]) + '_output.' + inp.split('.')[-1]
        else:
            out = parser.output

        if(os.path.exists(out)):
            Colour.print('[Warning] '+out+' file already exists',Colour.YELLOW)
        return inp,out

    def get_trimmer(parser):
        trimmer = ' '
        if(not parser.action == 'trim'):
            return trimmer

        if(not parser.start_time):
            st = input('Please enter start time in format hh:mm:ss or mm:ss : ')
        else:
            st = parser.start_time
        st = Time.get_time(st)
        if(not st):
            Colour.print('Wrong format for start-time',Colour.RED)
            sys.exit(0)

        if(not parser.time and not parser.end_time):
            t = input('Please enter time duration in format hh:mm:ss or mm:ss : ')
        elif(not parser.time):
            t = parser.end_time
            t = Time.get_time(t)
            if(not t):
                Colour.print('Wrong format for end_time',Colour.RED)
                sys.exit(0)
            t = Time.get_relative_time(st,t)
            if(not t):
                Colour.print('end_time should be greater than start_time',Colour.RED)
                sys.exit(0)
        else:
            t = parser.time

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
