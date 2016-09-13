#!/usr/bin/python
import sys, os, argparse
from urllib.request import urlopen
from multiprocessing import Pool

def findgitrepo(url):
    url = url.strip()
    head_path = "/.git/HEAD"
    tmpl_checking = "\nChecking {} ... "

    try:
        # Try to download http://target.tld/.git/HEAD
        req = urlopen(url + head_path)
        answer = req.read(200).decode()

        # Check if refs/heads is in the file
        if(not 'refs/heads' in answer):
            print(tmpl_checking.format(url), end='')
            print("Nope. No refs/heads found.\n")
            return

        # Write match to OUTPUTFILE
        fHandle = open(OUTPUTFILE,'a')
        fHandle.write(url + head_path + "\n")
        fHandle.close()
        print(tmpl_checking.format(url), end='')
        print("Yes!\n")
        print("[*] Found: {}\n".format(url))

    except Exception as e:
        print(tmpl_checking.format(url), end='')
        print("Nope.")
        return

if __name__ == '__main__':

    # Parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--inputfile', default='urls.txt', help='input file')
    parser.add_argument('-o', '--outputfile', default='output.txt', help='output file')
    parser.add_argument('-t', '--threads', default=200, help='threads')
    args = parser.parse_args()

    URLFILE=args.inputfile
    OUTPUTFILE=args.outputfile
    MAXPROCESSES=int(args.threads)

    print("Scanning...")
    pool = Pool(processes=MAXPROCESSES)
    urls = open(URLFILE, "r").readlines()
    pool.map(findgitrepo, urls)

    print("\nAll done. Quit.")
