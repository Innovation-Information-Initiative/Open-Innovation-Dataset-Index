#!/usr/bin/env python
"""
check_frontmatter.py
Adapted from: Kevin Fronczak
Date: July 25, 2017

Usage:
	python3 check_frontmatter.py [tests]

Implemented tests:
	--skip=item1,item2  :  Sets files to be skipped
"""
import sys
import frontmatter
# from helpers.utils import get_project_root

def get_frontmatter(filename, errCount):
	'''Extracts frontmatter from post for further processing.'''
	post_vars = dict()
	start_read = False
	errList = list()
	try:
		record = frontmatter.load(filename)
	except Exception as e:
		errCount += 1
		errList.append("ERROR: {}".format(e))

	return post_vars, errCount, errList

if __name__ == "__main__":
	filename = sys.argv[1]
	errCount = 0
	frontmatter, errCount, errList = get_frontmatter(filename, errCount)
	print(errList)
