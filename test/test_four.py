#!/usr/bin/env python2
# -*- coding : utf8 -*-

import unittest
import re
from section.four import *


class TestSectionFour(unittest.TestCase):
    def setUp(self):
        """this is run before each test, we need to create a SectionFour object"""
        self.testee=SectionFour()


    def test_init(self):
        self.assertIsNotNone(self.testee)

    def test_sg_groupname_present(self):
        """testing that the function list_all_sg returns the right format 1/3"""
        #[{u'GroupName': 'toto42', u'GroupId': 'sg-xxxxx'}]
        for sgname, sgid in self.testee.list_all_sg():
            self.assertTrue('GroupName' in sgname) 

    def test_sg_groupid_present(self):
        """testing that the function list_all_sg returns the right format 2/3"""
        for sgname, sgid in self.testee.list_all_sg():
            self.assertTrue('GroupId' in sgid)

    def test_sg_id_format(self):
        """testing that the function list_all_sg returns the right format 3/3"""
        if self.testee.list_all_sg():
            # matching sg to format sg-12345678 regex sg-[0-9a-f]{8}
            self.assertTrue(re.match(r'sg-[0-9a-f]{8}',self.testee.list_all_sg()[0]['GroupId']))
    
    def test_rules_format(self):
        """testing that the function getrules() returns the right format"""
        if self.testee.getrules():
            self.assertTrue('FromPort' in self.testee.getrules()[0].keys())

    def tearDown(self):
        """this is run after  each test, we need to destroy the object"""
        del self.testee

if __name__ == '__main__':
    unittest.main()
