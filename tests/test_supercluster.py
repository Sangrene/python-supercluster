import pytest
from ..python_supercluster import Supercluster
from .fixtures import features

def test_supercluster():
  supercluster = Supercluster().load(features)
  assert("")