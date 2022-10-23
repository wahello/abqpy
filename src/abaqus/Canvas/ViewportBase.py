from typing import Optional, Tuple, Sequence, Dict, overload

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from typing_extensions import Literal

from .AttributeColorMap import AttributeColorMap
from .Displayable import Displayable
from .ImageOptions import ImageOptions
from .Layer import Layer
from .MovieOptions import MovieOptions
from ..Animation.AnimationController import AnimationController
from ..Annotation.AnnotationsToPlotArray import AnnotationsToPlotArray
from ..DisplayGroup.Leaf import Leaf
from ..DisplayOptions.AssemblyDisplayOptions import AssemblyDisplayOptions
from ..DisplayOptions.LightOptions import LightOptions
from ..DisplayOptions.PartDisplayOptions import PartDisplayOptions
from ..DisplayOptions.ViewportAnnotationOptions import ViewportAnnotationOptions
from ..OdbDisplay.OdbDisplay import OdbDisplay
from ..PlotOptions.DetailPlotOptions import DetailPlotOptions
from ..UtilityAndView.SymbolicConstant import abaqusConstants as C
from ..UtilityAndView.View import View
from ..UtilityAndView.abaqusConstants import (
    Boolean,
    DEFAULT_COLORS,
    HOLLOW_CIRCLE,
    OFF,
    ON,
    SMALL,
    SYSTEM,
    SymbolicConstant,
)
from .._OptionsBase import _OptionsBase


