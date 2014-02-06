from cairocffi import RecordingSurface, Context
from env import _SURFACE_CACHE, _CONTEXT_CACHE


class ContextDependent(object):
    def __init__(self):
        # initialize context cache if it doesn't exist
        if not _CONTEXT_CACHE:
            _SURFACE_CACHE = RecordingSurface()
            _CONTEXT_CACHE = Context( _SURFACE_CACHE )

class Drawable(object):
    """A base class for making things that can be drawn
    all drawable items must implement a draw function that receives a cairocffi
    Context object.
    """
    def __init__(self):
        pass

    def origin(self):
        pass

    def bbox(self):
        pass

    def draw(self, ctx):
        pass

    def move(self, vector):
        pass

    def rotate(self, angle, center=None):
        pass

    def scale(self, amount):
        pass

