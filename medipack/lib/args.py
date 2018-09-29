import os
import sys

try:
    from argparse import ArgumentParser
    from argcomplete import autocomplete
except:
    err = """
    You haven't installed the required dependencies.
    """
    print(err)
    sys.exit(0)



class Args:
    def validate_crop_args(args):
        return

    def _is_valid_file(parser, arg):
        if not os.path.exists(arg):
            parser.error("The file %s does not exist!" % arg)
        else:
            return arg

    def get_parser():
        parser = ArgumentParser()
        parser.add_argument("inp",nargs='?',
                            type=lambda x: Args._is_valid_file(trim_parser,x),
                            help="input video file ex: input.mp4")
        subparsers = parser.add_subparsers(dest='action')

        trim_parser = subparsers.add_parser('trim')
        trim_parser.add_argument("-s", "--start_time", help="start time for cuting in format hh:mm:ss or mm:ss")
        time_group = trim_parser.add_mutually_exclusive_group()
        time_group.add_argument("-e", "--end_time", help="end time for cuting in format hh:mm:ss or mm:ss")
        time_group.add_argument("-t", "--time", help="clip duration in format hh:mm:ss or mm:ss")
        trim_parser.add_argument("-o", "--output",help="output file name, ex: output.mp4")

        crop_parser = subparsers.add_parser('crop')
        crop_parser.add_argument("-w", "--width",type=int,default=100,help="crop video window width (on scale of 100)")
        crop_parser.add_argument("-l", "--height",type=int,default=100,help="crop video window height (on scale of 100)")
        crop_parser.add_argument("-x", "--x_point",type=int,default=0,help="crop video window top-left points x (on scale of 100)")
        crop_parser.add_argument("-y", "--y_point",type=int,default=0,help="crop video window top-left points y (on scale of 100)")
        crop_parser.add_argument("-o", "--output",help="output file name, ex: output.mp4")

        resize_parser = subparsers.add_parser('resize')
        resize_parser.add_argument("-q", "--quality",type=int,default=100,help="output video quality (on scale of 100)")
        resize_parser.add_argument("-o", "--output",help="output file name, ex: output.mp4")


        autocomplete(parser)
        parser = parser.parse_args()
        return parser
