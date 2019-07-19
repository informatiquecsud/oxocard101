import sys
import os
from runestone import build  # build is called implicitly by the paver driver.
from runestone import get_master_url
from socket import gethostname
import pkg_resources
from sphinxcontrib import paverutils
from runestone.server import get_dburl
import paver
from paver.easy import *
import paver.setuputils
paver.setuputils.install_distutils_tasks()

sys.path.append(os.getcwd())

# The project name, for use below.
project_name = os.path.basename(os.path.dirname(os.path.abspath(__file__)))

master_url = 'http://localhost'
if not master_url:
    master_url = get_master_url()

# The root directory for ``runestone serve``.
serving_dir = "./build/" + project_name
# The destination directory for ``runestone deploy``.
dest = "./published"

options(
    sphinx=Bunch(docroot=".",),

    build=Bunch(
        builddir=serving_dir,
        sourcedir="_sources",
        outdir=serving_dir,
        confdir=".",
        template_args={'login_required': 'false',
                       'loglevel': 10,
                       'course_title': 'Oxocard\\ 101',
                       'python3': 'false',
                       'dburl': 'postgresql://user:password@localhost/runestone',
                       'default_ac_lang': 'python',
                       'jobe_server': 'http://jobe2.cosc.canterbury.ac.nz',
                       'proxy_uri_runs': '/jobe/index.php/restapi/runs/',
                       'proxy_uri_files': '/jobe/index.php/restapi/files/',
                       'downloads_enabled': 'true',
                       'enable_chatcodes': 'True',
                       'allow_pairs': 'True',
                       'dynamic_pages': False,
                       'use_services': True,
                       'basecourse': project_name,
                       # If ``dynamic_pages`` is 'True', then the following values are ignored, since they're provided by the server.
                       'course_id': project_name,
                       'appname': 'runestone',
                       'course_url': master_url,
                       }
    )
)

# if we are on runestone-deploy then use the proxy server not canterbury
if gethostname() == 'runestone-deploy':
    del options.build.template_args['jobe_server']
    del options.build.template_args['proxy_uri_runs']
    del options.build.template_args['proxy_uri_files']

version = pkg_resources.require("runestone")[0].version
options.build.template_args['runestone_version'] = version

# If DBURL is in the environment override dburl
options.build.template_args['dburl'] = get_dburl(outer=locals())
