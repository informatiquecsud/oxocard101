import re
import sys
import os
import shutil


def log(msg, obj):
    if debug:
        if obj:
            msg = msg + ' : ' + str(obj)
        print(msg)


def get_default_exts(asset_type):
    if asset_type in ['figure']:
        return ['jpe?g', 'png', 'gif']


def extract_assets(rst_source, asset_type='figure', exts=None):
    '''

    link to regex : https://regex101.com/r/KtKMuz/2

    '''
    exts = exts or get_default_exts(asset_type)
    regex = r'(?P<directive>{directive})::\s+(?P<filename>[A-Za-z0-9y-]+.(?P<file_extension>{exts}))'.format(
        exts='|'.join(exts),
        directive=asset_type
    )
    pattern = re.compile(regex, re.MULTILINE | re.IGNORECASE)
    return [m.group('filename') for m in pattern.finditer(rst_source)]


def copy_assets(filenames, dest_dir):
    for f in filenames:
        src_file = os.path.join('mdfiles', f)
        log('Copying file to destination dir', src_file)
        shutil.copy2(src_file, dest_dir)


if __name__ == '__main__':
    # TODO: for now this is nonsens ... -i read directly from stdin
    rst_source = sys.stdin.read()
    dest_dir = sys.argv[1]

    debug = False

    if '-d' in sys.argv:
        debug = True

    # make directory
    dest_dir = os.path.join('_sources', dest_dir)
    log('Creating destination directory : ', dest_dir)
    try:
        os.mkdir(dest_dir)
    except Exception as e:
        log("Error creating destination directory", str(e))
    # write the rst into index.rst
    dest_index_rst = os.path.join(dest_dir, 'index.rst')
    with open(dest_index_rst, 'w') as fd:
        log('Writing rst to file', dest_index_rst)
        fd.write(rst_source)
    # get asset filenames
    filenames = extract_assets(rst_source, asset_type='figure')
    # copy all the assets
    copy_assets(filenames, dest_dir)

# TODOS
#
# 1) add a better cli options system
# 2) use ``sh`` module to run pandoc directly on specified file (or * glob) and
#    read rst source from pandoc output. Use the path from the input file to
#    determine relative location of assets and copy in subdirectory depending on
#    the asset type (figure|code-block|...)
# 3) Use md filename to process as base for directory name in target _source dir
# 4) One could also use a magic comment (or special sequence) that could
#    indicate the destination directory
# 5) Rewrite the rst source like so (xxx.png) => (figures/xxx.png) and put the
#    assets in a directory like ``figures``
