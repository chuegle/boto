# Copyright (c) 2006,2007 Mitch Garnaat http://garnaat.org/
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
#
import boto2
from boto2.pyami.scriptbase import ScriptBase
import os, StringIO

class CopyBot(ScriptBase):

    def __init__(self):
        ScriptBase.__init__(self)
        self.wdir = boto2.config.get('Pyami', 'working_dir')
        self.log_file = '%s.log' % self.instance_id
        self.log_path = os.path.join(self.wdir, self.log_file)
        boto2.set_file_logger(self.name, self.log_path)
        self.src_name = boto2.config.get(self.name, 'src_bucket')
        self.dst_name = boto2.config.get(self.name, 'dst_bucket')
        self.replace = boto2.config.getbool(self.name, 'replace_dst', True)
        s3 = boto2.connect_s3()
        self.src = s3.lookup(self.src_name)
        if not self.src:
            boto2.log.error('Source bucket does not exist: %s' % self.src_name)
        dest_access_key = boto2.config.get(self.name, 'dest_aws_access_key_id', None)
        if dest_access_key:
            dest_secret_key = boto2.config.get(self.name, 'dest_aws_secret_access_key', None)
            s3 = boto2.connect(dest_access_key, dest_secret_key)
        self.dst = s3.lookup(self.dst_name)
        if not self.dst:
            self.dst = s3.create_bucket(self.dst_name)

    def copy_bucket_acl(self):
        if boto2.config.get(self.name, 'copy_acls', True):
            acl = self.src.get_xml_acl()
            self.dst.set_xml_acl(acl)

    def copy_key_acl(self, src, dst):
        if boto2.config.get(self.name, 'copy_acls', True):
            acl = src.get_xml_acl()
            dst.set_xml_acl(acl)

    def copy_keys(self):
        boto2.log.info('src=%s' % self.src.name)
        boto2.log.info('dst=%s' % self.dst.name)
        try:
            for key in self.src:
                if not self.replace:
                    exists = self.dst.lookup(key.name)
                    if exists:
                        boto2.log.info('key=%s already exists in %s, skipping' % (key.name, self.dst.name))
                        continue
                boto2.log.info('copying %d bytes from key=%s' % (key.size, key.name))
                prefix, base = os.path.split(key.name)
                path = os.path.join(self.wdir, base)
                key.get_contents_to_filename(path)
                new_key = self.dst.new_key(key.name)
                new_key.set_contents_from_filename(path)
                self.copy_key_acl(key, new_key)
                os.unlink(path)
        except:
            boto2.log.exception('Error copying key: %s' % key.name)

    def copy_log(self):
        key = self.dst.new_key(self.log_file)
        key.set_contents_from_filename(self.log_path)
        
    def main(self):
        fp = StringIO.StringIO()
        boto2.config.dump_safe(fp)
        self.notify('%s (%s) Starting' % (self.name, self.instance_id), fp.getvalue())
        if self.src and self.dst:
            self.copy_keys()
        if self.dst:
            self.copy_log()
        self.notify('%s (%s) Stopping' % (self.name, self.instance_id),
                    'Copy Operation Complete')
        if boto2.config.getbool(self.name, 'exit_on_completion', True):
            ec2 = boto2.connect_ec2()
            ec2.terminate_instances([self.instance_id])
        
