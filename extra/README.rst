MEDIPACK
^^^^^^^^

Medipack is `Media + Package`, A command-line tool used to `trim`, `crop`, `resize` media files.


Supported formats
^^^^^^^^^^^^^^^^^

-  mp4
-  mp3

Supported Actions
^^^^^^^^^^^^^^^^^

-  trim
-  crop
-  resize

Installation
^^^^^^^^^^^^

Build from source
'''''''''''''''''

-  ``git clone https://github.com/srbcheema1/medipack``
-  ``cd medipack``
-  ``python3 setup.py install``

As a Python package
'''''''''''''''''''

::

    sudo pip3 install --user medipack

Usage
^^^^^

::

    usage: medipack [inp] [action {crop,trim,resize}] [suboptions] [-0 Output file]





Examples
^^^^^^^^

-  Trim a video with given starting and ending point

   ::

       medipack input.mp4 trim -s 01:04 -e 14:08 -o output.mp4

-  Trim a video with given starting point and clip length

   ::

       medipack input.mp4 trim -s 01:04 -t 13:04 -o output.mp4

-  Trim an audio file with given starting and ending point

   ::

       medipack input.mp3 trim -s 01:04 -e 14:04 -o output.mp3

-  Resize a video with quality 50%

   ::

       medipack input.mp4 resize -q 50

-  Crop a video and get lower-bottom quarter

   ::

       medipack input.mp4 crop -x 50 -y 50 -w 50 -l 50 -o output.mp4


Note :
''''''

-  For audio files only *trim* action is supported.

-  If you dont provide output file then the outputfile will be names as <base>_output.<extension> for base.extension file.

-  You may skip options, medikit is smart enough to detect or ask you the required options as per requirement

-  In case of any bug/issue, Please report this to srbcheema2@gmail.com. Or, even better, submit a PR to fix it!


Developer / Author :    Srb Cheema
''''''''''''''''''

