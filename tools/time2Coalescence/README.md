
# time2Coalescence.py

time2Coalescence.py takes a standard phylogeny json file.
This script works by first determining all IDs that have the
greatest origin_time (i.e. last generation). Then it atempts
to find the MRCA of these IDs. If IDs have more then one
parent then a set of MRCAs will be searched for instead.

This script requires the origin_time field.
This script assumes that an ancestor -1 is a progenitor. If
-1 is found as MRCA, script will report that no MRCA could
be found.

usage: time2Coalescence.py [-h] [-path PATH] [-file NAME] [-verbose]

optional arguments:
  -h, --help  show this help message and exit
  -path PATH  path to files - default : none (will read files in current
              directory)
  -file NAME  name of data file. default : lineageData.csv
  -verbose    adding this flag will provide more text output while running
              (useful if you are working with a lot of data to make sure that
              you are not hanging) - default (if not set) : OFF

