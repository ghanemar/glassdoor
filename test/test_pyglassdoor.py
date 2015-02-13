import unittest
import os
import pyglassdoor

keys = ['name', 'industry']


class TestGlassdoor(unittest.TestCase):

    def test_get_company(self):
        api = pyglassdoor.Api()
        c = api.get("ibm")
        print c
        try:
            self.assertTrue(all([k in c.keys() for c in keys]),
                            'Missing Keys')
        except Exception as e:
            raise Exception('get company failed: %s' % e)