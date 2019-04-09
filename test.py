
import os
import unittest

from pyfakefs.fake_filesystem_unittest import Patcher


class FakeFSTest(unittest.TestCase):
    def setUp(self):
        super(FakeFSTest, self).setUp()
        patcher = Patcher()
        patcher.setUp()
        self.addCleanup(patcher.tearDown)
        self.fs = patcher.fs

    def test_check_ownership(self):
        path = '/foo'
        self.fs.create_file(path, contents=b'something')
        os.chmod(path, mode=0)
        with self.assertRaises(PermissionError):
            open(path, 'rb')
