from abaqusConstants import *
from .Load import Load
from ..Region.Region import Region


class PipePressure(Load):
    """The PipePressure object stores the data for a pressure applied to pipe or elbow
    elements.
    The PipePressure object is derived from the Load object.

    Attributes
    ----------
    name: str
        A String specifying the load repository key.
    distributionType: SymbolicConstant
        A SymbolicConstant specifying whether the load is uniform. Possible values are UNIFORM,
        HYDROSTATIC, USER_DEFINED, and FIELD. The default value is UNIFORM.
    side: SymbolicConstant
        A SymbolicConstant specifying whether the pressure is applied internally or externally.
        Possible values are INTERNAL and EXTERNAL. The default value is INTERNAL.
    diameter: float
        A Float specifying the effective inner or outer diameter.
    field: str
        A String specifying the name of the :py:class:`~abaqus.Field.AnalyticalField.AnalyticalField` object associated with this load.
        The **field** argument applies only when **distributionType=FIELD**. The default value is an
        empty string.
    region: Region
        A :py:class:`~abaqus.Region.Region.Region` object specifying the region to which the load is applied.

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import load
        mdb.models[name].loads[name]

    """

    # A String specifying the load repository key.
    name: str = ""

    # A SymbolicConstant specifying whether the load is uniform. Possible values are UNIFORM,
    # HYDROSTATIC, USER_DEFINED, and FIELD. The default value is UNIFORM.
    distributionType: SymbolicConstant = UNIFORM

    # A SymbolicConstant specifying whether the pressure is applied internally or externally.
    # Possible values are INTERNAL and EXTERNAL. The default value is INTERNAL.
    side: SymbolicConstant = INTERNAL

    # A Float specifying the effective inner or outer diameter.
    diameter: float = None

    # A String specifying the name of the AnalyticalField object associated with this load.
    # The **field** argument applies only when **distributionType**=FIELD. The default value is an
    # empty string.
    field: str = ""

    # A Region object specifying the region to which the load is applied.
    region: Region = Region()

    def __init__(
        self,
        name: str,
        createStepName: str,
        region: Region,
        magnitude: float,
        diameter: float,
        hZero: float,
        hReference: float,
        field: str = "",
        amplitude: str = UNSET,
        distributionType: SymbolicConstant = UNIFORM,
        side: SymbolicConstant = INTERNAL,
    ):
        """This method creates a Pressure object.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            mdb.models[name].PipePressure

        Parameters
        ----------
        name
            A String specifying the load repository key.
        createStepName
            A String specifying the name of the step in which the pressure is created.
        region
            A Region object specifying the region to which the load is applied.
        magnitude
            A Float specifying the pressure magnitude.Note:*magnitude* is optional if
            **distributionType**=USER_DEFINED.
        diameter
            A Float specifying the effective inner or outer diameter.
        hZero
            A Float specifying the height of the zero pressure level when
            **distributionType**=HYDROSTATIC.
        hReference
            A Float specifying the height of the reference pressure level when
            **distributionType**=HYDROSTATIC.
        field
            A String specifying the name of the AnalyticalField object associated with this load.
            The **field** argument applies only when **distributionType**=FIELD. The default value is an
            empty string.
        amplitude
            A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
            UNSET should be used if the load has no amplitude reference. The default value is UNSET.
            You should provide the **amplitude** argument only if it is valid for the specified step.
        distributionType
            A SymbolicConstant specifying whether the load is uniform. Possible values are UNIFORM,
            HYDROSTATIC, USER_DEFINED, and FIELD. The default value is UNIFORM.
        side
            A SymbolicConstant specifying whether the pressure is applied internally or externally.
            Possible values are INTERNAL and EXTERNAL. The default value is INTERNAL.

        Returns
        -------
            A PipePressure object.
        """
        super().__init__()
        pass

    def setValues(
        self,
        field: str = "",
        amplitude: str = UNSET,
        distributionType: SymbolicConstant = UNIFORM,
        side: SymbolicConstant = INTERNAL,
    ):
        """This method modifies the data for an existing PipePressure object in the step where it
        is created.

        Parameters
        ----------
        field
            A String specifying the name of the AnalyticalField object associated with this load.
            The **field** argument applies only when **distributionType**=FIELD. The default value is an
            empty string.
        amplitude
            A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
            UNSET should be used if the load has no amplitude reference. The default value is UNSET.
            You should provide the **amplitude** argument only if it is valid for the specified step.
        distributionType
            A SymbolicConstant specifying whether the load is uniform. Possible values are UNIFORM,
            HYDROSTATIC, USER_DEFINED, and FIELD. The default value is UNIFORM.
        side
            A SymbolicConstant specifying whether the pressure is applied internally or externally.
            Possible values are INTERNAL and EXTERNAL. The default value is INTERNAL.
        """
        pass

    def setValuesInStep(
        self,
        stepName: str,
        magnitude: float = None,
        hZero: float = None,
        hReference: float = None,
        amplitude: str = "",
    ):
        """This method modifies the propagating data for an existing PipePressure object in the
        specified step.

        Parameters
        ----------
        stepName
            A String specifying the name of the step in which the load is modified.
        magnitude
            A Float specifying the pressure magnitude.
        hZero
            A Float specifying the height of the zero pressure level when
            **distributionType**=HYDROSTATIC.
        hReference
            A Float specifying the height of the reference pressure level when
            **distributionType**=HYDROSTATIC.
        amplitude
            A String or a SymbolicConstant specifying the name of the amplitude reference. Possible
            values for the SymbolicConstant are UNCHANGED and FREED. UNCHANGED should be used if the
            amplitude is propagated from the previous static analysis step. FREED should be used if
            the load has no amplitude reference. You should provide the **amplitude** argument only if
            it is valid for the specified step.
        """
        pass
