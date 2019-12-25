from PyQt5 import QtWidgets
from Main_Window import Ui_MainWindow
from PyQt5.QtCore import QThread, pyqtSignal
from player import player
from mutagen.mp3 import MP3
import sys
import glob
import time


def convert(miliseconds: float):
    seconds = miliseconds / float(1000)
    return str(int((seconds) / 60)) + "." + str(round(seconds % 60, 2))


class ProgressMusic(QThread, player):
    currTime = pyqtSignal(int)
    cnt: int
    SongEnd = player.endEvent

    def run(self):
        while player.pyGMix.music.get_busy():
            cnt = player.pyGMix.music.get_pos()
            time.sleep(0.001)
            self.currTime.emit(cnt)

            while 1:
                if player.pygame.event.get() == self.SongEnd:
                    self.playNxt.emit()
                else:
                    break

    def __del__(self):
        self.terminate()


class mywindow(QtWidgets.QMainWindow, ProgressMusic):
    filesInDir: list
    isPaused: bool
    path: str

    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # calling method for getting path to the music folder
        self.ui.actionSelect_folder.triggered.connect(self.getPath)
        # calling method for selection the item from combo box
        self.ui.filesList.activated.connect(self.comBoxSelect)

        # calling method which allow work with play-pause button
        self.ui.playPauseBtn.clicked.connect(self.playPause)

        # calling methods for "previous", "next" buttons
        self.ui.prevBtn.clicked.connect(self.playPrev)
        self.ui.nxtBtn.clicked.connect(self.playNext)

        self.ui.playingTimeline.setMinimum(0)

    def nxtSong(self):
        file = self.filesInDir[self.ui.filesList.currentIndex() + 1]
        player.setFile(file)
        player.pyGMix.music.play()

    def setEndPos(self, path: str):
        song = MP3(path)
        seconds = song.info.length
        endPos = str(int((seconds) / 60)) + "." + str(round(seconds % 60, 2))
        self.ui.endPos.setText(endPos)
        self.ui.playingTimeline.setMaximum(seconds * 1000)

    def startProgressCount(self):
        self.thread = ProgressMusic()
        self.thread.currTime.connect(self.setProgressValue)
        self.thread.start()

    def setProgressValue(self, val):
        self.ui.curPos.setText(convert(val))
        self.ui.playingTimeline.setValue(val)

    def getMusicList(self):
        # gething all .mp3 files from selected folder
        self.filesInDir = glob.glob(f"{self.path}/*.mp3")

        # set isPaused none for play that file from beginnig
        self.isPaused = None

        # if in folder exist some .mp3 files, we load the firts one
        if len(self.filesInDir) > 0:
            player.setFile(self, self.filesInDir[0])
            self.setEndPos(self.filesInDir[0])

            # enabling bottons
            self.ui.playPauseBtn.setDisabled(False)
            self.ui.nxtBtn.setDisabled(False)
            self.ui.prevBtn.setDisabled(False)

            # adding items to combo box from list
            for i in self.filesInDir:
                self.ui.filesList.addItem(i)

    def comBoxSelect(self):
        print(str(self.ui.filesList.currentText()))

        # loading selected in check-box file
        player.setFile(self, str(self.ui.filesList.currentText()))

        # playing the selected file
        player.pyGMix.music.play()
        self.setEndPos(self.filesInDir[self.ui.filesList.currentIndex()])
        # set isPauset as False to know that file is playing
        self.isPaused = False
        self.ui.playPauseBtn.setText("Pause")

    # play-pause button method
    def playPause(self):
        # if file is first we start them from beginning
        if self.isPaused is None:
            player.pyGMix.music.play()
            self.startProgressCount()
            self.isPaused = False

        # if file is playing we pausing them
        elif not self.isPaused:
            player.pyGMix.music.pause()
            self.ui.playPauseBtn.setText("Continue")
            self.isPaused = True
        # if file is paused we unpause them
        else:
            player.pyGMix.music.unpause()
            self.ui.playPauseBtn.setText("Pause")
            self.isPaused = False

    def getPath(self):
        self.path = str(QtWidgets.QFileDialog.getExistingDirectory())
        self.getMusicList()


    def playPrev(self):
        currIndex = int(self.ui.filesList.currentIndex() - 1)
        if currIndex < 0 or (currIndex >= len(self.filesInDir)):
            currIndex = int(self.ui.filesList.currentIndex())

        filePath = self.filesInDir[currIndex]

        self.ui.filesList.setCurrentIndex(currIndex)

        self.setEndPos(filePath)

        player.setFile(self, str(filePath))
        player.pyGMix.music.play()
        #self.startProgressCount()

    def playNext(self):
        currIndex = int(self.ui.filesList.currentIndex() + 1)

        if currIndex < 0 or (currIndex >= len(self.filesInDir)):
            currIndex = int(self.ui.filesList.currentIndex())

        filePath = self.filesInDir[currIndex]

        self.ui.filesList.setCurrentIndex(currIndex)

        self.setEndPos(filePath)

        player.setFile(self, str(filePath))
        player.pyGMix.music.play()
        #self.startProgressCount()



def main():
    app = QtWidgets.QApplication([])
    application = mywindow()
    application.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
