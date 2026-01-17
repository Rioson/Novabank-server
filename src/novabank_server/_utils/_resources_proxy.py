from __future__ import annotations

from typing import Any
from typing_extensions import override

from ._proxy import LazyProxy


class ResourcesProxy(LazyProxy[Any]):
    """A proxy for the `novabank_server.resources` module.

    This is used so that we can lazily import `novabank_server.resources` only when
    needed *and* so that users can just import `novabank_server` and reference `novabank_server.resources`
    """

    @override
    def __load__(self) -> Any:
        import importlib

        mod = importlib.import_module("novabank_server.resources")
        return mod


resources = ResourcesProxy().__as_proxied__()
