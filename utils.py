import slicer
import qt
import logging  

class util():

    def __init__(self) -> None:
        #self.listOnScreenWidgets()
        self.mw = Widget(slicer.util.mainWindow())
        pass
    
    __shortcutDict = {
        "Scene3D"     : "CentralWidget/CentralWidgetLayoutFrame/ThreeDWidget1",
        "SceneRed"    : "CentralWidget/CentralWidgetLayoutFrame/qMRMLSliceWidgetRed",
        "SceneYellow" : "CentralWidget/CentralWidgetLayoutFrame/qMRMLSliceWidgetYellow",
        "SceneGreen"  : "CentralWidget/CentralWidgetLayoutFrame/qMRMLSliceWidgetGreen",
        "Module"      : "PanelDockWidget/dockWidgetContents/ModulePanel/ScrollArea/qt_scrollarea_viewport/scrollAreaWidgetContents"
    }

    def listOnScreenWidgets(self):
        print(self.mw.className, end=", ")
        print(self.mw.name)
        self.__getWidgetsRecursive(self.mw, 1)

    def __getWidgetsRecursive(self, widget, depth):
        children = widget.getChildren()
        for child in children:
            if child.name != "" and child.className != "QAction":
                for i in range(depth):
                    print("\t", end="")
                print(child.className, end=", ")
                print(child.name)
                self.__getWidgetsRecursive(child, depth + 1)

    def getNamedWidget(self, path, widget=None):
        if path == "":
            return
        if not widget:
            widget = self.mw
        wNames = path.split("/")
        extendedPath = self.widgetShortcuts(wNames[0])
        extendedPath.extend(wNames[1:])
        for name in extendedPath:
            widget = widget.getNamedChild(name)
            if not widget:
                return None
        return widget
    
    def widgetShortcuts(self, shortcut):
        if shortcut in self.__shortcutDict.keys():
            return self.__shortcutDict[shortcut].split("/")
        else:
            return [shortcut]
    
    def getWidgetsByToolTip(self, parent, tooltip):
        widgets = []
        if not parent:
            parent = self.mw
        if tooltip == "":
            return widgets
        for child in parent.getChildren():
            if child.toolTip == tooltip:
                widgets.append(child)
        return widgets
    
    def getWidgetsByClassName(self, parent, classname):
        widgets = []
        if not parent:
            parent = self.mw
        if classname == "":
            return widgets
        for child in parent.getChildren():
            if child.className == classname:
                widgets.append(child)
        return widgets

    def static(x):
        print("Hello, world"*x)
        
        
class WidgetFinder(qt.QWidget):
    def __init__(self, parent=None):
        super(WidgetFinder, self).__init__(parent)
        self.setAttribute(qt.Qt.WA_StyledBackground)
        self.setStyleSheet("QWidget { background-color: rgba(153, 51, 153, 50)}")
        self.focusPolicy = qt.Qt.StrongFocus
        self.LanguageToolsLogic = None
        self.shortcutKeySequence = qt.QKeySequence("Ctrl+6")
        self.shortcut = None
        self.logic = None
        self.cursorOverridden = False

    def __del__(self):
        self.showPointCursor(False)

    def enableShortcut(self, enable):
        if (self.shortcut is not None) == enable:
            return
        if self.shortcut:
            self.shortcut.disconnect("activated()")
            self.shortcut.setParent(None)
            self.shortcut.deleteLater()
            self.shortcut = None
            self.hideOverlay()
        else:
            self.shortcut = qt.QShortcut(self.parent())
            self.shortcut.setKey(self.shortcutKeySequence)
            self.shortcut.connect( "activated()", self.showFullSize)

    def showPointCursor(self, enable):
        if enable == self.cursorOverridden:
            return
        if enable:
            slicer.app.setOverrideCursor(qt.Qt.PointingHandCursor)
        else:
            slicer.app.restoreOverrideCursor()
        self.cursorOverridden = enable

    def showFullSize(self):
        self.pos = qt.QPoint()
        self.setFixedSize(self.parent().size)
        self.show()
        self.setFocus(qt.Qt.ActiveWindowFocusReason)
        self.showPointCursor(True)

    def overlayOnWidget(self, widget):
        pos = widget.mapToGlobal(qt.QPoint())
        pos = self.parent().mapFromGlobal(pos)
        self.pos = pos
        self.setFixedSize(widget.size)

    def hideOverlay(self):
        self.hide()
        self.showPointCursor(False)

    def widgetAtPos(self, pos):
        self.setAttribute(qt.Qt.WA_TransparentForMouseEvents)
        widget = qt.QApplication.widgetAt(pos)
        self.setAttribute(qt.Qt.WA_TransparentForMouseEvents, False)
        return widget

    def keyPressEvent(self, event):
        self.hideOverlay()

    def mousePressEvent(self, event):
        # Get widget at mouse position
        pos = qt.QCursor().pos()
        widget = self.widgetAtPos(pos)
        slicer.TextFinderLastWidget = widget  # useful for debugging
        logging.info("Widget found: "+widget.objectName)
        self.overlayOnWidget(widget)
        self.showPointCursor(False)
        print(widget)
    
        
class Widget():
    def __init__(self, widgetData) -> None:
        self.__widgetData = widgetData
        self.name = widgetData.name
        self.className = widgetData.className()
        if not hasattr(self.__widgetData, 'toolTip'):
            self.toolTip = "None"
        else:
            self.toolTip = widgetData.toolTip
        if not hasattr(self.__widgetData, 'text'):
            self.text = "None"
        else:
            self.text = widgetData.text
        pass

    def __str__(self):
        string = "Widget:\n"
        string += "\tName:      " + self.name + "\n"
        string += "\tText:      " + self.text + "\n"
        string += "\tToolTip:   " + self.toolTip + "\n"
        string += "\tClassName: " + self.className + "\n"
        string += "\tID:        " + hex(id(self.__widgetData)) + "\n"
        return string
    
    def inner(self):
        return self.__widgetData

    def getNamedChild(self, childName):
        if not hasattr(self.__widgetData, 'children'):
            return None
        for child in self.__widgetData.children():
            if child.name == childName:
                return Widget(child)
        return None

    def getChildren(self):
        children = []
        if not hasattr(self.__widgetData, 'children'):
            return children
        for child in self.__widgetData.children():
            children.append(Widget(child))
        return children
    
    def childrenDetails(self):
        children = self.getChildren()
        for child in children:
            print(child)
    
    def click(self):
        return self.__widgetData.click()
    
    def getGlobalPos(self):
        mw = slicer.util.mainWindow()
        windowPos = mw.mapToGlobal(mw.rect.topLeft())

        globalPosTopLeft = self.__widgetData.mapToGlobal(self.__widgetData.rect.topLeft())
        return [globalPosTopLeft.x() - windowPos.x(), globalPosTopLeft.y() - windowPos.y()]
    
    def getSize(self):
        posTopLeft = self.__widgetData.rect.topLeft()
        posBotRight = self.__widgetData.rect.bottomRight()
        return [posBotRight.x() - posTopLeft.x(), posBotRight.y() - posTopLeft.y()]
