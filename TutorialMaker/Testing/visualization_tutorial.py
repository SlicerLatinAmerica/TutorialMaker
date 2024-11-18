# https://github.com/spujol/SlicerVisualizationTutorial/blob/master/SlicerVisualizationTutorial_SoniaPujol.pdf
import slicer
import SampleData

import Lib.utils as utils

from slicer.ScriptedLoadableModule import *

# VisualizationTutorial


class VisualizationTutorialTest(ScriptedLoadableModuleTest):
    """
    This is the test case for your scripted module.
    Uses ScriptedLoadableModuleTest base class, available at:
    https://github.com/Slicer/Slicer/blob/main/Base/Python/slicer/ScriptedLoadableModule.py
    """

    def setUp(self):
        """Do whatever is needed to reset the state - typically a scene clear will be enough."""
        slicer.mrmlScene.Clear(0)

    def runTest(self):
        """Run as few or as many tests as needed here."""
        self.setUp()
        self.test_VisualizationTutorial1()

    def test_VisualizationTutorial1(self):
        """Tests parts of the VisualizationTutorial tutorial."""
        self.Tutorial = utils.Tutorial(
            "Slicer	Welcome", "Sonia Pujol, Ph.D.", "28/08/2024", "description"
        )

        self.util = utils.util()
        self.layoutManager = slicer.app.layoutManager()
        self.mainWindow = slicer.util.mainWindow()

        self.COLORS = ["Red", "Green", "Yellow"]
        self.CENTRAL_WIDGETS_PATH = "CentralWidget/CentralWidgetLayoutFrame/QSplitter:0/QWidget:0/qMRMLSliceWidget"

        # Clear Output folder
        self.Tutorial.clearTutorial()
        self.Tutorial.beginTutorial()
        self.delayDisplay("Starting the test")

        # Run Visualization Tutorial - Part 1
        self.runVisualizationTutorialPart1()

        # Run Visualization Tutorial - Part 2
        self.runVisualizationTutorialPart2()

        # Run Visualization Tutorial - Part 3
        self.runVisualizationTutorialPart3()

        # Done
        self.Tutorial.endTutorial()
        self.delayDisplay("Test passed!")

    def runVisualizationTutorialPart1(self):
        pass

    def runVisualizationTutorialPart2(self):
        pass

    def runVisualizationTutorialPart3(self):
        # 1 shot:
        self.mainWindow.moduleSelector().selectModule("Welcome")
        self.layoutManager.setLayout(slicer.vtkMRMLLayoutNode.SlicerLayoutConventionalView)
        self.Tutorial.nextScreenshot()
        self.delayDisplay("Screenshot #1: In the Welcome screen.")

        # 2 shot:
        TESTING_DATA_URL = "https://github.com/Slicer/SlicerTestingData/releases/download/"

        try:
            SampleData.downloadFromURL(
                fileNames='slicer4minute.mrb',
                loadFiles=True,
                uris=TESTING_DATA_URL + 'SHA256/5a1c78c3347f77970b1a29e718bfa10e5376214692d55a7320af94b9d8d592b8',
                checksums='SHA256:5a1c78c3347f77970b1a29e718bfa10e5376214692d55a7320af94b9d8d592b8')
            self.delayDisplay('Finished with download and loading')
        except:
            pass

        self.mainWindow.moduleSelector().selectModule('Models')
        self.Tutorial.nextScreenshot()
        self.delayDisplay('Screenshot #2: In the Models screen with the sample data loaded.')

        # 3 shot:
        self.pin_buttons = {
            color: self.util.getNamedWidget(
                f"{self.CENTRAL_WIDGETS_PATH}{color}/SliceController/BarWidget/PinButton"
            )
            for color in self.COLORS
        }

        self.visibility_buttons = {
            color: self.util.getNamedWidget(
                f"{self.CENTRAL_WIDGETS_PATH}{color}/SliceController/qMRMLSliceControllerWidget/SliceFrame/SliceVisibilityButton"
            )
            for color in self.COLORS
        }

        red_slice_position = -32
        self.red_slice_node = slicer.util.getNode("vtkMRMLSliceNodeRed")

        self.pin_buttons["Red"].click()
        self.visibility_buttons["Red"].click()
        self.red_slice_node.SetSliceOffset(red_slice_position)

        self.Tutorial.nextScreenshot()
        self.delayDisplay("Screenshot #3: Red slice plane adjusted to position -32 and its visibility toggled on.")

        # 4 shot:
        skin = slicer.util.getNode(pattern="Skin")
        skin.GetDisplayNode().SetOpacity(0.5)

        cam = slicer.util.getNode(pattern="vtkMRMLCameraNode1")
        cam.GetCamera().Azimuth(45)
        cam.GetCamera().Elevation(30)
        cam.GetCamera().Zoom(1.4)

        self.Tutorial.nextScreenshot()
        self.delayDisplay(
            "Screenshot #4: Adjusted the opacity of the skin model to 50% and updated the camera view (45° azimuth, 30° elevation, 1.4x zoom)."
        )

        # 5 shot:
        skull_bone = slicer.util.getNode(pattern="skull_bone")
        skull_bone.GetDisplayNode().SetVisibility(False)

        self.Tutorial.nextScreenshot()
        self.delayDisplay(
            "Screenshot #5: Skull bone model visibility turned off to isolate other structures."
        )

        # 6 shot:
        self.pin_buttons["Green"].click()
        self.visibility_buttons["Green"].click()

        self.Tutorial.nextScreenshot()
        self.delayDisplay(
            "Screenshot #6: Green slice plane visibility toggled on and its position adjusted."
        )

        # 7 shot:
        hemispheric_white_matter_display_node = slicer.util.getNode(pattern="hemispheric_white_matter").GetDisplayNode()

        hemispheric_white_matter_display_node.SetClipping(True)

        red_plane = self.util.getNamedWidget("PanelDockWidget/dockWidgetContents/ModulePanel/ScrollArea/qt_scrollarea_viewport/scrollAreaWidgetContents/ModelsModuleWidget/ClippingButton/MRMLClipNodeWidget/RedSliceClippingCheckBox")
        red_plane.click()

        green_plane = self.util.getNamedWidget("PanelDockWidget/dockWidgetContents/ModulePanel/ScrollArea/qt_scrollarea_viewport/scrollAreaWidgetContents/ModelsModuleWidget/ClippingButton/MRMLClipNodeWidget/GreenSliceClippingCheckBox")
        green_plane.click()

        self.Tutorial.nextScreenshot()
        self.delayDisplay(
            "Screenshot #7: Enabled clipping for the hemispheric white matter model using red and green slice planes."
        )

        # 8 shot:
        green_slice_position = -32
        self.green_slice_node = slicer.util.getNode("vtkMRMLSliceNodeGreen")
        self.green_slice_node.SetSliceOffset(green_slice_position)

        self.Tutorial.nextScreenshot()
        self.delayDisplay(
            "Screenshot #8: Adjusted the position of the green slice plane to -32 for further analysis."
        )

        # 9 shot:
        cam.GetCamera().Elevation(40)
        cam.GetCamera().Zoom(0.8)

        self.Tutorial.nextScreenshot()
        self.delayDisplay(
            "Screenshot #9: Final visualization with adjusted camera elevation (40°) and zoom level (0.8x)."
        )

