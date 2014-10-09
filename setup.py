#!/usr/bin/python

# Copyright (c) 2006-2009 Mitch Garnaat http://garnaat.org/
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish, dis-
# tribute, sublicense, and/or sell copies of the Software, and to permit
# persons to whom the Software is furnished to do so, subject to the fol-
# lowing conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABIL-
# ITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT
# SHALL THE AUTHOR BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, 
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

from boto1 import Version

setup(name = "boto1",
      version = Version,
      description = "Amazon Web Services Library",
      long_description="Python interface to Amazon's Web Services.",
      author = "Mitch Garnaat",
      author_email = "mitch@garnaat.com",
      scripts = ["bin/sdbadmin", "bin/elbadmin", "bin/s3put", "bin/fetch_file", "bin/launch_instance", 'bin/list_instances', "bin/taskadmin"],
      url = "http://code.google.com/p/boto/",
      packages = [ 'boto1', 'boto1.sqs', 'boto1.s3',
                   'boto1.ec2', 'boto1.ec2.cloudwatch', 'boto1.ec2.autoscale', 'boto1.ec2.elb',
                   'boto1.sdb', 'boto1.sdb.persist', 'boto1.sdb.db', 'boto1.sdb.db.manager',
                   'boto1.mturk', 'boto1.pyami', 'boto1.mashups', 'boto1.contrib', 'boto1.manage',
                   'boto1.services', 'boto1.tests', 'boto1.cloudfront', 'boto1.rds', 'boto1.vpc',
                   'boto1.fps'],
      license = 'MIT',
      platforms = 'Posix; MacOS X; Windows',
      classifiers = [ 'Development Status :: 3 - Alpha',
                      'Intended Audience :: Developers',
                      'License :: OSI Approved :: MIT License',
                      'Operating System :: OS Independent',
                      'Topic :: Internet',
                      ],
      )
