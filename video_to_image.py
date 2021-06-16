import cv2
import os
import sys
from PyQt5 import QtWidgets,uic
from PyQt5.QtWidgets import QFileDialog



class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi('video_to_images.ui', self) # Load the .ui file
        videoYeriAlinan = " "
        kayitYeriAlinan = " "
        self.buttonVideoSec.clicked.connect(self.videoYeriBul)
        self.buttonKayitYerSec.clicked.connect(self.kayitYerBul)
        self.buttonBaslat.clicked.connect(self.basla)
        self.show()

    def basla(self):
        if self.kayitYeriAlinan!="" and self.videoYeriAlinan!="":
            self.buttonBaslat.setText("Çalışıyor, Bekleyiniz....")
            cam = cv2.VideoCapture(str(self.videoYeriAlinan))
            os.chdir(self.kayitYeriAlinan)
            currentframe = 0
            while (True):
                ret, frame = cam.read()
                if ret:
                    name = str(currentframe) + '.jpg'
                    cv2.imwrite(str(name), frame)
                    currentframe += 1
                else:
                    break

                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

            cam.release()
            cv2.destroyAllWindows()
            self.buttonBaslat.setText("Bitti....")

    def videoYeriBul(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                  "All Files (*);;Video Files (*.mp4)", options=options)
        if fileName:
            name = fileName.split("/")
            self.labelVideoYer.setText(name[-1])
            self.videoYeriAlinan=fileName
        self.buttonBaslat.setText("BASLAT")
    def kayitYerBul(self):
        secilenKlasor = QFileDialog.getExistingDirectory(self, caption='Choose Directory', directory=os.getcwd())
        if secilenKlasor:
            name = secilenKlasor.split("/")
            self.labelKayitYer.setText(name[-1])
            self.kayitYeriAlinan=secilenKlasor
        self.buttonBaslat.setText("BASLAT")




if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    app.exec_()