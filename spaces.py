import cairocffi as cairo
from geometry import Box2D

class Surface(object):
    """
    A thing that can be saved as an image
    """
    def __init__(self, width, height):
        self.box = Box2D( width, height )
        self.surface = cairo.ImageSurface(
                "FORMAT_ARGB32",
                int(width),
                int(height),
                )
        self.ctx = cairo.Context( self.surface )
        self.drawing_stack = []

    def add(self, other, position="center"):
        """adds some element to the Surface"""
        self.justify_object( other, position )
        self.drawing_stack.append( other )

    def justify_object(self, thing, position="center"):
        """places an object in relation to the drawing surface, using that
        object's bounding box."""
        if position == "center":
            vector = self.box.center() - thing.bbox.center()
        else:
            vector = None
        if vector:
            thing.move( vector )

    def render(self):
        """This calls on the cairocffi api to draw
        all of the objects in the drawing_stack"""
        for item in self.drawing_stack:
            # objects in the drawing stack are responsible for drawing
            # themselves
            item.draw( self.ctx )

    def save(self, filepath="sketchImage.png"):
        self.surface.write_to_png( filepath )

