# Python SuperCluster
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/python-supercluster)
![Test workflow status](https://github.com/Sangrene/python-supercluster/actions/workflows/tests.yaml/badge.svg)

## Usage
```python
index = SuperCluster().load(features)
clusters_at_zoom_2 = index.get_clusters([-180, -90, 180, 90], 2)
  ```
