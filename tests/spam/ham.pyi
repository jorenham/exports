from .external import external, external as external_alt

__all__ = ('public_all', 'public_export', 'external', 'external_alt')

def public_all() -> bool: ...
def public_export() -> bool: ...
def private() -> bool: ...  # undocumented
