import pytest
from mlproject.tools import haversine

def test():
    assert haversine(48.865070, 2.380009, 43.535065, 3.427292) == 603.2466449981002
