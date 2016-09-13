GitFinder
==============
Thie identifies web sites with publicly accessible Git repositories. It simply checks if the ```.git/HEAD``` file contains ```refs/heads```. 

#Usage

```
> python gitfinder.py -h
usage: gitfinder.py [-h] [-i INPUTFILE] [-o OUTPUTFILE] [-t THREADS]

optional arguments:
  -h, --help            show this help message and exit
  -i INPUTFILE, --inputfile INPUTFILE
                        input file
  -o OUTPUTFILE, --outputfile OUTPUTFILE
                        output file
  -t THREADS, --threads THREADS
                        threads
```

The input file should contain the targets one per line. The script will output discovered URLs to stdout and to the OUTPUTFILE.
