from setuptools import setup, find_packages
import os

import distribute_setup
distribute_setup.use_setuptools()

# disables creation of .DS_Store files inside tarballs on Mac OS X
os.environ['COPY_EXTENDED_ATTRIBUTES_DISABLE'] = 'true'
os.environ['COPYFILE_DISABLE'] = 'true'

def relative_path(path, srcdir='src'):
    return os.path.join(os.path.dirname(__file__), srcdir, path)

def get_tagged_version():
    import os.path, subprocess
    if(os.path.exists(relative_path('VERSION'))):
        with open(relative_path('VERSION'), 'rU') as f:
            version = f.read().strip()
    else:
        proc = subprocess.Popen(['git', 'describe', '--tags'],
            stderr  = subprocess.PIPE,
            stdout  = subprocess.PIPE,
            cwd     = os.path.dirname(__file__) or None
        )
        (stdoutdata, stderrdata) = proc.communicate()
        if(proc.returncode):
            raise RuntimeError(stderrdata)
        version = stdoutdata.strip().lstrip('v')

        print "writing version file..."
        with open(relative_path('VERSION'), 'w') as f:
            f.write(version)
    print 'package version: %s' % version
    return version

def autosetup():
    from setuptools import setup, find_packages
    return setup(
		name='django-moderation',

        packages        = find_packages('src'),

        entry_points    = {
            'setuptools.file_finders'   : [
                'git = setuptools_git:gitlsfiles',
            ],
        },

		version=get_tagged_version(),
		description="Generic Django objects moderation application",
		long_description=open("README.rst").read() + "\n" +
					   open(os.path.join("docs", "HISTORY.txt")).read(),

		classifiers=[
		'Development Status :: 4 - Beta',
		'Environment :: Web Environment',
		'Intended Audience :: Developers',
		'License :: OSI Approved :: BSD License',
		'Operating System :: OS Independent',
		'Programming Language :: Python',
		'Framework :: Django',
		],
		keywords='django moderation models',
		author='Dominik Szopa',
		author_email='dszopa@gmail.com',
		url='http://github.com/dominno/django-moderation',
		license='BSD',
		package_dir = {'': 'src'},
		include_package_data=True,
		install_requires=[
		  'setuptools',
		],
		zip_safe=False,
    )

if(__name__ == '__main__'):
    dist = autosetup()

