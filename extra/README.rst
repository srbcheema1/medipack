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


Note :
''''''

-  For audio files only *trim* action is supported.

-  If you dont provide output file then the outputfile will be names as <base>_output.<extension> for base.extension file.

-  You may skip options, medikit is smart enough to detect or ask you the required options as per requirement

-  In case of any bug/issue, Please report this to srbcheema2@gmail.com. Or, even better, submit a PR to fix it!


Developer / Author :    Srb Cheema
''''''''''''''''''

