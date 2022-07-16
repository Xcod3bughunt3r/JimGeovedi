# -*- coding: utf-8 -*-

import codecs
from collections import defaultdict, Counter

import logging
logging.basicConfig(format='%(asctime)s [%(process)d] [%(levelname)s] %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S', level=logging.INFO)
requests_logger = logging.getLogger('requests')
requests_logger.setLevel('WARNING')

try:
    import regex as re
except ImportError:
    logging.info('Regex module not found. Will use regular `re`.')
    import re


# http://www.mobify.com/blog/sqlalchemy-memory-magic/
from pympler import summary, muppy
import psutil

def get_virtual_memory_usage_kb():
    """
    The process's current virtual memory size in Kb, as a float.
    """
    return float(psutil.Process().memory_info_ex().vms) / 1024.0

def memory_usage(where=None):
    """
    Print out a basic summary of memory usage.
    """
    mem_summary = summary.summarize(muppy.get_objects())
    print "Memory summary:", where
    summary.print_(mem_summary, limit=2)
    print "VM: %.2fMb" % (get_virtual_memory_usage_kb() / 1024.0)


