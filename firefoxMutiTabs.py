#!/usr/bin/env python

import subprocess

# fill in your firefox.exe path
firefox_path = ""
cmdline = [firefox_path]


with open('url_list.txt', 'r') as url_file:
    for url in url_file:
        cmdline.append(url)
subprocess.Popen(cmdline)
