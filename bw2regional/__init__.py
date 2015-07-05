# -*- coding: utf-8 -*
__version__ = (0, 3)

from .graphics import RegionalizedGrapher
from .intersection import Intersection
from .lca import (
    ExtensionTablesLCA,
    OneSpatialScaleLCA,
    TopologicalExtensionTablesLCA,
    TwoSpatialScalesLCA,
    TwoSpatialScalesWithGenericLoadingLCA,
)
from .loading import Loading
from .meta import (
    extension_tables,
    faces,
    geocollections,
    intersections,
    loadings,
)
from .utils import import_regionalized_cfs, create_empty_intersection, reset_geo_meta
from .xtables import ExtensionTable
from .base_data import (
    import_base_reg_data,
    import_lc_impact_lcia_method,
)
from .ecoinvent import prepare_ecoinvent_database

from bw2data import config
config.metadata.extend([
    extension_tables,
    faces,
    geocollections,
    intersections,
    loadings,
])
