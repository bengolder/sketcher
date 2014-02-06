class TextBlock(object):
    """ For drawing text
    """
    def __init__(self, string):
        self.contents = []
        self.contents.append(string)
        self.size = 14
        self._set_bbox()
        self.font = "sans-serif"

    def draw(self, ctx):
        pass

    def _set_bbox(self):
        """resets the bounding box based on string contents
        """
        pass



