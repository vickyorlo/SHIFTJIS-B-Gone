import codecs
import glob
import sys
import os

os.chdir(sys.argv[1])

for filetype in ['*.erb', '*.erh', '*.csv', '*.config']:
    for x in glob.glob('**/' + filetype, recursive=True):
        try:
            with codecs.open(x, mode='r', encoding='shiftjis') as file:
                lines = file.read()

            with codecs.open(x, mode='w', encoding='utf-8') as file:
                file.write(u'\uFEFF')
                for line in lines:
                    file.write(line)
            print(x + " converted")
        except UnicodeDecodeError:
            print(x + " looks like an UTF already")
