from ..UtilityAndView.abaqusConstants import *
from .PredefinedField import PredefinedField
from ..Assembly.PartInstanceArray import PartInstanceArray
from ..Region.Region import Region


class MaterialAssignment(PredefinedField):
    """The MaterialAssignment object stores the data for an initial material assignment
    predefined field, for use with an Eulerian analysis.
    The MaterialAssignment object is derived from the PredefinedField object.

    .. note:: 
        This object can be accessed by:

        .. code-block:: python

            import load
            mdb.models[name].predefinedFields[name]

        The corresponding analysis keywords are:

        - INITIAL CONDITIONS
    """

    #: A :py:class:`~abaqus.Region.Region.Region` object specifying the region to which the predefined field is applied.
    region: Region = Region()

    #: A String specifying the repository key.
    name: str

    #: A :py:class:`~abaqus.Assembly.PartInstanceArray.PartInstanceArray` object specifying the part instances to which the predefined field
    #: is applied. All instances must be assigned the same Eulerian section.
    instanceList: PartInstanceArray

    #: A Boolean specifying whether the volume fraction data will be uniform or defined by
    #: discrete fields. The default value is OFF.
    useFields: Boolean = OFF

    #: A sequence of tuples specifying the uniform volume fractions to be assigned. This
    #: argument is valid only when **useFields** = FALSE. Each tuple contains two entries:A Region
    #: object.A tuple of Floats specifying the uniform volume fraction values. The length of
    #: the tuple must match the number of material instance names specified in the Eulerain
    #: section assigned to part instances specified by **instanceList**.
    assignmentList: tuple = ()

    #: A sequence of tuples specifying the discrete volume fractions to be assigned. This
    #: argument is valid only when **useFields** = TRUE. Each tuple contains two entries:A Region
    #: object.A tuple of Strings specifying Discrete Field names. The length of the tuple must
    #: match the number of material instance names specified in the Eulerain section assigned
    #: to part instances specified by **instanceList**.
    fieldList: tuple = ()

    #: A sequence of three Ints specifying colors used to display the material instance
    #: assignments. This is a sequence of R,G,B colors, where the values are represented by
    #: integers between 0 and 255. The default value is an empty sequence.
    colorList: tuple = ()

    def __init__(
        self,
        name: str,
        instanceList: PartInstanceArray,
        useFields: Boolean = OFF,
        assignmentList: tuple = (),
        fieldList: tuple = (),
        colorList: tuple = (),
    ):
        """This method creates a MaterialAssignment predefined field object.

        .. note:: 
            This function can be accessed by:

            .. code-block:: python

                mdb.models[name].MaterialAssignment

        Parameters
        ----------
        name
            A String specifying the repository key.
        instanceList
            A :py:class:`~abaqus.Assembly.PartInstanceArray.PartInstanceArray` object specifying the part instances to which the predefined field
            is applied. All instances must be assigned the same Eulerian section.
        useFields
            A Boolean specifying whether the volume fraction data will be uniform or defined by
            discrete fields. The default value is OFF.
        assignmentList
            A sequence of tuples specifying the uniform volume fractions to be assigned. This
            argument is valid only when **useFields** = FALSE. Each tuple contains two entries:A Region
            object.A tuple of Floats specifying the uniform volume fraction values. The length of
            the tuple must match the number of material instance names specified in the Eulerain
            section assigned to part instances specified by **instanceList**.
        fieldList
            A sequence of tuples specifying the discrete volume fractions to be assigned. This
            argument is valid only when **useFields** = TRUE. Each tuple contains two entries:A Region
            object.A tuple of Strings specifying Discrete Field names. The length of the tuple must
            match the number of material instance names specified in the Eulerain section assigned
            to part instances specified by **instanceList**.
        colorList
            A sequence of three Ints specifying colors used to display the material instance
            assignments. This is a sequence of R,G,B colors, where the values are represented by
            integers between 0 and 255. The default value is an empty sequence.

        Returns
        -------
        MaterialAssignment
            A :py:class:`~abaqus.PredefinedField.MaterialAssignment.MaterialAssignment` object.
        """
        super().__init__()

    def setValues(
        self,
        useFields: Boolean = OFF,
        assignmentList: tuple = (),
        fieldList: tuple = (),
        colorList: tuple = (),
    ):
        """This method modifies the MaterialAssignment object.

        Parameters
        ----------
        useFields
            A Boolean specifying whether the volume fraction data will be uniform or defined by
            discrete fields. The default value is OFF.
        assignmentList
            A sequence of tuples specifying the uniform volume fractions to be assigned. This
            argument is valid only when **useFields** = FALSE. Each tuple contains two entries:A Region
            object.A tuple of Floats specifying the uniform volume fraction values. The length of
            the tuple must match the number of material instance names specified in the Eulerain
            section assigned to part instances specified by **instanceList**.
        fieldList
            A sequence of tuples specifying the discrete volume fractions to be assigned. This
            argument is valid only when **useFields** = TRUE. Each tuple contains two entries:A Region
            object.A tuple of Strings specifying Discrete Field names. The length of the tuple must
            match the number of material instance names specified in the Eulerain section assigned
            to part instances specified by **instanceList**.
        colorList
            A sequence of three Ints specifying colors used to display the material instance
            assignments. This is a sequence of R,G,B colors, where the values are represented by
            integers between 0 and 255. The default value is an empty sequence.
        """
        ...
