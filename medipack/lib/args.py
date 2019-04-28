import os
import sys

try:
    import argparse
    from argcomplete import autocomplete
except:
    err = """
    You haven't installed the required dependencies.
    """
    print(err)
    sys.exit(0)

from .srbColour import Colour


class Args:
    def validate_crop_args(parser):
        if(not parser.action == 'crop'):
            return True

        if(parser.left + parser.right >= 100):
            message = 'Sum of value of left and right crop arguments should be from 0 to 99'
            Colour.print(message,Colour.RED)
            sys.exit(0)
        if(parser.left + parser.right >= 100):
            message = 'Sum of value of top and bottom crop arguments should be from 0 to 99'
            Colour.print(message,Colour.RED)
            sys.exit(0)


    def _is_valid_percent(parser, arg):
        try:
            arg = int(arg)
        except:
            parser.error("Percentage value should be an Integer value")
        if arg < 0 or arg > 100:
            parser.error("Percentage value should be in 0 to 100")
        else:
            return arg


    def _is_valid_file(parser, arg):
        if not os.path.exists(arg):
            parser.error("The file %s does not exist!" % arg)
        else:
            return arg


    def get_parser():
        class HelpFormatter(argparse.ArgumentDefaultsHelpFormatter, argparse.RawTextHelpFormatter):
            pass

        # parser = argparse.ArgumentParser(formatter_class=HelpFormatter)
        parser = argparse.ArgumentParser()

        parser.add_argument("-v","--version",
                            action='store_true',
                            help='Display version number')

        subparsers = parser.add_subparsers(dest='action')

        trim_parser = subparsers.add_parser('trim')
        trim_parser.add_argument("inp",nargs='?',
                                type=lambda x: Args._is_valid_file(trim_parser,x),
                                help="input video file ex: input.mp4")
        trim_parser.add_argument("-s", "--start",
                                help="start time for cuting in format hh:mm:ss or mm:ss")
        time_group = trim_parser.add_mutually_exclusive_group()
        time_group.add_argument("-e", "--end",
                                help="end time for cuting in format hh:mm:ss or mm:ss")
        time_group.add_argument("-t", "--time",
                                help="clip duration in format hh:mm:ss or mm:ss")
        trim_parser.add_argument("-o", "--output",
                                help="output file name, ex: output.mp4")


        crop_parser = subparsers.add_parser('crop',formatter_class=HelpFormatter)
        crop_parser.add_argument("inp",nargs='?',
                                type=lambda x: Args._is_valid_file(crop_parser,x),
                                help="input video file ex: input.mp4")
        crop_parser.add_argument("-t", "--top",
                                default=0,
                                type=lambda x: Args._is_valid_percent(crop_parser,x),
                                help="percentage of screen to be chopped from top")
        crop_parser.add_argument("-b", "--bottom",
                                default=0,
                                type=lambda x: Args._is_valid_percent(crop_parser,x),
                                help="percentage of screen to be chopped from bottom")
        crop_parser.add_argument("-l", "--left",
                                default=0,
                                type=lambda x: Args._is_valid_percent(crop_parser,x),
                                help="percentage of screen to be chopped from left")
        crop_parser.add_argument("-r", "--right",
                                default=0,
                                type=lambda x: Args._is_valid_percent(crop_parser,x),
                                help="percentage of screen to be chopped from right")
        crop_parser.add_argument("-o", "--output",
                                help="output file name, ex: output.mp4")


        resize_parser = subparsers.add_parser('resize')
        resize_parser.add_argument("inp",nargs='?',
                                    type=lambda x: Args._is_valid_file(trim_parser,x),
                                    help="input video file ex: input.mp4")
        resize_parser.add_argument("-q", "--quality",
                                    type=int,default=50,
                                    help="output video quality (on scale of 100) (default: 50)")
        resize_parser.add_argument("-o", "--output",
                                    help="output file name, ex: output.mp4")


        extract_parser = subparsers.add_parser('extract')
        extract_parser.add_argument("inp",nargs='?',
                                    type=lambda x: Args._is_valid_file(trim_parser,x),
                                    help="input video file ex: input.mp4")
        extract_group = extract_parser.add_mutually_exclusive_group(required=True)
        extract_group.add_argument("-v","--video",
                                    action='store_true')
        extract_group.add_argument("-a","--audio",
                                    action='store_true')
        extract_parser.add_argument("-o", "--output",
                                    help="output file name")


        autocomplete(parser)
        parsed_args = parser.parse_args()
        if(not parsed_args.version and not parsed_args.action):
            Colour.print('requires atleast one command line argument',Colour.RED)
            parser.print_help(sys.stderr)
            sys.exit(1)
        return parsed_args
