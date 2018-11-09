#!/usr/bin/python
import urllib 

#urllib.urlretrieve('ftp://server/path/to/file', 'file')
# if you need to pass credentials:

urllib.urlretrieve('ftp://root:redhat@192.168.234.134/opt/minnu/scripts/perl/file_download/BH_DLY_PRE_888_ACT_20160808.csv', 'BH_DLY_PRE_888_ACT_20160808.csv')
#/opt/minnu/scripts/perl/file_download/BH_DLY_PRE_888_ACT_20160808.csv
