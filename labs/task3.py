import sys
import gc
import weakref

a = []
b = a
print("Ссылки:", sys.getrefcount(a))
del b
print("После del:", sys.getrefcount(a))

class A:
    pass

obj = A()
ref = weakref.ref(obj)
print("До удаления:", ref())
del obj
gc.collect()
print("После удаления:", ref())

d = weakref.WeakValueDictionary()
obj = A()
d["obj"] = obj
print("Словарь:", list(d.keys()))
del obj
gc.collect()
print("После del:", list(d.keys()))
