
"""
    A basic object that provides a skeleton backing of custom objects
    The skeleton includes:
        window the object is contained in
        position in 2d space
        an overridable start, update, and destroy functions
"""
class BasicObject(object):
    def __init__(self):
        pass;
    
    def create(self):
        pass;

    def update(self):
        pass;

    def destroy(self):
        pass;
