Progress bar for rsync
========================

Shows file progress and total progress as a progress bar.

Usage
---------
Run rsync with -P and pipe into this program. Example::

	rsync -P -avz user@host:/onefolder otherfolder/ | python rsyncprogress.py

It will show something like this::

	65%|30652/117251|################         |ETA:  0:04:20|File:100%|Illustris-3/...68/gas2_subhalo_5885.hdf5|0:00:00|156.48kB/s
	
	                                                               ^ File progress 
	                                                                     ^ File name                             ^ ETA  ^ Speed
	                  ^ Overall progress bar   ^ and ETA
	           ^ total number of files
	       ^ files to be checked
	^ Overall progress

You need the progressbar-latest package installed (see PyPI).

License
-----------
Copyright (c) 2015-2022 Johannes Buchner

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
