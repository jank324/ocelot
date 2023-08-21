"""Ocelot GUI tool"""

import sys

from app.gui import GUIWindow
from PyQt5.QtWidgets import QApplication


class OcelotWindow:
    def __init__(self):
        self.gui = GUIWindow()


def main():
    app = QApplication(sys.argv)
    window = OcelotWindow()
    window.gui.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
