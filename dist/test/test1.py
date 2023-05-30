from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QFrame, QPushButton
import sys

def toggle_frame_visibility():
    frame.setVisible(not frame.isVisible())

# 创建应用程序对象
app = QApplication(sys.argv)

# 创建主窗口
window = QWidget()
window.setWindowTitle("隐藏示例")

# 创建布局
layout = QVBoxLayout()

# 创建一个 QFrame
frame = QFrame()
frame.setStyleSheet("background-color: #FF0000;")  # 设置背景颜色为红色

# 添加按钮用于切换 QFrame 的可见性
button = QPushButton("切换可见性")
button.clicked.connect(toggle_frame_visibility)

# 将按钮添加到布局中
layout.addWidget(button)

# 设置主窗口的布局
window.setLayout(layout)

# 显示窗口
window.show()

# 运行应用程序
sys.exit(app.exec())




