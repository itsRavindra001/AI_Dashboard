import math
from PySide6.QtCore import QTimer, Qt, QPointF
from PySide6.QtGui import (
    QColor,
    QFont,
    QLinearGradient,
    QPainter,
    QPen,
    QRadialGradient,
)
from PySide6.QtWidgets import QMainWindow, QWidget

from app.services.system_service import get_system_stats
from app.services.time_service import get_current_time, get_current_date


class WallpaperWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.stats = {
            "cpu": 0,
            "ram": 0,
            "storage": 0,
        }

        self.time = ""
        self.date = ""

        self.angle = 0

        self.setAttribute(Qt.WidgetAttribute.WA_OpaquePaintEvent)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_wallpaper)
        self.timer.start(1000)

        self.update_wallpaper()

    def update_wallpaper(self):
        self.stats = get_system_stats()
        self.time = get_current_time()
        self.date = get_current_date()

        self.angle = (self.angle + 1) % 360

        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)

        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        width = self.width()
        height = self.height()

        self.draw_background(painter, width, height)
        self.draw_system_status(painter)
        self.draw_clock(painter, width, height)
        self.draw_learning_progress(painter, width, height)

        painter.end()

    # ---------------------------------------------------------
    # BACKGROUND
    # ---------------------------------------------------------

    def draw_background(self, painter, width, height):
        gradient = QLinearGradient(0, 0, width, height)

        gradient.setColorAt(0.0, QColor("#03070c"))
        gradient.setColorAt(0.45, QColor("#07111c"))
        gradient.setColorAt(1.0, QColor("#020409"))

        painter.fillRect(0, 0, width, height, gradient)

        # Subtle central glow
        glow = QRadialGradient(
            QPointF(width * 0.55, height * 0.48),
            min(width, height) * 0.45,
        )

        glow.setColorAt(0.0, QColor(20, 70, 110, 35))
        glow.setColorAt(0.55, QColor(10, 40, 70, 15))
        glow.setColorAt(1.0, QColor(0, 0, 0, 0))

        painter.fillRect(0, 0, width, height, glow)

        # Technology grid
        painter.setPen(QPen(QColor(40, 70, 95, 25), 1))

        grid_size = 70

        for x in range(0, width, grid_size):
            painter.drawLine(x, 0, x, height)

        for y in range(0, height, grid_size):
            painter.drawLine(0, y, width, y)

    # ---------------------------------------------------------
    # SYSTEM STATUS - LEFT
    # ---------------------------------------------------------

    def draw_system_status(self, painter):
        x = 55
        y = 60

        painter.setPen(QColor("#e8f1f8"))

        title_font = QFont("Segoe UI", 16)
        title_font.setBold(True)

        painter.setFont(title_font)

        painter.drawText(
            x,
            y,
            "SYSTEM STATUS",
        )

        painter.setPen(QColor("#3ed598"))

        painter.drawText(
            x,
            y + 28,
            "●  ONLINE",
        )

        items = [
            ("CPU", self.stats["cpu"]),
            ("RAM", self.stats["ram"]),
            ("STORAGE", self.stats["storage"]),
        ]

        y += 80

        for name, value in items:
            painter.setPen(QColor("#8392a0"))

            painter.setFont(QFont("Segoe UI", 10))

            painter.drawText(
                x,
                y,
                name,
            )

            painter.setPen(QColor("#e8f1f8"))

            value_font = QFont("Segoe UI", 17)
            value_font.setBold(True)

            painter.setFont(value_font)

            painter.drawText(
                x + 100,
                y,
                f"{value:.0f}%",
            )

            # Progress line
            bar_x = x
            bar_y = y + 10
            bar_width = 170
            bar_height = 3

            painter.setPen(Qt.PenStyle.NoPen)

            painter.setBrush(QColor("#17232e"))

            painter.drawRoundedRect(
                bar_x,
                bar_y,
                bar_width,
                bar_height,
                2,
                2,
            )

            painter.setBrush(QColor("#3e9cff"))

            painter.drawRoundedRect(
                bar_x,
                bar_y,
                int(bar_width * value / 100),
                bar_height,
                2,
                2,
            )

            y += 55

    # ---------------------------------------------------------
    # ROUND CLOCK - RIGHT
    # ---------------------------------------------------------

    def draw_clock(self, painter, width, height):
        center_x = width - 170
        center_y = 165

        radius = 100

        # Outer glow
        glow = QRadialGradient(
            QPointF(center_x, center_y),
            radius + 25,
        )

        glow.setColorAt(0.0, QColor(40, 150, 255, 30))
        glow.setColorAt(0.7, QColor(40, 120, 255, 10))
        glow.setColorAt(1.0, QColor(0, 0, 0, 0))

        painter.setBrush(glow)
        painter.setPen(Qt.PenStyle.NoPen)

        painter.drawEllipse(
            QPointF(center_x, center_y),
            radius + 25,
            radius + 25,
        )

        # Clock face
        painter.setBrush(QColor("#07111a"))

        painter.setPen(
            QPen(
                QColor("#3e9cff"),
                2,
            )
        )

        painter.drawEllipse(
            QPointF(center_x, center_y),
            radius,
            radius,
        )

        # Inner ring
        painter.setPen(
            QPen(
                QColor(70, 160, 255, 70),
                1,
            )
        )

        painter.drawEllipse(
            QPointF(center_x, center_y),
            radius - 12,
            radius - 12,
        )

        # Tick marks
        for i in range(60):
            angle = math.radians(i * 6)

            outer = radius - 5

            inner = radius - (15 if i % 5 == 0 else 10)

            x1 = center_x + math.cos(angle) * inner
            y1 = center_y + math.sin(angle) * inner

            x2 = center_x + math.cos(angle) * outer
            y2 = center_y + math.sin(angle) * outer

            painter.setPen(
                QPen(
                    QColor("#4d9fe8"),
                    2 if i % 5 == 0 else 1,
                )
            )

            painter.drawLine(
                QPointF(x1, y1),
                QPointF(x2, y2),
            )

        # Time
        painter.setPen(QColor("#ffffff"))

        time_font = QFont("Segoe UI", 18)
        time_font.setBold(True)

        painter.setFont(time_font)

        painter.drawText(
            center_x - 65,
            center_y + 8,
            self.time,
        )

        painter.setPen(QColor("#8293a2"))

        date_font = QFont("Segoe UI", 9)

        painter.setFont(date_font)

        painter.drawText(
            center_x - 55,
            center_y + 30,
            self.date,
        )

        # Center dot
        painter.setBrush(QColor("#3e9cff"))

        painter.drawEllipse(
            QPointF(center_x, center_y),
            4,
            4,
        )

    # ---------------------------------------------------------
    # AI / ML PROGRESS - BOTTOM LEFT
    # ---------------------------------------------------------

    def draw_learning_progress(self, painter, width, height):
        x = 55
        y = height - 175

        painter.setPen(QColor("#e8f1f8"))

        title_font = QFont("Segoe UI", 15)
        title_font.setBold(True)

        painter.setFont(title_font)

        painter.drawText(
            x,
            y,
            "AI / ML PROGRESS",
        )

        progress = [
            ("PYTHON", 72),
            ("MACHINE LEARNING", 35),
            ("DEEP LEARNING", 15),
        ]

        y += 35

        for name, value in progress:
            painter.setFont(QFont("Segoe UI", 9))
            painter.setPen(QColor("#8392a0"))

            painter.drawText(
                x,
                y,
                name,
            )

            painter.setPen(QColor("#ffffff"))

            painter.drawText(
                x + 170,
                y,
                f"{value}%",
            )

            # Progress bar
            painter.setPen(Qt.PenStyle.NoPen)

            painter.setBrush(QColor("#17232e"))

            painter.drawRoundedRect(
                x,
                y + 8,
                200,
                4,
                2,
                2,
            )

            painter.setBrush(QColor("#3e9cff"))

            painter.drawRoundedRect(
                x,
                y + 8,
                int(200 * value / 100),
                4,
                2,
                2,
            )

            y += 35


class DashboardWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("AI Dashboard")

        self.setWindowFlag(
            Qt.WindowType.FramelessWindowHint
        )

        self.setWindowFlag(
            Qt.WindowType.WindowStaysOnTopHint
        )

        self.showFullScreen()

        self.setCentralWidget(
            WallpaperWidget()
        )