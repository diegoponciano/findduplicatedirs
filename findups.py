import fnmatch
import itertools
import os
import os.path
import re
import sys
from tqdm import tqdm


if len(sys.argv) != 2:
    print("usage: %s directory" % sys.argv[0])
    exit(1)


directory = os.path.abspath(sys.argv[1])


includes = []  # for files only
excludes = ['.Trash-1000', '.Trashes', '.git']  # for dirs and files

# transform glob patterns to regular expressions
includes = r'|'.join([fnmatch.translate(x) for x in includes])
excludes = r'|'.join([fnmatch.translate(x) for x in excludes]) or r'$.'


# for root, dirs, files in os.walk(directory):
#     path, dirs, files = os.walk(directory).next()
#     count_files = (int(len(files)))
#     for i in tqdm.tqdm(range(count_files)):
#         time.sleep(0.1)
#         for fname in files:
#             full_fname = os.path.join(root, fname)


dircounter = 0
for dirpath, dirs, files in tqdm(os.walk(directory)):
    for dr in dirs:
        dircounter += 1

folders = []

for root, dirs, files in tqdm(os.walk(directory), total=dircounter):
    dirs[:] = [os.path.join(root, d) for d in dirs]
    dirs[:] = [d for d in dirs if not re.match(excludes, d)]

    for dr in dirs:
        folders.append(
            {'root': root[len(directory):],
             'directory': os.path.basename(dr)})

print(len(folders))

import pdb
pdb.set_trace()

folders = sorted(folders, key=lambda d: d['directory'])
folders2 = [{dr: list(flds)} for dr, flds in itertools.groupby(
    folders, key=lambda d: d['directory'])]
[i['root'] for i in list(folders2[11].values())[0]]
