from PyQt5 import QtWidgets
from Main_Window import Ui_MainWindow
from player import player
import sys
import glob


class mywindow(QtWidgets.QMainWindow, player):
    filesInDir:list
    isPaused:bool
    path:str
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #calling method for getting path to the music folder
        self.ui.actionSelect_folder.triggered.connect(self.getPath)
        #calling method for selection the item from combo box
        self.ui.filesList.activated.connect(self.comBoxSelect)

        #calling method which allow work with play-pause button
        self.ui.playPauseBtn.clicked.connect(self.playPause)

        #calling methods for "previous", "next" buttons
        self.ui.prevBtn.clicked.connect(self.playPrev)
        self.ui.nxtBtn.clicked.connect(self.playNext)

    def getMusicList(self):
        #gething all .mp3 files from selected folder
        self.filesInDir = glob.glob(f"{self.path}/*.mp3")

        #set isPaused none for play that file from beginnig
        self.isPaused = None

        #if in folder exist some .mp3 files, we load the firts one
        if len(self.filesInDir) > 0:
            player.getFile(self, self.filesInDir[0])

            #enabling bottons
            self.ui.playPauseBtn.setDisabled(False)
            self.ui.nxtBtn.setDisabled(False)
            self.ui.prevBtn.setDisabled(False)

            #adding items to combo box from list
            for i in self.filesInDir:
                self.ui.filesList.addItem(i)


    def comBoxSelect(self):
        print(str(self.ui.filesList.currentText()))

        #loading selected in check-box file
        player.getFile(self,str(self.ui.filesList.currentText()))

        #playing the selected file
        player.pyGMix.music.play()
        #set isPauset as False to know that file is playing
        self.isPaused = False
        self.ui.playPauseBtn.setText("Pause")

    #play-pause button method
    def playPause(self):
        #if file is first we start them from beginning
        if self.isPaused is None:
            player.pyGMix.music.play(-1)
            self.isPaused = False

        #if file is playing we pausing them
        elif not self.isPaused:
            player.pyGMix.music.pause()
            self.ui.playPauseBtn.setText("Continue")
            self.isPaused = True
        #if file is paused we unpause them
        else:
            player.pyGMix.music.unpause()
            self.ui.playPauseBtn.setText("Pause")
            self.isPaused = False


    def getPath(self):
        self.path = str(QtWidgets.QFileDialog.getExistingDirectory())
        self.getMusicList()


    def playPrev(self):
        self.playPrevNext(True)

    def playNext(self):
        self.playPrevNext(False)

    def playPrevNext(self, dir:bool):

        if dir:
            currIndex = int(self.ui.filesList.currentIndex() - 1)
        else:
            currIndex = int(self.ui.filesList.currentIndex() + 1)

        if currIndex < 0 or (currIndex >= len(self.filesInDir)):
            currIndex = int(self.ui.filesList.currentIndex())

        filePath = self.filesInDir[currIndex]

        self.ui.filesList.setCurrentIndex(currIndex)

        player.getFile(self,str(filePath))
        player.pyGMix.music.play(-1)





if __name__ == '__main__':

    app = QtWidgets.QApplication([])
    application = mywindow()
    application.show()

    sys.exit(app.exec())