from PySide6.QtCore import QTimer
from PySide6.QtWidgets import (
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QVBoxLayout,
    QWidget,
)

from app.services.system_service import get_system_stats


class DashboardWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("AI Dashboard")
        self.resize(1000, 600)

        self.setup_ui()
        self.setup_timer()

    def setup_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)

        title = QLabel("AI Dashboard")
        main_layout.addWidget(title)

        cards_layout = QHBoxLayout()
        main_layout.addLayout(cards_layout)

        self.system_card = QLabel()
        self.time_card = QLabel("TIME\n--:--:--")
        self.learning_card = QLabel("LEARNING\nProgress: --%")

        cards_layout.addWidget(self.system_card)
        cards_layout.addWidget(self.time_card)
        cards_layout.addWidget(self.learning_card)

    def setup_timer(self):
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_system_stats)
        self.timer.start(1000)

        self.update_system_stats()

    def update_system_stats(self):
        stats = get_system_stats()

        self.system_card.setText(
            f"SYSTEM\n"
            f"CPU: {stats['cpu']:.1f}%\n"
            f"RAM: {stats['ram']:.1f}%\n"
            f"Storage: {stats['storage']:.1f}%"
        )