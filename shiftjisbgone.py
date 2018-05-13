import codecs
import glob
import sys
import os

os.chdir(sys.argv[1])

notconverted = list()

for filetype in ['*.erb', '*.erh', '*.csv', '*.config']:
    for x in glob.glob('**/' + filetype, recursive=True):
        try:
            raw = open(x, 'rb').read(3)
            if raw == b'\xef\xbb\xbf':
                print(x + " looks like an UTF-8 with BOM already")
                continue

            with codecs.open(x, mode='r', encoding='shift_jis') as file:
                lines = file.read()

            with codecs.open(x, mode='w', encoding='utf-8') as file:
                file.write(u'\uFEFF')
                for line in lines:
                    file.write(line)
            print(x + " converted")
        except UnicodeDecodeError:
            print(
                x + 'is not a shift-jis encoded file!')
            notconverted.append(x)

if notconverted.__len__() > 0:
    print("not converted:")
    print(notconverted)

    print("\nI'm going to try decoding it as a shift_jis2004 file. This may not necessarily work.")

    for x in notconverted:
        try:
            with codecs.open(x, mode='r', encoding='shiftjis2004') as file:
                lines = file.read()

            with codecs.open(x, mode='w', encoding='utf-8') as file:
                file.write(u'\uFEFF')
                for line in lines:
                    file.write(line)
            print(x + " converted")
        except UnicodeDecodeError:
            print(
                x + ' did not decode, you are on your own.')
