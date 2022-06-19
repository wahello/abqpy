from abaqusConstants import *
from ..PlotOptions.DGCommonOptions import DGCommonOptions


class CommonOptions(DGCommonOptions):
    """The CommonOptions object stores values and attributes that are common to all plot
    states. The CommonOptions object has no constructor command. Abaqus creates a
    *defaultOdbDisplay.commonOptions* member when you import the Visualization module.
    Abaqus creates a **commonOptions** member when it creates the OdbDisplay object, using the
    values from *defaultOdbDisplay.commonOptions*. Abaqus creates the **odbDisplay** member
    when a viewport is created, using the values from **defaultOdbDisplay**.
    CommonOptions objects are accessed in one of two ways:
    - The default common options. These settings are used as defaults when other
    **commonOptions** members are created. These settings can be set to customize user
    preferences.
    - The common options associated with a particular viewport.
    The CommonOptions object is derived from the DGCommonOptions object.

    Attributes
    ----------
    deformationScaling: SymbolicConstant
        A SymbolicConstant specifying the deformation scale factor mode. Possible values are
        AUTO, UNIFORM, and NONUNIFORM. The default value is AUTO.
    uniformScaleFactor: float
        A Float specifying the uniform deformation scaling constant when
        **deformationScaling=UNIFORM**. The default value is **autoDeformationScaleValue**.
    autoDeformationScaleValue: float
        A Float specifying the deformation scale factor value when **deformationScaling=AUTO**.
        This value is read-only.
    nonuniformScaleFactor: float
        A tuple of three Floats specifying the deformation scaling in each of the three
        coordinate directions when **deformationScaling=NONUNIFORM**. The default value is
        (**autoDeformationScaleValue**, **autoDeformationScaleValue**, **autoDeformationScaleValue**).
    renderStyle: SymbolicConstant
        A SymbolicConstant specifying the render style of the plot. Possible values are
        WIREFRAME, FILLED, HIDDEN, and SHADED. The default value is SHADED.
    visibleEdges: SymbolicConstant
        A SymbolicConstant specifying which edges to plot. Possible values are ALL, EXTERIOR,
        FEATURE, FREE, and NONE. The default value is EXTERIOR.NONE can be used only when
        **renderStyle=SHADED**.
    edgeLineStyle: SymbolicConstant
        A SymbolicConstant specifying the edge line style. Possible values are SOLID, DASHED,
        DOTTED, and DOT_DASH. The default value is SOLID.
    edgeLineThickness: SymbolicConstant
        A SymbolicConstant specifying the edge line thickness. Possible values are VERY_THIN,
        THIN, MEDIUM, and THICK. The default value is VERY_THIN.
    colorCodeOverride: Boolean
        A Boolean specifying whether to allow color coded items in the output database to
        override the edge and fill color settings. The default value is ON.
    elemLabels: Boolean
        A Boolean specifying whether to plot the element labels. The default value is OFF.
    faceLabels: Boolean
        A Boolean specifying whether to plot the face labels. The default value is OFF.
    nodeLabels: Boolean
        A Boolean specifying whether to plot the node labels. The default value is OFF.
    nodeSymbols: Boolean
        A Boolean specifying whether to plot the node symbols. The default value is OFF.
    nodeSymbolType: SymbolicConstant
        A SymbolicConstant specifying the node symbol types. Possible values are:
            - FILLED_CIRCLE
            - FILLED_SQUARE
            - FILLED_DIAMOND
            - FILLED_TRI
            - HOLLOW_CIRCLE
            - HOLLOW_SQUARE
            - HOLLOW_DIAMOND
            - HOLLOW_TRI
            - CROSS
            - XMARKER
        The default value is HOLLOW_CIRCLE.
    nodeSymbolSize: SymbolicConstant
        A SymbolicConstant specifying the node symbol size. Possible values are SMALL, MEDIUM,
        and LARGE. The default value is SMALL.
    elementShrink: Boolean
        A Boolean specifying whether elements are displayed in a shrunk format. The default
        value is OFF.
    elementShrinkFactor: int
        An Int specifying the percentage to shrink the elements when **elementShrink=ON**.
        Possible values are 0≤≤ **elementShrinkPercentage** ≤≤ 90. The default value is 5.
    coordinateScale: Boolean
        A Boolean specifying whether to scale coordinates. The default value is OFF.
    normals: Boolean
        A Boolean specifying whether to draw arrows that indicate the directions of element and
        surface normals. The default value is OFF.
    normalDisplay: SymbolicConstant
        A SymbolicConstant specifying whether to draw element normals or surface normals.
        Possible values are ELEMENT and SURFACE. The default value is ELEMENT.
    normalArrowLength: SymbolicConstant
        A SymbolicConstant specifying the length of the normal arrows. Possible values are
        SHORT, MEDIUM, and LONG. The default value is MEDIUM.
    normalLineThickness: SymbolicConstant
        A SymbolicConstant specifying the thickness of the normal arrows. Possible values are
        VERY_THIN, THIN, MEDIUM, and THICK. The default value is VERY_THIN.
    normalArrowheadStyle: SymbolicConstant
        A SymbolicConstant specifying the arrowhead style of the normal arrows. Possible values
        are NONE, FILLED, and WIRE. The default value is WIRE.
    translucency: Boolean
        A Boolean specifying whether to set translucency. The default value is OFF.
    translucencyFactor: float
        A Float specifying the translucency factor when **translucency=ON**. Possible values are
        0.0≤≤ **translucencyFactor** ≤≤ 1.0. The default value is 0.3.
    edgeColorWireHide: str
        A String specifying the color to be used to plot the edges of the model when
        **renderStyle=WIREFRAME** or HIDDEN. The default value is "White".
    edgeColorFillShade: str
        A String specifying the color to be used to plot the edges of the model when
        **renderStyle=FILLED** or SHADED. The default value is "Black".
    fillColor: str
        A String specifying the color to be used to fill elements when **renderStyle=FILLED** or
        SHADED. The default value is "White".
    labelFont: str
        A String specifying the label font to be used for all model labels. The default value is
        "-*-courier-medium-r-normal-*-*-120-*-*-m-*-*-*".
    elemLabelColor: str
        A String specifying the color to be used to plot the element labels. The default value
        is "Cyan".
    faceLabelColor: str
        A String specifying the color to be used to plot the face labels. The default value is
        "Red".
    nodeLabelColor: str
        A String specifying the color to be used to plot the node labels. The default value is
        "Yellow".
    nodeSymbolColor: str
        A String specifying the color to be used to plot the node symbols. The default value is
        "Yellow".
    faceNormalColor: str
        A String specifying the color to be used to plot the normal to a nonbeam element or to a
        surface. The default value is "Red".
    beamN1Color: str
        A String specifying the color to be used to plot an arrow along the beam n1n1-direction.
        The default value is "Blue".
    beamN2Color: str
        A String specifying the color to be used to plot an arrow along the beam n2n2-direction.
        The default value is "Red".
    beamTangentColor: str
        A String specifying the color to be used to plot an arrow along the tangent to a beam.
        The default value is "White".
    coordinateScaleFactors: float
        A tuple of three Floats specifying the coordinate scaling in each of the three
        coordinate directions when **coordinateScale=ON**. The default value is (1, 1, 1).

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import visualization
        session.defaultOdbDisplay.commonOptions
        session.viewports[name].assemblyDisplay.displayGroupInstances[name].odbDisplayOptions.commonOptions
        session.viewports[name].layers[name].assemblyDisplay.displayGroupInstances[name].odbDisplayOptions.commonOptions
        session.viewports[name].layers[name].odbDisplay.commonOptions
        session.viewports[name].layers[name].odbDisplay.displayGroupInstances[name].odbDisplayOptions.commonOptions
        session.viewports[name].layers[name].partDisplay.displayGroupInstances[name].odbDisplayOptions.commonOptions
        session.viewports[name].odbDisplay.commonOptions
        session.viewports[name].odbDisplay.displayGroupInstances[name].odbDisplayOptions.commonOptions
        session.viewports[name].partDisplay.displayGroupInstances[name].odbDisplayOptions.commonOptions

    """

    # A SymbolicConstant specifying the deformation scale factor mode. Possible values are
    # AUTO, UNIFORM, and NONUNIFORM. The default value is AUTO.
    deformationScaling: SymbolicConstant = AUTO

    # A Float specifying the uniform deformation scaling constant when
    # **deformationScaling**=UNIFORM. The default value is **autoDeformationScaleValue**.
    uniformScaleFactor: float = None

    # A Float specifying the deformation scale factor value when **deformationScaling**=AUTO.
    # This value is read-only.
    autoDeformationScaleValue: float = None

    # A tuple of three Floats specifying the deformation scaling in each of the three
    # coordinate directions when **deformationScaling**=NONUNIFORM. The default value is
    # (*autoDeformationScaleValue*, **autoDeformationScaleValue**, **autoDeformationScaleValue**).
    nonuniformScaleFactor: float = None

    # A SymbolicConstant specifying the render style of the plot. Possible values are
    # WIREFRAME, FILLED, HIDDEN, and SHADED. The default value is SHADED.
    renderStyle: SymbolicConstant = SHADED

    # A SymbolicConstant specifying which edges to plot. Possible values are ALL, EXTERIOR,
    # FEATURE, FREE, and NONE. The default value is EXTERIOR.NONE can be used only when
    # **renderStyle**=SHADED.
    visibleEdges: SymbolicConstant = EXTERIOR

    # A SymbolicConstant specifying the edge line style. Possible values are SOLID, DASHED,
    # DOTTED, and DOT_DASH. The default value is SOLID.
    edgeLineStyle: SymbolicConstant = SOLID

    # A SymbolicConstant specifying the edge line thickness. Possible values are VERY_THIN,
    # THIN, MEDIUM, and THICK. The default value is VERY_THIN.
    edgeLineThickness: SymbolicConstant = VERY_THIN

    # A Boolean specifying whether to allow color coded items in the output database to
    # override the edge and fill color settings. The default value is ON.
    colorCodeOverride: Boolean = ON

    # A Boolean specifying whether to plot the element labels. The default value is OFF.
    elemLabels: Boolean = OFF

    # A Boolean specifying whether to plot the face labels. The default value is OFF.
    faceLabels: Boolean = OFF

    # A Boolean specifying whether to plot the node labels. The default value is OFF.
    nodeLabels: Boolean = OFF

    # A Boolean specifying whether to plot the node symbols. The default value is OFF.
    nodeSymbols: Boolean = OFF

    # A SymbolicConstant specifying the node symbol types. Possible values are:
    # - FILLED_CIRCLE
    # - FILLED_SQUARE
    # - FILLED_DIAMOND
    # - FILLED_TRI
    # - HOLLOW_CIRCLE
    # - HOLLOW_SQUARE
    # - HOLLOW_DIAMOND
    # - HOLLOW_TRI
    # - CROSS
    # - XMARKER
    # The default value is HOLLOW_CIRCLE.
    nodeSymbolType: SymbolicConstant = HOLLOW_CIRCLE

    # A SymbolicConstant specifying the node symbol size. Possible values are SMALL, MEDIUM,
    # and LARGE. The default value is SMALL.
    nodeSymbolSize: SymbolicConstant = SMALL

    # A Boolean specifying whether elements are displayed in a shrunk format. The default
    # value is OFF.
    elementShrink: Boolean = OFF

    # An Int specifying the percentage to shrink the elements when **elementShrink**=ON.
    # Possible values are 0≤≤ **elementShrinkPercentage** ≤≤ 90. The default value is 5.
    elementShrinkFactor: int = 5

    # A Boolean specifying whether to scale coordinates. The default value is OFF.
    coordinateScale: Boolean = OFF

    # A Boolean specifying whether to draw arrows that indicate the directions of element and
    # surface normals. The default value is OFF.
    normals: Boolean = OFF

    # A SymbolicConstant specifying whether to draw element normals or surface normals.
    # Possible values are ELEMENT and SURFACE. The default value is ELEMENT.
    normalDisplay: SymbolicConstant = ELEMENT

    # A SymbolicConstant specifying the length of the normal arrows. Possible values are
    # SHORT, MEDIUM, and LONG. The default value is MEDIUM.
    normalArrowLength: SymbolicConstant = MEDIUM

    # A SymbolicConstant specifying the thickness of the normal arrows. Possible values are
    # VERY_THIN, THIN, MEDIUM, and THICK. The default value is VERY_THIN.
    normalLineThickness: SymbolicConstant = VERY_THIN

    # A SymbolicConstant specifying the arrowhead style of the normal arrows. Possible values
    # are NONE, FILLED, and WIRE. The default value is WIRE.
    normalArrowheadStyle: SymbolicConstant = WIRE

    # A Boolean specifying whether to set translucency. The default value is OFF.
    translucency: Boolean = OFF

    # A Float specifying the translucency factor when **translucency**=ON. Possible values are
    # 0.0≤≤ **translucencyFactor** ≤≤ 1.0. The default value is 0.3.
    translucencyFactor: float = 0

    # A String specifying the color to be used to plot the edges of the model when
    # **renderStyle**=WIREFRAME or HIDDEN. The default value is "White".
    edgeColorWireHide: str = ""

    # A String specifying the color to be used to plot the edges of the model when
    # **renderStyle**=FILLED or SHADED. The default value is "Black".
    edgeColorFillShade: str = ""

    # A String specifying the color to be used to fill elements when **renderStyle**=FILLED or
    # SHADED. The default value is "White".
    fillColor: str = ""

    # A String specifying the label font to be used for all model labels. The default value is
    # "-*-courier-medium-r-normal-*-*-120-*-*-m-*-*-*".
    labelFont: str = ""

    # A String specifying the color to be used to plot the element labels. The default value
    # is "Cyan".
    elemLabelColor: str = ""

    # A String specifying the color to be used to plot the face labels. The default value is
    # "Red".
    faceLabelColor: str = ""

    # A String specifying the color to be used to plot the node labels. The default value is
    # "Yellow".
    nodeLabelColor: str = ""

    # A String specifying the color to be used to plot the node symbols. The default value is
    # "Yellow".
    nodeSymbolColor: str = ""

    # A String specifying the color to be used to plot the normal to a nonbeam element or to a
    # surface. The default value is "Red".
    faceNormalColor: str = ""

    # A String specifying the color to be used to plot an arrow along the beam n1n1-direction.
    # The default value is "Blue".
    beamN1Color: str = ""

    # A String specifying the color to be used to plot an arrow along the beam n2n2-direction.
    # The default value is "Red".
    beamN2Color: str = ""

    # A String specifying the color to be used to plot an arrow along the tangent to a beam.
    # The default value is "White".
    beamTangentColor: str = ""

    # A tuple of three Floats specifying the coordinate scaling in each of the three
    # coordinate directions when **coordinateScale**=ON. The default value is (1, 1, 1).
    coordinateScaleFactors: float = None

    def setValues(
        self,
        options: "CommonOptions" = None,
        renderStyle: SymbolicConstant = SHADED,
        visibleEdges: SymbolicConstant = EXTERIOR,
        deformationScaling: SymbolicConstant = AUTO,
        uniformScaleFactor: float = None,
        nonuniformScaleFactor: tuple = (),
        edgeColorWireHide: str = "",
        edgeColorFillShade: str = "",
        edgeLineStyle: SymbolicConstant = SOLID,
        edgeLineThickness: SymbolicConstant = VERY_THIN,
        fillColor: str = "",
        colorCodeOverride: Boolean = ON,
        labelFont: str = "",
        elemLabels: Boolean = OFF,
        elemLabelColor: str = "",
        faceLabels: Boolean = OFF,
        faceLabelColor: str = "",
        nodeLabels: Boolean = OFF,
        nodeLabelColor: str = "",
        nodeSymbols: Boolean = OFF,
        nodeSymbolType: SymbolicConstant = HOLLOW_CIRCLE,
        nodeSymbolColor: str = "",
        nodeSymbolSize: SymbolicConstant = SMALL,
        elementShrink: Boolean = OFF,
        elementShrinkFactor: int = 5,
        coordinateScale: Boolean = OFF,
        coordinateScaleFactors: tuple = (),
        normals: Boolean = OFF,
        normalDisplay: SymbolicConstant = ELEMENT,
        faceNormalColor: str = "",
        beamN1Color: str = "",
        beamN2Color: str = "",
        beamTangentColor: str = "",
        normalArrowLength: SymbolicConstant = MEDIUM,
        normalLineThickness: SymbolicConstant = VERY_THIN,
        normalArrowheadStyle: SymbolicConstant = WIRE,
        translucency: Boolean = OFF,
        translucencyFactor: float = 0,
    ):
        """This method modifies the CommonOptions object.

        Parameters
        ----------
        options
            A CommonOptions object from which values are to be copied. If other arguments are also
            supplied to setValues, they will override the values in **options**. The default value is
            None.
        renderStyle
            A SymbolicConstant specifying the render style of the plot. Possible values are
            WIREFRAME, FILLED, HIDDEN, and SHADED. The default value is SHADED.
        visibleEdges
            A SymbolicConstant specifying which edges to plot. Possible values are ALL, EXTERIOR,
            FEATURE, FREE, and NONE. The default value is EXTERIOR.NONE can be used only when
            **renderStyle**=SHADED.
        deformationScaling
            A SymbolicConstant specifying the deformation scale factor mode. Possible values are
            AUTO, UNIFORM, and NONUNIFORM. The default value is AUTO.
        uniformScaleFactor
            A Float specifying the uniform deformation scaling constant when
            **deformationScaling**=UNIFORM. The default value is **autoDeformationScaleValue**.
        nonuniformScaleFactor
            A sequence of three Floats specifying the deformation scaling in each of the three
            coordinate directions when **deformationScaling**=NONUNIFORM. The default value is
            (*autoDeformationScaleValue*, **autoDeformationScaleValue**, **autoDeformationScaleValue**).
        edgeColorWireHide
            A String specifying the color to be used to plot the edges of the model when
            **renderStyle**=WIREFRAME or HIDDEN. The default value is "White".
        edgeColorFillShade
            A String specifying the color to be used to plot the edges of the model when
            **renderStyle**=FILLED or SHADED. The default value is "Black".
        edgeLineStyle
            A SymbolicConstant specifying the edge line style. Possible values are SOLID, DASHED,
            DOTTED, and DOT_DASH. The default value is SOLID.
        edgeLineThickness
            A SymbolicConstant specifying the edge line thickness. Possible values are VERY_THIN,
            THIN, MEDIUM, and THICK. The default value is VERY_THIN.
        fillColor
            A String specifying the color to be used to fill elements when **renderStyle**=FILLED or
            SHADED. The default value is "White".
        colorCodeOverride
            A Boolean specifying whether to allow color coded items in the output database to
            override the edge and fill color settings. The default value is ON.
        labelFont
            A String specifying the label font to be used for all model labels. The default value is
            "-*-courier-medium-r-normal-*-*-120-*-*-m-*-*-*".
        elemLabels
            A Boolean specifying whether to plot the element labels. The default value is OFF.
        elemLabelColor
            A String specifying the color to be used to plot the element labels. The default value
            is "Cyan".
        faceLabels
            A Boolean specifying whether to plot the face labels. The default value is OFF.
        faceLabelColor
            A String specifying the color to be used to plot the face labels. The default value is
            "Red".
        nodeLabels
            A Boolean specifying whether to plot the node labels. The default value is OFF.
        nodeLabelColor
            A String specifying the color to be used to plot the node labels. The default value is
            "Yellow".
        nodeSymbols
            A Boolean specifying whether to plot the node symbols. The default value is OFF.
        nodeSymbolType
            A SymbolicConstant specifying the node symbol types. Possible values are:

            - FILLED_CIRCLE
            - FILLED_SQUARE
            - FILLED_DIAMOND
            - FILLED_TRI
            - HOLLOW_CIRCLE
            - HOLLOW_SQUARE
            - HOLLOW_DIAMOND
            - HOLLOW_TRI
            - CROSS
            - XMARKER
            The default value is HOLLOW_CIRCLE.
        nodeSymbolColor
            A String specifying the color to be used to plot the node symbols. The default value is
            "Yellow".
        nodeSymbolSize
            A SymbolicConstant specifying the node symbol size. Possible values are SMALL, MEDIUM,
            and LARGE. The default value is SMALL.
        elementShrink
            A Boolean specifying whether elements are displayed in a shrunk format. The default
            value is OFF.
        elementShrinkFactor
            An Int specifying the percentage to shrink the elements when **elementShrink**=ON.
            Possible values are 0≤≤ **elementShrinkPercentage** ≤≤ 90. The default value is 5.
        coordinateScale
            A Boolean specifying whether to scale coordinates. The default value is OFF.
        coordinateScaleFactors
            A sequence of three Floats specifying the coordinate scaling in each of the three
            coordinate directions when **coordinateScale**=ON. The default value is (1, 1, 1).
        normals
            A Boolean specifying whether to draw arrows that indicate the directions of element and
            surface normals. The default value is OFF.
        normalDisplay
            A SymbolicConstant specifying whether to draw element normals or surface normals.
            Possible values are ELEMENT and SURFACE. The default value is ELEMENT.
        faceNormalColor
            A String specifying the color to be used to plot the normal to a nonbeam element or to a
            surface. The default value is "Red".
        beamN1Color
            A String specifying the color to be used to plot an arrow along the beam n1n1-direction.
            The default value is "Blue".
        beamN2Color
            A String specifying the color to be used to plot an arrow along the beam n2n2-direction.
            The default value is "Red".
        beamTangentColor
            A String specifying the color to be used to plot an arrow along the tangent to a beam.
            The default value is "White".
        normalArrowLength
            A SymbolicConstant specifying the length of the normal arrows. Possible values are
            SHORT, MEDIUM, and LONG. The default value is MEDIUM.
        normalLineThickness
            A SymbolicConstant specifying the thickness of the normal arrows. Possible values are
            VERY_THIN, THIN, MEDIUM, and THICK. The default value is VERY_THIN.
        normalArrowheadStyle
            A SymbolicConstant specifying the arrowhead style of the normal arrows. Possible values
            are NONE, FILLED, and WIRE. The default value is WIRE.
        translucency
            A Boolean specifying whether to set translucency. The default value is OFF.
        translucencyFactor
            A Float specifying the translucency factor when **translucency**=ON. Possible values are
            0.0≤≤ **translucencyFactor** ≤≤ 1.0. The default value is 0.3.

        Raises
        ------
        RangeError
        """
        pass
