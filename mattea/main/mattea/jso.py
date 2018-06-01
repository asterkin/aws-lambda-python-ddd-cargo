"""Lazy conversion of dict into Python object"""

def jso(v):
    class Struct:
        def __init__(self, d):
            self.__d__ = d

        def __getattr__(self, a):
            return jso(self.__d__[a]) if a in self.__d__ else None
        
        def __getitem__(self, a):
            return self.__getattr__(a)

        def __repr__(self):
            return self.__d__.__repr__()
    class List:
        def __init__(self, l):
            self.__l__ = l

        def __getitem__(self, i):
            if( i < len(self.__l__)): return jso(self.__l__[i])
            else: raise StopIteration
            
        class Iterator:
            def __init__(self, l):
                self.__i__ = -1
                self.__l__ = l
                
            def __iter__(self):
                return self
                
            def __next__(self):
                self.__i__ += 1
                return List.__getitem__(self.__l__, self.__i__)
            
        def __iter__(self):
            return List.Iterator(self)

        def __repr__(self):
            return self.__l__.__repr__()

        def __len__(self):
            return self.__l__.__len__()

    if isinstance(v, dict): return Struct(v)
    elif isinstance(v, list): return List(v)
    else: return v

