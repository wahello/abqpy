import typing

from abaqusConstants import *
from .DesignResponse import DesignResponse
from .GeometricRestriction import GeometricRestriction
from .ObjectiveFunction import ObjectiveFunction
from .OptimizationConstraint import OptimizationConstraint
from .StopCondition import StopCondition


class OptimizationTaskBase:
    """The OptimizationTask object is the abstract base type for other OptimizationTask
    objects. The OptimizationTask object has no explicit constructor. The methods and
    members of the OptimizationTask object are common to all objects derived from
    OptimizationTask.

    .. note:: 
        This object can be accessed by:

        .. code-block:: python

            import optimization
            mdb.models[name].optimizationTasks[name]
    """

    #: A String specifying the optimization task repository key.
    name: str = ""

    #: The SymbolicConstant MODEL or a Region object specifying the region to which the
    #: optimization task is applied. The default value is MODEL.
    region: SymbolicConstant = MODEL

    #: A repository of DesignResponse objects.
    designResponses: typing.Dict[str, DesignResponse] = {}

    #: A repository of ObjectiveFunction objects.
    objectiveFunctions: typing.Dict[str, ObjectiveFunction] = {}

    #: A repository of OptimizationConstraint objects.
    optimizationConstraints: typing.Dict[str, OptimizationConstraint] = {}

    #: A repository of GeometricRestriction objects.
    geometricRestrictions: typing.Dict[str, GeometricRestriction] = {}

    #: A repository of StopCondition objects.
    stopConditions: typing.Dict[str, StopCondition] = {}
