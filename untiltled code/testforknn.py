#!usr/bin/env python
# -*- coding：UTF-8-*-
import unittest
import classify0
import numpyknn
import numpy as ny

class testclassify(unittest.TestCase):
    def test_classify(self):
        cdata = [0.5, 0.6, 2]
        ydata = [[1.0, 1.1, 2.0], [1.0, 1.0, 2.2], [0, 0, 4.1], [0, 0.1, 4.5]]
        label = ['a', 'a', 'b', 'b']
        alist = classify0.classify(cdata, ydata, label, 3)
        self.assertEqual(alist,'a')

class testnumpy(unittest.TestCase):
    def test_numpy(self):
        cdata2 = ny.array([0.5, 0.6, 2])
        ydata2 = ny.array([[1.0, 1.1, 2.0], [1.0, 1.0, 2.2], [0, 0, 4.1], [0, 0.1, 4.5]])
        label = ['a', 'a', 'b', 'b']
        alist = numpyknn.classify0(cdata2, ydata2, label, 3)
        self.assertEqual(alist, 'a')
if __name__=='__main__':
    unittest.main()