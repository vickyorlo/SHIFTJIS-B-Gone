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
                x + 'is not a shift-jis encoded file! Youre gonna have to deal with it yourself.')
            notconverted.append(x)

print("not converted:")
print(notconverted)
