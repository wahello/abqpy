from abaqusConstants import *
from .Interaction import Interaction
from ..Region.RegionArray import RegionArray


class PressurePenetration(Interaction):
    """The PressurePenetration object defines pressure penetration loading simulated with
    surface-to-surface contact.
    The PressurePenetration object is derived from the Interaction object.

    Attributes
    ----------
    name: str
        A String specifying the repository key.
    createStepName: str
        A String specifying the name of the step in which the :py:class:`~abaqus.Interaction.PressurePenetration.PressurePenetration` object is
        created.
    contactInteraction: str
        A String specifying the name of the Surface-to-surface contact (Standard) interaction.
    mainPoints: RegionArray
        A :py:class:`~abaqus.Region.RegionArray.RegionArray` object specifying the points on the main surface that are exposed to the
        fluid.
    secondaryPoints: RegionArray
        A :py:class:`~abaqus.Region.RegionArray.RegionArray` object specifying the points on the secondary surface that are exposed to
        the fluid.

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import interaction
        mdb.models[name].interactions[name]

    The corresponding analysis keywords are:

    - PRESSURE PENETRATION

    """

    # A String specifying the repository key.
    name: str = ""

    # A String specifying the name of the step in which the PressurePenetration object is
    # created.
    createStepName: str = ""

    # A String specifying the name of the Surface-to-surface contact (Standard) interaction.
    contactInteraction: str = ""

    # A RegionArray object specifying the points on the main surface that are exposed to the
    # fluid.
    mainPoints: RegionArray = RegionArray()

    # A RegionArray object specifying the points on the secondary surface that are exposed to
    # the fluid.
    secondaryPoints: RegionArray = RegionArray()

    def __init__(
        self,
        name: str,
        createStepName: str,
        contactInteraction: str,
        mainPoints: RegionArray,
        secondaryPoints: RegionArray,
        penetrationPressure: float,
        criticalPressure: float,
        amplitude: str = UNSET,
        penetrationTime: float = 0,
    ):
        """This method creates a PressurePenetration object.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            mdb.models[name].PressurePenetration

        Parameters
        ----------
        name
            A String specifying the repository key.
        createStepName
            A String specifying the name of the step in which the PressurePenetration object is
            created.
        contactInteraction
            A String specifying the name of the Surface-to-surface contact (Standard) interaction.
        mainPoints
            A RegionArray object specifying the points on the main surface that are exposed to the
            fluid.
        secondaryPoints
            A RegionArray object specifying the points on the secondary surface that are exposed to
            the fluid.
        penetrationPressure
            A tuple of Floats specifying the fluid pressure magnitude. For steady state dynamic
            analyses, a tuple of Complexes specifying the fluid pressure magnitude.
        criticalPressure
            A tuple of Floats specifying the critical contact pressure below which fluid penetration
            starts to occur.
        amplitude
            A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
            UNSET should be used if the load has no amplitude reference. The default value is UNSET.
            You should provide the **amplitude** argument only if it is valid for the specified step.
        penetrationTime
            A Float specifying the fraction of the current step time over which the fluid pressure
            on newly penetrated contact surface segments is ramped up to the current magnitude. The
            default value is 0.001.

        Returns
        -------
            A PressurePenetration object.
        """
        super().__init__()
        pass

    def setValues(self, amplitude: str = UNSET, penetrationTime: float = 0):
        """This method modifies the data for an existing PressurePenetration object in the step
        where it is created.

        Parameters
        ----------
        amplitude
            A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
            UNSET should be used if the load has no amplitude reference. The default value is UNSET.
            You should provide the **amplitude** argument only if it is valid for the specified step.
        penetrationTime
            A Float specifying the fraction of the current step time over which the fluid pressure
            on newly penetrated contact surface segments is ramped up to the current magnitude. The
            default value is 0.001.
        """
        pass

    def setValuesInStep(
        self,
        stepName: str,
        penetrationPressure: float = None,
        criticalPressure: float = None,
        amplitude: str = "",
        penetrationTime: float = 0,
    ):
        """This method modifies the propagating data for an existing PressurePenetration object in
        the specified step.

        Parameters
        ----------
        stepName
            A String specifying the name of the step in which the interaction is modified.
        penetrationPressure
            A tuple of Floats specifying the fluid pressure magnitude. For steady state dynamic
            analyses, a tuple of Complexes specifying the fluid pressure magnitude.
        criticalPressure
            A tuple of Floats specifying the critical contact pressure below which fluid penetration
            starts to occur.
        amplitude
            A String or a SymbolicConstant specifying the name of the amplitude reference. Possible
            values for the SymbolicConstant are UNCHANGED and FREED. UNCHANGED should be used if the
            amplitude is propagated from the previous analysis step. FREED should be used if the
            load is changed to have no amplitude reference. You should provide the **amplitude**
            argument only if it is valid for the specified step.
        penetrationTime
            A Float specifying the fraction of the current step time over which the fluid pressure
            on newly penetrated contact surface segments is ramped up to the current magnitude. The
            default value is 0.001.
        """
        pass
