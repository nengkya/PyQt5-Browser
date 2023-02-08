#PyQt6 tidak auto login google account.
import PyQt5.QtNetwork, PyQt5.QtWidgets,\
    PyQt5.QtWebEngineWidgets, PyQt5.QtCore, sys

from http.cookies import SimpleCookie

class MainWindow(PyQt5.QtWidgets.QMainWindow):

    def __init__(self, * args, ** kwargs):

        super(MainWindow, self).__init__(* args, ** kwargs)

        self.loader  = PyQt5.QtWebEngineWidgets.QWebEngineView()

        self.profile = \
            PyQt5.QtWebEngineWidgets.QWebEngineProfile(\
                "storage", self.loader)

        self.cookie_store = self.profile.cookieStore()

        '''
        with open('cookie.txt', 'rb') as f:
            contents = f.read()
        '''

        cookie = SimpleCookie()
        cookie['name'] = 'value'
        cookie['name']['samesite'] = None
        cookie['name']['secure'] = True
        contents = cookie.output().encode('ascii')

        self.cookie_store.setCookie(\
            PyQt5.QtNetwork.QNetworkCookie(contents))

        self.webpage = \
            PyQt5.QtWebEngineWidgets.QWebEnginePage(\
                self.profile, self.loader)

        for qt_cookie in \
            PyQt5.QtNetwork.QNetworkCookie.parseCookies(contents):
            print(qt_cookie.toRawForm())
            self.cookie_store.setCookie(qt_cookie)

        self.setWindowTitle('HaGa Browser')

        self.setWindowIcon(PyQt5.QtGui.QIcon('viper.png'))

        self.loader.setUrl(PyQt5.QtCore.QUrl('http://www.google.com'))

        #Sets the given widget to be the main window’s central widget.
        self.setCentralWidget(self.loader)

        self.showMaximized()

#harus ada aplikasi terlebih dahulu, untuk dapat ada window.
application = PyQt5.QtWidgets.QApplication(sys.argv)

window = MainWindow()

#aplikasi dieksekusi
application.exec()
