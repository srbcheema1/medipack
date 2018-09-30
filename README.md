# MEDIPACK

[![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.ocm/srbcheema1/medipack/issues)
[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.png?v=103)](https://github.com/srbcheema1/medipack)
[![HitCount](http://hits.dwyl.io/srbcheema1/medipack.svg)](http://hits.dwyl.io/srbcheema1/medipack)

Medipack is `Media + Package`, A command-line tool used to `trim`, `crop`, `resize` media files.

[![Medipack](https://raw.githubusercontent.com/srbcheema1/medipack/master/extra/medipack-52x90.png)](https://pypi.org/project/medipack/)


### Installation

#### Build from Source

- `git clone https://github.com/srbcheema1/medipack`
- `cd medipack`
- `sudo python3 setup.py install`

#### Build from Source

```
sudo python3 -m pip install --user medipack

```

### Usage

```
usage: medipack [inp] [action {crop,trim,resize}] [suboptions] [-0 Output file]
```

```
suboptions are:
    trim        trim a video/audio file from given starting point to given ending point.
    crop        crop frame window of video.
    resize      resize the file by reducing video quality. to make small size video files.
```

```
For more help run:

medipack -h
medipack trim -h
medipack crop -h
medipack resize -h
```


### Supported formats

- mp4
- mp3

### supported actions

- trim
- crop
- resize

### Examples

#### trim

- trimming a video from 01:04 to 14:08
```
medipack input.mp4 -s 01:04 -e 14:08 -o output.mp4
medipack input.mp4 -s 01:04 -t 13:04 -o output.mp4
medipack input.mp4 -s 01:04 -e 14:08
medipack input.mp4 -s 01:04 -t 13:04
medipack input.mp4 trim
medipack trim
```
- trimming an audio from 01:04 to 14:08
```
medipack input.mp3 -s 01:04 -e 14:08 -o output.mp3
```

#### crop

- To crop the bottom right quarter of a video window
```
medipack input.mp4 crop -t 50 -l 50 -o output.mp4
medipack input.mp4 crop -t 50 -l 50
```

- To crop away top 10% of area
```
medipack input.mp4 crop -t 10 -o output.mp4
```

- To crop away right 20% of the area
```
medipack input.mp4 crop -r 20 -o output.mp4
```

- To crop away top 10% of area and right 20% of the area
```
medipack input.mp4 crop -t 10 -r 20 -o output.mp4
```

#### resize

- To resize a video to reduce its size
```
medipack input.mp4 resize -q 40 -o output.mp4
medipack input.mp4 resize -q 40
```

### Note

- For audio files only trim action is supported.
- If you dont provide output file then the outputfile will be names as <base>_output.<extension> for base.extension file.
- You may skip options, medikit is smart enough to detect or ask you the required options as per requirement
- In case of any bug/issue, Please report this to srbcheema2@gmail.com. Or, even better, submit a PR to fix it!


### Contact / Social Media

[![Github](https://raw.githubusercontent.com/srbcheema1/medipack/master/extra/github.png)](https://github.com/srbcheema1/)
[![LinkedIn](https://raw.githubusercontent.com/srbcheema1/medipack/master/extra/linkedin-48x48.png)](https://www.linkedin.com/in/srbcheema1/)
[![Facebook](https://raw.githubusercontent.com/srbcheema1/medipack/master/extra/fb.png)](https://www.facebook.com/srbcheema/)

### Development by

Developer / Author: [Srb Cheema](https://github.com/srbcheema1/)
