"""Find in list using a general predicate. Seems to be missing in Python"""
def find(p, xs):
    it = iter(xs)
    for v in it:
        if(p(v)): return (v, it)
    return (None, it)

"""Drop all None values in a dict."""
def drop_nulls(d):
    return {k:v for k,v in d.items() if v is not None}

from .Repository import Repository

def repository(name, **kwargs):
    return Repository(name, **kwargs)

    

        
