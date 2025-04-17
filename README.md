# Python SuperCluster
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/python-supercluster)
![Test workflow status](https://github.com/Sangrene/python-supercluster/actions/workflows/tests.yaml/badge.svg)

This library aims to provide the geospatial clustering features of mapbox supercluster while using Python and optimised numpy under the hood for good performances.
## Usage
```python
features = [
    [-79.04411780507252, 43.08771393436908],
    [-62.06181800038502, 5.686896063275327],
    [-54.58299719960377, -25.568291925005923],
    [51.258313644180184, 11.822028799226407],
    [25.852793816021233, -17.928033135943423],
]
index = SuperCluster().load(features)
clusters_at_zoom_2 = index.get_clusters([-180, -90, 180, 90], 2)
  ```
