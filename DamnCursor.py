#from PyQt5.QtCore import *
#from PyQt5.QtGui import *
#from PyQt5.QtWidgets import *

from PyQt4.QtCore import *
from PyQt4.QtGui import *



if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)

        
    desktop = QApplication.desktop()
    availableGeometry=desktop.availableGeometry()
    
    screenWidth=availableGeometry.width()
    screenHeight=availableGeometry.height()
    
    
    cursor=QCursor()
    lastPos=QCursor.pos()


    def checkCursorMoving():
        global lastPos
        currentPos=QCursor.pos()
        print(lastPos,currentPos,lastPos==currentPos)
        
        
        if lastPos==currentPos:
            cursor.setPos(screenWidth,screenHeight)

        lastPos=currentPos
        
    timer = QTimer()
    timer.timeout.connect(checkCursorMoving)
    timer.start(10000)

    def on_aboutDamnCursor_triggered():
        describ = 'DamnCursor 让该死的光标滚一边去！！！'
        QMessageBox.about(None, "关于 DamnCursor", describ)
    

    def on_aboutMe_triggered():
        describ = '''
<html>
<head/>

<body>

    <p>
        <span style=" font-size:10pt;">欢迎光临我的专页：</span>
        <a href="http://imath.diandian.com">
            <span style=" font-size:10pt; text-decoration: underline; color:#0000ff;">http://imath.diandian.com</span>
        </a>
    </p>
</body>

</html>
'''
        QMessageBox.about(None, "关于我", describ)

    def on_aboutQt_triggered():
        QMessageBox.aboutQt(None)
        
    quitAction =QAction("&Quit", None,triggered=qApp.quit)
    aboutDamnCursorAction = QAction("about DamnCursor",None,triggered=on_aboutDamnCursor_triggered)
    aboutAuthorAction = QAction("about Author",None,triggered=on_aboutMe_triggered)
    aboutQtAction = QAction("about Qt",None,triggered=on_aboutQt_triggered)

    
    trayIconMenu =QMenu()

    trayIconMenu.addAction(aboutAuthorAction)
    trayIconMenu.addAction(aboutQtAction)
    trayIconMenu.addAction(aboutDamnCursorAction)
    trayIconMenu.addAction(quitAction)

    trayIcon = QSystemTrayIcon()
    trayIcon.setContextMenu(trayIconMenu)
    trayIcon.setIcon(QIcon('DamnCursor.png'))
    trayIcon.show()

    sys.exit(app.exec_())  
