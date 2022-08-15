from ..UtilityAndView.abaqusConstants import *
from .InteractionState import InteractionState


class FluidInflatorState(InteractionState):
    """The FluidInflatorState object stores the propagating data for a FluidInflator object.
    One instance of this object is created internally by the FluidInflator object for each
    step. The instance is also deleted internally by the FluidInflator object.
    The FluidInflatorState object has no constructor or methods.
    The FluidInflatorState object is derived from the InteractionState object.

    .. note::
        This object can be accessed by:

        .. code-block:: python

            import interaction
            mdb.models[name].steps[name].interactionStates[name]

    """

    #: A *SymbolicConstant* specifying the propagation state of the InteractionState object.
    #: Possible values are:
    #:
    #: - NOT_YET_ACTIVE
    #: - CREATED
    #: - PROPAGATED
    #: - MODIFIED
    #: - DEACTIVATED
    #: - NO_LONGER_ACTIVE
    #: - TYPE_NOT_APPLICABLE
    #: - INSTANCE_NOT_APPLICABLE
    #: - BUILT_INTO_BASE_STATE
    status: SymbolicConstant = None
