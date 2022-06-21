from .Section import Section


class AcousticInfiniteSection(Section):
    """The AcousticInfiniteSection object defines the properties of an acoustic section.
    The AcousticInfiniteSection object is derived from the Section object.

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import section
        mdb.models[name].sections[name]
        import odbSection
        session.odbs[name].sections[name]

    The corresponding analysis keywords are:

    - SOLID SECTION
    """

    def __init__(self, name: str, material: str, thickness: float = 1, order: int = 10):
        """This method creates an AcousticInfiniteSection object.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            mdb.models[name].AcousticInfiniteSection
            session.odbs[name].AcousticInfiniteSection

        Parameters
        ----------
        name
            A String specifying the repository key.
        material
            A String specifying the name of the material.
        thickness
            A Float specifying the thickness of the section. Possible values are **thickness** >> 0.0.
            The default value is 1.0.
        order
            An Int specifying the number of ninth-order polynomials that will be used to resolve the
            variation of the acoustic field in the infinite direction. Possible values are 0 <<
            **order** ≤≤ 10. The default value is 10.

        Returns
        -------
        AcousticInfiniteSection
            An :py:class:`~abaqus.Section.AcousticInfiniteSection.AcousticInfiniteSection` object.

        Raises
        ------
        InvalidNameError
        RangeError
        """
        super().__init__()
        pass

    def setValues(self, thickness: float = 1, order: int = 10):
        """This method modifies the AcousticInfiniteSection object.

        Parameters
        ----------
        thickness
            A Float specifying the thickness of the section. Possible values are **thickness** >> 0.0.
            The default value is 1.0.
        order
            An Int specifying the number of ninth-order polynomials that will be used to resolve the
            variation of the acoustic field in the infinite direction. Possible values are 0 <<
            **order** ≤≤ 10. The default value is 10.

        Raises
        ------
        RangeError
        """
        pass
