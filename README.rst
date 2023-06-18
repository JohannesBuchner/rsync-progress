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

Contributing
------------

Contributions are welcome. Please open an issue or a pull request.

License: MIT
