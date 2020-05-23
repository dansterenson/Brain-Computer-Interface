import os
import sys
import pytest
import pathlib

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append('../')


_SAMPLE_PATH = pathlib.Path(__file__).absolute().parent / 'tests/data/test_file.mind.gz'
