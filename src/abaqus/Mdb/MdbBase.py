import typing

from ..Adaptivity.AdaptivityProcess import AdaptivityProcess
from ..Annotation.Annotation import Annotation
from ..CustomKernel.RepositorySupport import RepositorySupport
from ..EditMesh.MeshEditOptions import MeshEditOptions
from ..Job.Job import Job
from ..Job.OptimizationProcess import OptimizationProcess
from ..Model.Model import Model


class MdbBase:
    """The Mdb object is the high-level Abaqus model database. A model database stores models
    and analysis controls.

    .. note:: 
        This object can be accessed by:

        .. code-block:: python

            mdb
    """

    #: An Int specifying the release number of the Mdb object in memory.
    version: int = None

    #: A Float specifying the value of a counter associated with the Mdb object. The counter
    #: indicates when the Mdb object was last changed.
    lastChangedCount: float = None

    #: A repository of Job objects.
    jobs: typing.Dict[str, Job] = {}

    #: A repository of AdaptivityProcess objects.
    adaptivityProcesses: typing.Dict[str, AdaptivityProcess] = {}

<<<<<<< HEAD
=======
    #: A repository of Coexecution objects.
    coexecutions: typing.Dict[str, Coexecution] = {}

>>>>>>> 94bc5bb (Use typing annotations to support Python 3.8 and less)
    #: A repository of OptimizationProcess objects.
    optimizationProcesses: typing.Dict[str, OptimizationProcess] = typing.Dict[
        str, OptimizationProcess
    ]()

    #: A :py:class:`~abaqus.EditMesh.MeshEditOptions.MeshEditOptions` object specifying the undo/redo behavior when editing meshes on parts
    #: or part instances.
    meshEditOptions: MeshEditOptions = MeshEditOptions()

    #: A repository of Model objects.
    models: typing.Dict[str, Model] = {}

    #: A :py:class:`~abaqus.CustomKernel.RepositorySupport.RepositorySupport` object.
    customData: RepositorySupport = RepositorySupport()

    #: A repository of Annotation objects.
    annotations: typing.Dict[str, Annotation] = {}

    def __init__(self, pathName: str = ""):
        """This constructor creates an empty Mdb object.

        .. note:: 
            This function can be accessed by:

            .. code-block:: python

                Mdb

        Parameters
        ----------
        pathName: str
            A String specifying the path to be used when the model database is saved to a file. If
            you do not provide a file extension, .cae is appended automatically to the path. The
            default value is an empty string.

        Returns
        -------
        Mdb
            A :py:class:`~abaqus.Mdb.Mdb.Mdb` object
        """
        self.pathName = pathName
        self.models["Model-1"] = Model("Model-1")
        self.models["Model-1"].FieldOutputRequest("F-Output-1", "Initial")

    def importDxf(self, fileName: str):
        """This method creates a ConstrainedSketch object from a file containing dxf-format
        (AutoCAD) geometry. Only a limited number of entities are supported. This format should
        be used only if no other formats are available.

        .. note:: 
            This function can be accessed by:

            .. code-block:: python

                Mdb

        Parameters
        ----------
        fileName
            A String specifying the path to the dxf file to open.

        Returns
        -------
        Mdb
            A :py:class:`~abaqus.Mdb.Mdb.Mdb` object
        """
        ...

    def openMdb(self, pathName: str):
        """This method opens an existing model database file.

        .. note:: 
            This function can be accessed by:

            .. code-block:: python

                Mdb

        Parameters
        ----------
        pathName: str
            A String specifying the path to the model database file to open. If you do not provide a
            file extension, Abaqus/CAE attempts to open the file with .cae appended to the path.

        Returns
        -------
        Mdb
            A :py:class:`~abaqus.Mdb.Mdb.Mdb` object

        Raises
        ------
        MdbError
            invalid model database;
            If the file is an invalid model database
        MdbError
            incompatible release number, expected *<Abaqus release>*, got *<earlier or later Abaqus release>*;
            If the file contains a model database from an Abaqus release other than the Abaqus
            release you are currently running
        MdbError
            cannot open file; may be in use by another CAE session;
            If the model database file is already opened in write mode
        MdbError
            cannot open file;
            If the command fails to open the model database file for reasons not mentioned above
        """
        ...

    def close(self):
        """This method closes an open Mdb object but does not save the Mdb object to disk. After
        closing the Mdb object, this method creates a new unnamed empty Mdb object.
        """
        ...

    def save(self):
        """This method saves an Mdb object to disk at the location specified by **pathName**
        (*pathName* is a member of the Mdb object).

        Raises
        ------
        MdbError
            cannot save file: pathname member is empty;
            If **pathName** is empty
        MdbError
            “abaqus.cae” is an invalid CAE filename;
            If **pathName** is abaqus.cae

        Parameters
        ----------
        MdbError
            cannot save file;
            If the command fails to save the Mdb object to disk for reasons not mentioned above
        """
        ...

    def saveAs(self, pathName: str):
        """This method saves an Mdb object to disk at the specified location.

        Parameters
        ----------
        pathName: str
            A String specifying the path to be used when the model database is saved to a file. If
            you do not provide a file extension, .cae is appended automatically to the path.

        Raises
        ------
        MdbError
            “abaqus.cae” is an invalid CAE filename;
            If **pathName** is abaqus.cae
        MdbError
            cannot save file;
            If the command fails to save the Mdb object to disk for reasons not mentioned above
        """
        ...

    def openAuxMdb(self, pathName: str):
        """This method opens an auxiliary Mdb object on the disk at the specified location. This
        enables models from the auxiliary Mdb object to be copied into the current Mdb.

        Parameters
        ----------
        pathName: str
            A String specifying the path to the auxiliary Mdb which is to be opened. If you do not
            provide a file extension, .cae is appended automatically to the path.

        Raises
        ------
        MdbError
            invalid model database;
            If the file is an invalid model database
        MdbError
            incompatible release number;
            If the file contains a model database from an Abaqus release other than the Abaqus
            release you are currently running
        MdbError
            cannot open file;
            If the command fails to open the model database file for reasons not mentioned above
        """
        ...

    def closeAuxMdb(self):
        """This method closes the auxiliary Mdb which had been opened earlier using the openAuxMdb
        command.

        Raises
        ------

        Parameters
        ----------
        MdbError
            The auxiliary Mdb was not opened;
            If the auxiliary Mdb was not opened earlier
        """
        ...

    def getAuxMdbModelNames(self):
        """This method returns a list of model names present in the auxiliary Mdb which had been
        opened earlier using the openAuxMdb command.

        Returns
        -------
        typing.List[str]
            A list of model names present in the auxiliaryMdb

        Raises
        ------
        MdbError
            The auxiliary Mdb was not opened;
            If the auxiliary Mdb was not opened earlier
        """
        ...

    def copyAuxMdbModel(self, fromName: str, toName: str = ""):
        """This method copies a specified model from the auxiliary Mdb which had been opened
        earlier using the openAuxMdb command.

        Parameters
        ----------
        fromName
            A String specifying the model name in the auxiliary Mdb which is to be copied.
        toName
            A String specifying the name to be given to the model after it is copied into the Mdb.
            If this argument is not specified **toName** is assumed to be the same as **fromName**. If a
            model with name **toName** already exists in Mdb, it is overwritten.

        Raises
        ------
        MdbError
            The auxiliary Mdb was not opened;
            If the auxiliary Mdb was not opened earlier
        KeyError
            fromName does not exist;
            If the model fromName does not exist in the auxiliary Mdb
        """
        ...
