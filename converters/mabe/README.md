
# mabeData2stdPhylogeny.py 

converts mabe data files to standard phylogeny format.
Output generates lineage.json and lineage.csv

usage: mabeData2stdPhylogeny.py [-h] [-path PATH] [-fileType TYPE]
                                [-columnNames COLUMN_NAME [COLUMN_NAME ...]]
                                [-newColumnNames COLUMN_NAME [COLUMN_NAME ...]]
                                -updateRange FIRST LAST STEP [-verbose]

optional arguments:
  -h, --help            show this help message and exit
  -path PATH            path to files - default : none (will read files in
                        current directory)
  -fileType TYPE        type of file, snapshot or SSwD, default : snapshot
  -columnNames COLUMN_NAME [COLUMN_NAME ...]
                        column names of data to read from source files -
                        default : ID score_AVE timeOfBirth (will automatically
                        include ancestors)
  -newColumnNames COLUMN_NAME [COLUMN_NAME ...]
                        column names of data to be copied into new data file -
                        default : ID score timeOfBirth (will automatically
                        include parents)
  -updateRange FIRST LAST STEP
                        update range first, last, step
  -verbose              adding this flag will provide more text output while
                        running (useful if you are working with a lot of data
                        to make sure that you are not hanging) - default (if
                        not set) : OFF
