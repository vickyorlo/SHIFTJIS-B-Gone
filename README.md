# SHIFTJIS-B-Gone
Script that gets rid of some of the plague that is non-unicode encoding.

Usage:

```shiftjisbgone.py [path to folder]```

The script will convert any SHIFT-JIS text file it finds into a glorious UTF-8 (with BOM, for reasons). Currently only works on .erb, .erh, .csv and .config files, but if you so require, you can change the list of extensions in the code.

If you want this script for just text files, replace line 8 with

```for filetype in ['*.txt']:```
