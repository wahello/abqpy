class Color:
    """The Color object contains the RGB definition of a system color.

    .. note:: 
        This object can be accessed by:

        .. code-block:: python

            session.colors[name]
    """

    #: A String specifying the name of the color.
    name: str = ""

    #: A tuple of three Floats specifying the RGB value of the color. The Float values must be
    #: between 0.0 and 1.0.
    rgb: float = None

    def setByRGB(self, rgb: tuple):
        """This method changes the RGB value of a user-defined color. However, users cannot define
        colors, and this method does not modify system-defined colors.

        Parameters
        ----------
        rgb
            A sequence of three Floats specifying the RGB value of the color. The Float values must
            be between 0.0 and 1.0.
        """
        ...
