import sys
from PyQt5.QtWidgets import QApplication
from models.clock_model import ClockModel
from controllers.clock_controller import ClockController
from views.clock_view import AlarmClock
import qtmodern.styles
import qtmodern.windows


class App(QApplication):
    def __init__(self, sys_argv):
        super(App, self).__init__(sys_argv)
        self.model = ClockModel()
        self.main_controller = ClockController(self.model)
        self.main_view = None

    # Hack to get qtmodern style working. qtmodern has to set the style before initializing the window
    def show_window(self):
        self.main_view = qtmodern.windows.ModernWindow(AlarmClock(self.model, self.main_controller))
        self.main_view.show()


if __name__ == '__main__':
    app = App(sys.argv)
    qtmodern.styles.dark(app)
    app.show_window()
    sys.exit(app.exec_())
