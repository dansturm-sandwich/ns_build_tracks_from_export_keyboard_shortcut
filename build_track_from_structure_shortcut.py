"""
Adds a Ctrl+B shortcut to open an action equivalent to "Right-click > Build Track > From Export Structure"
"""

import hiero.ui 
from PySide6 import QtGui 

class openBuildTrackMenu(QtGui.QAction): 

    def __init__(self): 
        super().__init__() 
        self.setObjectName("open_build_track_menu") 
        self.setShortcut("Ctrl+B") 
        self.triggered.connect(self.doit) 

    def doit(self):
        sequence = hiero.ui.activeSequence()
        if sequence is None:
            return False

        if not isinstance(hiero.ui.activeView(), hiero.ui.TimelineEditor):
            timeline = hiero.ui.getTimelineEditor(sequence)
            timeline.window().setFocus()

        hiero.ui.BuildExternalMediaTrack.BuildExternalMediaTrackAction().trigger() 

open_build_track_menu = openBuildTrackMenu() 
hiero.ui.registerAction(open_build_track_menu) 
hiero.ui.mainWindow().addAction(open_build_track_menu)