@abaqus_class_doc
class ViewportBase(_OptionsBase):
    """A viewport is the container for the graphics generated by the application. TheViewport
    object stores the various settings that determine how objects are displayed within that
    viewport.

    .. note::
        This object can be accessed by::

            session.viewports[name]
    """

    #: A String specifying the repository key.
    name: str

    #: A pair of Floats specifying the **X**- and **Y**-coordinates in millimeters in the canvas
    #: coordinate system of the lower left corner of the viewport. The default origin is (0, 0).
    origin: Sequence[float] = (0.0, 0.0)

    #: A Float specifying the width in millimeters of the viewport. Possible values are 30 ≤
    #: **width** ≤ (*maxWidth*). The default value is 120. Note: The maximum value of width
    #: (*maxWidth*) is the width of the screen in millimeters.
    width: float = 120.0

    #: A Float specifying the height in millimeters of the viewport. This height includes the
    #: title bar. Possible values are 30 ≤ **height** ≤ (*maxHeight*). The default value is 80.0.
    #: Note: The maximum value of height (*maxHeight*) is the height of the screen in millimeters.
    height: float = 80.0

    #: A Boolean specifying whether the viewport border is visible in a printed image. The
    #: default value is ON.
    border: Boolean = ON

    #: A Boolean specifying whether the viewport title should be displayed in a printed image.
    #: The default value is ON.If **border** = OFF, the title will not be visible, even if
    #: **titleBar** =ON.
    titleBar: Boolean = ON

    #: A SymbolicConstant specifying which title to use for the viewport title. Possible values
    #: are CUSTOM and SYSTEM. The default value is SYSTEM.If **titleStyle** = CUSTOM,
    #: **customTitleString** will be used. If **titleStyle** =  SYSTEM, a system-generated string
    #: will be used.
    titleStyle: Literal[C.CUSTOM, C.SYSTEM] = SYSTEM

    #: A String specifying the viewport title when **titleStyle** =CUSTOM. The default value is
    #: an empty string.
    customTitleString: str = ""

    #: A SymbolicConstant specifying the display mode of the viewport. Possible values
    #: are:SINGLE, specifying a single **displayedObject**.OVERLAY, specifying one or more layers
    #: to be displayed simultaneously—each layer contains one **displayedObject**.
    displayMode: Optional[SymbolicConstant] = None

    #: A SymbolicConstant specifying which layer or layers will be controlled by the view
    #: manipulation tools when **displayMode** = OVERLAY. Possible values are ALL and CURRENT.
    viewManipLayers: Optional[SymbolicConstant] = None

    #: A Float specifying a factor to be used in offsetting layers in the screen Z direction.
    #: Possible values are -1 to 1. A negative value reverses the apparent order in which the
    #: layers are plotted.
    layerOffset: Optional[float] = None

    #: A SymbolicConstant specifying the current state of a viewport. Possible values are
    #: NORMAL, MAXIMIZED, and MINIMIZED.
    windowState: Optional[SymbolicConstant] = None

    #: A Float specifying the width in millimeters of the current viewport, regardless of the
    #: value of **windowState**.
    currentWidth: Optional[float] = None

    #: A Float specifying the height in millimeters of the current viewport, regardless of the
    #: value of **windowState**, and including the title bar.
    currentHeight: Optional[float] = None

    #: A Boolean specifying whether the viewport is linked for synchronization. The default
    #: value is ON.
    applyLinkedCommands: Boolean = ON

    #: A SymbolicConstant specifying the currently active color mappings. Possible values
    #: are:
    #: DEFAULT_COLORS
    #: PART_GEOM_MAP_COLORS
    #: ASSEMBLY_MAP_COLORS
    #: PART_MAP_COLORS
    #: INSTANCE_MAP_COLORS
    #: INSTANCE_TYPE_MAP_COLORS
    #: SECTION_MAP_COLORS
    #: MATERIAL_MAP_COLORS
    #: LOAD_MAP_COLORS
    #: BC_MAP_COLORS
    #: INTERACTION_MAP_COLORS
    #: CONSTRAINT_MAP_COLORS
    #: SET_MAP_COLORS
    #: SURFACE_MAP_COLORS
    #: INTERNAL_SET_MAP_COLORS
    #: INTERNAL_SURFACE_MAP_COLORS
    #: DISPLAY_GRP_MAP_COLORS
    #: SELECTION_GRP_MAP_COLORS
    #: ELTYPE_MAP_COLORS
    #: PLOT_MAP_COLORS
    #: MESH_MAP_COLORS
    #: The default value is DEFAULT_COLORS.
    activeColorModes: Literal[
        C.DEFAULT_COLORS,
        C.PART_GEOM_MAP_COLORS,
        C.ASSEMBLY_MAP_COLORS,
        C.PART_MAP_COLORS,
        C.INSTANCE_MAP_COLORS,
        C.INSTANCE_TYPE_MAP_COLORS,
        C.SECTION_MAP_COLORS,
        C.MATERIAL_MAP_COLORS,
        C.LOAD_MAP_COLORS,
        C.BC_MAP_COLORS,
        C.INTERACTION_MAP_COLORS,
        C.CONSTRAINT_MAP_COLORS,
        C.SET_MAP_COLORS,
        C.SURFACE_MAP_COLORS,
        C.INTERNAL_SET_MAP_COLORS,
        C.INTERNAL_SURFACE_MAP_COLORS,
        C.DISPLAY_GRP_MAP_COLORS,
        C.SELECTION_GRP_MAP_COLORS,
        C.ELTYPE_MAP_COLORS,
        C.PLOT_MAP_COLORS,
        C.MESH_MAP_COLORS,
    ] = DEFAULT_COLORS

    #: A SymbolicConstant specifying the last applied color mapping. Possible values
    #: are:
    #: DEFAULT_COLORS
    #: PART_GEOM_MAP_COLORS
    #: ASSEMBLY_MAP_COLORS
    #: PART_MAP_COLORS
    #: INSTANCE_MAP_COLORS
    #: INSTANCE_TYPE_MAP_COLORS
    #: SECTION_MAP_COLORS
    #: MATERIAL_MAP_COLORS
    #: LOAD_MAP_COLORS
    #: BC_MAP_COLORS
    #: INTERACTION_MAP_COLORS
    #: CONSTRAINT_MAP_COLORS
    #: SET_MAP_COLORS
    #: SURFACE_MAP_COLORS
    #: INTERNAL_SET_MAP_COLORS
    #: INTERNAL_SURFACE_MAP_COLORS
    #: DISPLAY_GRP_MAP_COLORS
    #: SELECTION_GRP_MAP_COLORS
    #: ELTYPE_MAP_COLORS
    #: PLOT_MAP_COLORS
    #: MESH_MAP_COLORS
    #: The default value is DEFAULT_COLORS.
    colorMode: Literal[
        C.DEFAULT_COLORS,
        C.PART_GEOM_MAP_COLORS,
        C.ASSEMBLY_MAP_COLORS,
        C.PART_MAP_COLORS,
        C.INSTANCE_MAP_COLORS,
        C.INSTANCE_TYPE_MAP_COLORS,
        C.SECTION_MAP_COLORS,
        C.MATERIAL_MAP_COLORS,
        C.LOAD_MAP_COLORS,
        C.BC_MAP_COLORS,
        C.INTERACTION_MAP_COLORS,
        C.CONSTRAINT_MAP_COLORS,
        C.SET_MAP_COLORS,
        C.SURFACE_MAP_COLORS,
        C.INTERNAL_SET_MAP_COLORS,
        C.INTERNAL_SURFACE_MAP_COLORS,
        C.DISPLAY_GRP_MAP_COLORS,
        C.SELECTION_GRP_MAP_COLORS,
        C.ELTYPE_MAP_COLORS,
        C.PLOT_MAP_COLORS,
        C.MESH_MAP_COLORS,
    ] = DEFAULT_COLORS

    #: A Float specifying the translucency that will be applied to objects colored using
    #: **initialColor** and it needs to be set along with **initialColor**. If **initialColor** is
    #: set to 'As is' then translucency will have no effect.
    translucency: Optional[float] = None

    #: A Boolean specifying whether an animation is connected to the viewport.
    animationConnect: Boolean = OFF

    #: A repository of AttributeColorMap objects specifying the objects cannot be constructed
    #: but the following attribute maps are supported:
    #:
    #: - "type"
    #: - "Element set"
    #: - "Material"
    #: - "Section"
    #: - "Default"
    #: - "Part"
    #: - "Part instance"
    #: - "Element type"
    #: - "Averaging region"
    #: - "Assembly"
    #: - "Property"
    #: - "Set"
    #: - "Surface"
    #: - "Skin"
    #: - "Profile"
    #: - "Part shape"
    #: - "Part status"
    #: - "Part geometry"
    #: - "Meshability"
    #: - "Instance type"
    #: - "Load"
    #: - "Boundary condition"
    #: - "Interaction"
    #: - "Constraint"
    #: - "Interaction type"
    #: - "Constraint type"
    #: - "Display group"
    #: - "Selection group"
    #: - "Interaction property"
    #: - "Connector"
    #: - "Connector type"
    #: - "Connector property"
    #: - "Internal set"
    #: - "Internal surface"
    #: - "mapColors"
    #: - "autoColors"
    #: - "overrides"
    #: - "defaultAutoColors"
    #: - "defaultOverrides"
    #: - "objectToCopy"
    #: - "colorMapping"
    #: - "colorMappings"
    #: - "colorMode"
    #: - "attributeColors"
    #: - "updateOverrides"
    #: - "colorCodeOverride"
    #: - "initialColor"
    #: - "Layup"
    #: - "Ply"
    colorMappings: Dict[str, AttributeColorMap] = {}

    #: A String specifying the color that will be applied to all objects in the viewport at the
    #: start of color coding. The possible values are 'As is', 'Default' or a string with a
    #: hexadecimal representation of a color.
    initialColor: str = ""

    #: A String specifying which layer is affected by options settings when **displayMode**
    #: =OVERLAY. The current layer is also the only layer affected by view manipulations
    #: when*viewManipLayers* =CURRENT.
    currentLayer: str = ""

    #: A :py:class:`~abaqus.Canvas.Displayable.Displayable` object specifying the object to be displayed. The
    #: Displayable type is an abstract generalization. The concrete possible types are Part, Assembly,
    #: ConstrainedSketch, Odb, PlyStackPlot, or XYPlot. If **displayedObject** = None, Abaqus
    #: displays an empty viewport.
    displayedObject: Displayable = Displayable()

    #: A repository of Layer objects specifying the key to the repository is a String with the
    #: name of the layer.
    layers: Dict[str, Layer] = {}

    #: A :py:class:`~abaqus.UtilityAndView.View.View` object specifying the object that controls viewing of the
    #: viewport content.
    view: View

    #: An :py:class:`~abaqus.OdbDisplay.OdbDisplay.OdbDisplay` object specifying the display options for the Odb object.
    odbDisplay: OdbDisplay = OdbDisplay()

    #: A :py:class:`~abaqus.DisplayOptions.PartDisplayOptions.PartDisplayOptions` object specifying the display options
    #: for the Part object.
    partDisplay: PartDisplayOptions = PartDisplayOptions()

    #: An :py:class:`~abaqus.DisplayOptions.AssemblyDisplayOptions.AssemblyDisplayOptions` object specifying the
    #: display options for the Assembly object.
    assemblyDisplay: AssemblyDisplayOptions = AssemblyDisplayOptions()

    #: A :py:class:`~abaqus.DisplayOptions.ViewportAnnotationOptions.ViewportAnnotationOptions` object.
    viewportAnnotationOptions: ViewportAnnotationOptions = ViewportAnnotationOptions()

    #: A :py:class:`~abaqus.PlotOptions.DetailPlotOptions.DetailPlotOptions` object.
    detailPlotOptions: DetailPlotOptions = DetailPlotOptions()

    #: An :py:class:`~abaqus.Annotation.AnnotationsToPlotArray.AnnotationsToPlotArray` object.
    annotationsToPlot: AnnotationsToPlotArray = AnnotationsToPlotArray()

    #: A tuple of Strings specifying the names of layers that will be displayed in the viewport
    #: when **displayMode** = OVERLAY.
    visibleLayers: tuple = ()

    #: A pair of Floats specifying the **X**- and **Y**-coordinates in millimeters in the canvas
    #: coordinate system of the lower left corner of the current viewport, regardless of the
    #: value of **windowState**.
    currentOrigin: Sequence[float] = ()

    #: A pair of Floats specifying the **X**- and **Y**-coordinates in millimeters of the lower
    #: left corner of the current viewport from a coordinate system having its origin in the
    #: lower left corner of the drawing area. This origin refers to the viewport location when
    #: **windowState** =MINIMIZED.
    iconOrigin: Sequence[float] = ()

    #: A :py:class:`~abaqus.DisplayOptions.LightOptions.LightOptions` object.
    lightOptions: LightOptions = LightOptions()

    #: An :py:class:`~abaqus.Canvas.ImageOptions.ImageOptions` object.
    imageOptions: ImageOptions = ImageOptions()

    #: A :py:class:`~abaqus.Canvas.MovieOptions.MovieOptions` object.
    movieOptions: MovieOptions = MovieOptions()

    #: An AnimationController object.
    #:
    #: .. versionadded:: 2020
    #:     The `animationController` attribute was added.
    animationController: AnimationController = AnimationController()

    #: A tuple of Strings specifying keys to the session.drawings repository. The default value
    #: is an empty sequence.
    drawings: tuple = ()

    @abaqus_method_doc
    def __init__(
        self,
        name: str,
        origin: Tuple[float, float] = (0.0, 0.0),
        width: float = 120.0,
        height: float = 80.0,
        border: Boolean = ON,
        titleBar: Boolean = ON,
        titleStyle: Literal[C.CUSTOM, C.SYSTEM] = SYSTEM,
        customTitleString: str = "",
    ):
        """This method creates a Viewport object with the specified origin and dimensions.

        .. note::
            This function can be accessed by::

                session.Viewport

        Parameters
        ----------
        name
            A String specifying the repository key.
        origin
            A pair of Floats specifying the **X**- and **Y**-coordinates in millimeters in the canvas
            coordinate system of the lower left corner of the viewport. The default origin is (0,
            0).
        width
            A Float specifying the width in millimeters of the viewport. Possible values are 30 ≤
            **width** ≤ (*maxWidth*). The default value is 120.0. Note: The maximum value of width
            (*maxWidth*) is the width of the screen in millimeters.
        height
            A Float specifying the height in millimeters of the viewport. This height includes the
            title bar. Possible values are 30 ≤ **height** ≤ (*maxHeight*). The default value is
            80.0. Note: The maximum value of height (*maxHeight*) is the height of the screen in
            millimeters.
        border
            A Boolean specifying whether the viewport border is visible in a printed image. The
            default value is ON.
        titleBar
            A Boolean specifying whether the viewport title should be displayed in a printed image.
            The default value is ON.If **border** = OFF, the title will not be visible, even if
            **titleBar** =ON.
        titleStyle
            A SymbolicConstant specifying which title to use for the viewport title. Possible values
            are CUSTOM and SYSTEM. The default value is SYSTEM.If **titleStyle** = CUSTOM,
            **customTitleString** will be used. If **titleStyle** =  SYSTEM, a system-generated string
            will be used.
        customTitleString
            A String specifying the viewport title when **titleStyle** =CUSTOM. The default value is
            an empty string.

        Returns
        -------
        Viewport
            A :py:class:`~abaqus.Canvas.Viewport.Viewport` object.

        Raises
        ------
        SystemError: the current viewport may not be deleted
            If the user attempts to delete the only viewport.
        RangeError: width must be a Float in the range: 30 <= width <= **maxWidth**
            If **width** is out of range.
        RangeError: height must be a Float in the range: 30 <= width <= **maxHeight**
            If **height** is out of range.
        """
        self.name = name
        self.origin = origin
        self.width = width
        self.height = height
        self.border = border
        self.titleBar = titleBar
        self.titleStyle = titleStyle
        self.customTitleString = customTitleString

    @abaqus_method_doc
    def bringToFront(self):
        """This method moves the Viewport object to the front."""
        # TODO: implement this method
        ...

    @abaqus_method_doc
    def disableMultipleColors(self):
        """This method disables applying multiple color mappings that was enabled using
        enableMultipleColors
        """
        # TODO: implement this method
        ...

    @abaqus_method_doc
    def disableRefresh(self):
        """This method disables Viewport refresh. Some methods that require the Viewport to be
        up-to-date will override this setting. It is advisable to use this method sparingly.
        """
        # TODO: implement this method
        ...

    @abaqus_method_doc
    def disableColorCodeUpdates(self):
        """This method disables Viewport updates and internal computations triggered because of
        color coding. Performance improvement will be significant when color coding is ON and
        repeating operations are performed using a script each of which requires color code
        updates. No benefit will be had when color coding is OFF.
        """
        # TODO: implement this method
        ...

    @abaqus_method_doc
    def enableMultipleColors(self):
        """This method enables multiple color mappings to be applied at the same time. It also
        ensures that the Viewport is updated correctly when **initialColor** is set.
        """
        # TODO: implement this method
        ...

    @abaqus_method_doc
    def enableRefresh(self):
        """This method enables Viewport refresh disabled using disableRefresh."""
        # TODO: implement this method
        ...

    @abaqus_method_doc
    def enableColorCodeUpdates(self):
        """This method enables Viewport color code updates disabled using disableColorCodeUpdates."""
        # TODO: implement this method
        ...

    @abaqus_method_doc
    def getActiveElementLabels(self, useCut: Boolean = OFF, printResults: Boolean = OFF):
        """This method returns the element labels currently active in the viewport based on the
        current display group. The element labels are printed only when the **displayedObject**
        member in the Viewport object is set to an Odb. The getActiveElementLabels method has
        the following arguments:

        Parameters
        ----------
        useCut
            A Boolean flag to specify if any active cutting plane is to be considered in determining
            active elements.
        printResults
            A Boolean flag to specify if the active element labels are to be printed to the replay
            file.

        Returns
        -------
        dict
            A Dictionary object of element labels, keyed by OdbInstance name. Returns None if the
            **displayedObject** member is not an Odb object.
        """
        # TODO: implement this method
        ...

    @abaqus_method_doc
    def getActiveNodeLabels(self, useCut: Boolean = OFF, printResults: Boolean = OFF):
        """This method returns the node labels currently active in the viewport based on the
        current display group. The node labels are printed only when the **displayedObject**
        member in the Viewport object is set to an Odb. The getActiveNodeLabels method has the
        following arguments:

        Parameters
        ----------
        useCut
            A Boolean flag to specify if any active cutting plane is to be considered in determining
            active nodes.
        printResults
            A Boolean flag to specify if the active node labels are to be printed to the replay
            file.

        Returns
        -------
        dict
            A Dictionary object of node labels, keyed by OdbInstance name. Returns None if the
            **displayedObject** member is not an Odb object.
        """
        # TODO: implement this method
        ...

    @abaqus_method_doc
    def getPrimVarMinMaxLoc(self):
        """This method returns a dictionary containing the minimum, maximum and their location for
        the current primary variable. A contour plot should be displayed in the current viewport
        or else the method will return **None**.

        Returns
        -------
        dict
            A dictionary with keys 'minPartInstanceName', 'minElementLabel', 'minNodeLabel',
            'minPosition', 'maxPartInstanceName', 'maxElementLabel', 'maxNodeLabel', 'maxPosition' .
        """
        # TODO: implement this method
        ...

    @abaqus_method_doc
    def makeCurrent(self):
        """This method makes theViewport object the current viewport."""
        # TODO: implement this method
        ...

    @abaqus_method_doc
    def maximize(self):
        """This method maximizes the Viewport object to fill the drawing area."""
        # TODO: implement this method
        ...

    @abaqus_method_doc
    def minimize(self):
        """This method minimizes the Viewport object to appear as an abbreviated title bar."""
        # TODO: implement this method
        ...

    @abaqus_method_doc
    def offset(self, deltaX: float = 0, deltaY: float = 0):
        """This method modifies the current **X**-*Y* location of the viewport by the specified
        distance.

        Parameters
        ----------
        deltaX
            A Float specifying the offset in millimeters of the **X**-component of the viewport
            origin. The default value is 0.
        deltaY
            A Float specifying the offset in millimeters of the **Y**-component of the viewport
            origin. The default value is 0.
        """
        # TODO: implement this method
        ...

    @abaqus_method_doc
    def restore(self):
        """This method restores a maximized or minimized Viewport object to its previous size and
        location.
        """
        # TODO: implement this method
        ...

    @abaqus_method_doc
    def sendToBack(self):
        """This method moves the Viewport object to the back."""
        # TODO: implement this method
        ...

    @overload
    @abaqus_method_doc
    def setColor(self, initialColor: str, translucency: str = ""):
        """This method specifies the color assignment using **initialColor** and **translucency**. If
        **initialColor** has a value of 'As is', **translucency** has no effect. The setColor method
        has the following arguments:

        Parameters
        ----------
        initialColor
            A string specifying the initial color applied to the objects.
        translucency
            A float in the range of 0.0 to 1.0 specifying how translucent the objects drawn using
            **initialColor** needs to be.
        """
        # TODO: implement this method
        ...

    @overload
    @abaqus_method_doc
    def setColor(self, colorMapping: AttributeColorMap):
        """This method specifies the color assignment using attributes specified by an
        AttributeColorMap object. The setColor method has the following arguments:

        Parameters
        ----------
        colorMapping
            An :py:class:`~abaqus.Canvas.AttributeColorMap.AttributeColorMap` object. Possible values are any
            AttributeColorMap object.
        """
        # TODO: implement this method
        ...

    @overload
    @abaqus_method_doc
    def setColor(
        self,
        leaf: Leaf,
        edgeColorWireHide: str = "",
        edgeColorFillShade: str = "",
        fillColor: str = "",
        nodeSymbolColor: str = "",
        nodeSymbolType: Literal[
            C.FILLED_CIRCLE,
            C.FILLED_SQUARE,
            C.FILLED_DIAMOND,
            C.FILLED_TRI,
            C.HOLLOW_CIRCLE,
            C.HOLLOW_SQUARE,
            C.HOLLOW_DIAMOND,
            C.HOLLOW_TRI,
            C.CROSS,
            C.XMARKER,
        ] = HOLLOW_CIRCLE,
        nodeSymbolSize: Literal[C.SMALL, C.MEDIUM, C.LARGE] = SMALL,
    ):
        """This method specifies the color of a Leaf object.

        Parameters
        ----------
        leaf
            A :py:class:`~abaqus.DisplayGroup.Leaf.Leaf` object. Possible values are any Leaf object.
        edgeColorWireHide
            A String specifying the color to be used for drawing the edges of the elements contained
            in **leaf** when the render style is wireframe or hidden.
        edgeColorFillShade
            A String specifying the color to be used for drawing the edges of the elements contained
            in **leaf** when the render style is filled or shaded.
        fillColor
            A String specifying the color to be used for drawing the faces of the elements contained
            in **leaf** when the render style is filled or shaded.
        nodeSymbolColor
            A String specifying the color to be used for drawing the nodes contained in **leaf**.
        nodeSymbolType
            A SymbolicConstant specifying the node symbol types for the nodes contained in **leaf**.
            Possible values are FILLED_CIRCLE, FILLED_SQUARE, FILLED_DIAMOND, FILLED_TRI,
            HOLLOW_CIRCLE, HOLLOW_SQUARE, HOLLOW_DIAMOND, HOLLOW_TRI, CROSS, and XMARKER. The
            default value is HOLLOW_CIRCLE.
        nodeSymbolSize
            A SymbolicConstant specifying the node symbol size for the nodes contained in **leaf**.
            Possible values are SMALL, MEDIUM, and LARGE. The default value is SMALL.
        """
        # TODO: implement this method
        ...

    @abaqus_method_doc
    def setColor(self, *args, **kwargs):
        # TODO: implement this method
        ...

    def forceRefresh(self):
        """This method causes the Viewport to refresh immediately. It is provided to allow scripts
        to refresh the Viewport before the script terminates. Normally, there would only be a
        single cumulative refresh that takes place immediately after the script completes.
        """
        # TODO: implement this method
        ...

    @abaqus_method_doc
    def setValues(
        self,
        displayedObject: Optional[Displayable] = None,
        displayMode: Optional[Literal[C.SINGLE, C.OVERLAY]] = None,
        visibleLayers: Sequence[str] = (),
        viewManipLayers: Optional[Literal[C.ALL, C.CURRENT]] = None,
        currentLayer: str = "",
        layerOffset: Optional[float] = None,
    ):
        """This method modifies the Viewport object. The arguments to setValues are the same as the
        arguments to the Viewport method, except for the **name** argument. In addition, the
        setValues method has the following arguments:

        Parameters
        ----------
        displayedObject
            A :py:class:`~abaqus.Canvas.Displayable.Displayable` object specifying the object to be displayed. The
            Displayable type is an abstract generalization. The concrete possible types are Part, Assembly,
            ConstrainedSketch, Odb, PlyStackPlot, or XYPlot. If **displayedObject** = None, Abaqus
            displays an empty viewport.
        displayMode
            A SymbolicConstant specifying the display mode of the viewport. Possible values
            are:

            * SINGLE, specifying a single **displayedObject**.
            * OVERLAY, specifying one or more layers to be displayed simultaneously—each layer contains one **displayedObject**.

        visibleLayers
            A sequence of Strings specifying the names of layers that will be displayed in the
            viewport when **displayMode** = OVERLAY.
        viewManipLayers
            A SymbolicConstant specifying which layer or layers will be controlled by the view
            manipulation tools when **displayMode** = OVERLAY. Possible values are ALL and CURRENT.
        currentLayer
            A String specifying which layer is affected by options settings when **displayMode**
            =OVERLAY. The current layer is also the only layer affected by view manipulations
            when*viewManipLayers* =CURRENT.
        layerOffset
            A Float specifying a factor to be used in offsetting layers in the screen Z direction.
            Possible values are -1 to 1. A negative value reverses the apparent order in which the
            layers are plotted.

        Raises
        ------
        RangeError
        """
        super().setValues(
            displayedObject=displayedObject,
            displayMode=displayMode,
            visibleLayers=visibleLayers,
            viewManipLayers=viewManipLayers,
            currentLayer=currentLayer,
            layerOffset=layerOffset,
        )

    @abaqus_method_doc
    def addDrawings(self, names: tuple = ()):
        """This method identifies the names of Drawing objects to be rendered in the Viewport.

        Parameters
        ----------
        names
            A sequence of String values identifying keys in the session.drawings repository.

        Raises
        ------
        ValueError
        """
        # TODO: implement this method
        ...

    @abaqus_method_doc
    def removeDrawings(self, names: tuple = ()):
        """This method identifies the names of Drawing objects to no longer be rendered in the
        Viewport.

        Parameters
        ----------
        names
            A sequence of String values identifying keys in the Viewport sequence.

        Raises
        ------
        ValueError
        """
        # TODO: implement this method
        ...

    @abaqus_method_doc
    def timeDisplay(self, numFrames: int = 0, numSeconds: int = 10, degreesPerFrame: float = 0):
        """This method refreshes the Viewport display **numFrames** times and then checks to see if
        **numSeconds** seconds have elapsed. If not, it will continue refreshing the Viewport
        until the time has elapsed. At completion, the actual number of refreshes (frames)
        rendered and elapsed time will be reported along with the calculated frames-per-second
        (fps).

        Parameters
        ----------
        numFrames
            An Int specifying the minimum number of times to refresh the Viewport. The default value
            is 0.
        numSeconds
            An Int specifying the minimum number of seconds to spend refreshing the Viewport. The
            default value is 10.
        degreesPerFrame
            A Float specifying the number of degrees to rotate the model view about its Z axis
            before each refresh. The default value is 0.0.
        """
        # TODO: implement this method
        ...
