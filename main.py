import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel, QVBoxLayout,
                             QHBoxLayout, QWidget, QFrame, QPushButton, QSlider,
                             QSpacerItem, QSizePolicy, QTableWidget, QTableWidgetItem)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont


class MRIAnomalyDetectionApp(QMainWindow):
    def __init__(self):
        super().__init__()

        # Main Window Setup
        self.setWindowTitle("MRI Anomaly Detection Interface")
        self.setGeometry(100, 100, 1100, 1100)

        # Central Widget and Layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QVBoxLayout()
        self.central_widget.setLayout(self.main_layout)

        # Top Row Layout: Button Bar, Image Display, Inventory Panel
        self.top_row_layout = QHBoxLayout()
        self.main_layout.addLayout(self.top_row_layout)

        # Button Bar Frame
        self.button_bar_frame = QFrame()
        self.button_bar_frame.setFrameShape(QFrame.Box)
        self.button_bar_frame.setFixedHeight(800)
        self.button_bar_layout = QVBoxLayout(self.button_bar_frame)
        self.top_row_layout.addWidget(self.button_bar_frame)

        # Clinical Rater Section
        self.bids_dataset_label = QLabel("Clinical Rater")
        self.bids_dataset_label.setAlignment(Qt.AlignCenter)
        self.button_bar_layout.addWidget(self.bids_dataset_label)

        # Separator
        self.separator = QFrame()
        self.separator.setFrameShape(QFrame.HLine)
        self.button_bar_layout.addWidget(self.separator)

        # BIDS Dataset Section
        self.bids_dataset_label = QLabel("BIDS Dataset")
        self.bids_dataset_label.setAlignment(Qt.AlignCenter)
        self.button_bar_layout.addWidget(self.bids_dataset_label)

        # Load Button
        self.load_button = QPushButton("Load")
        self.button_bar_layout.addWidget(self.load_button)

        # Separator
        self.separator = QFrame()
        self.separator.setFrameShape(QFrame.HLine)
        self.button_bar_layout.addWidget(self.separator)

        # "sub" Label and Text Area
        self.sub_label = QLabel("Subject")
        self.sub_label.setAlignment(Qt.AlignCenter)
        self.sub_text_area = QLabel("sub-101")
        self.sub_text_area.setFrameShape(QFrame.Box)
        self.button_bar_layout.addWidget(self.sub_label)
        self.button_bar_layout.addWidget(self.sub_text_area)

        # "ses" Label and Text Area
        self.ses_label = QLabel("Session")
        self.ses_label.setAlignment(Qt.AlignCenter)
        self.ses_text_area = QLabel("ses-01")
        self.ses_text_area.setFrameShape(QFrame.Box)
        self.button_bar_layout.addWidget(self.ses_label)
        self.button_bar_layout.addWidget(self.ses_text_area)

        # Separator
        self.separator = QFrame()
        self.separator.setFrameShape(QFrame.HLine)
        self.button_bar_layout.addWidget(self.separator)

        # Image Loading Buttons
        self.add_buttons(["T1w", "T2w", "FLAIR", "SWI", "ADC", "CBF"], "Image")

        # Separator
        self.separator = QFrame()
        self.separator.setFrameShape(QFrame.HLine)
        self.button_bar_layout.addWidget(self.separator)

        # Map Loading Buttons
        self.add_buttons(["Normal", "Lesion", "Lacune", "dPVS", "Bleed"], "Map")

        # Separator
        self.separator = QFrame()
        self.separator.setFrameShape(QFrame.HLine)
        self.button_bar_layout.addWidget(self.separator)

        # Load Button
        self.load_button = QPushButton("QUIT")
        self.button_bar_layout.addWidget(self.load_button)

        # Image Display Frame
        self.image_frame = QFrame()
        self.image_frame.setFixedSize(600, 860)
        self.image_frame.setFrameShape(QFrame.Box)
        self.image_frame_layout = QVBoxLayout(self.image_frame)
        self.image_label = QLabel("MRI Image Display")
        self.image_label.setAlignment(Qt.AlignCenter)
        self.image_frame_layout.addWidget(self.image_label)
        self.top_row_layout.addWidget(self.image_frame)

        # Additional Inventory Panel to the Right of Image
        self.inventory_panel = QFrame()
        self.inventory_panel.setFrameShape(QFrame.Box)
        self.inventory_panel_layout = QVBoxLayout(self.inventory_panel)
        self.inventory_panel_title = QLabel("CADA-MRIT")
        self.inventory_panel_title.setAlignment(Qt.AlignCenter)
        self.inventory_panel_layout.addWidget(self.inventory_panel_title)

        # Inventory Table
        self.inventory_table = QTableWidget(26, 2)
        self.inventory_table.setFixedSize(450, 810)
        self.inventory_table.setHorizontalHeaderLabels(["Label", "Response"])
        self.inventory_table.verticalHeader().setVisible(False)
        self.inventory_table.setColumnWidth(0, 325)
        self.inventory_table.setColumnWidth(1, 125)
        self.fill_inventory_table()

        self.inventory_panel_layout.addWidget(self.inventory_table)
        self.top_row_layout.addWidget(self.inventory_panel)

        # Bottom Row Layout: Sliders and Spacer
        self.bottom_row_layout = QHBoxLayout()

        # Frame for Image Sliders
        self.image_sliders_frame = self.create_sliders_frame(["T1w", "T2w", "FLAIR", "SWI", "ADC", "CBF"],
                                                             "Adjust Weights of Images")
        self.bottom_row_layout.addWidget(self.image_sliders_frame)

        # Frame for Map Sliders with an additional Button
        self.map_sliders_frame = self.create_sliders_frame(["Normal", "Lesion", "Lacune", "dPVS", "Bleed"],
                                                           "Adjust Weights of Maps")
        self.bottom_row_layout.addWidget(self.map_sliders_frame)

        # Third Object (You can customize this as needed)
        self.third_object_frame = QFrame()
        self.third_object_frame.setFrameShape(QFrame.Box)
        self.third_object_frame.setFixedWidth(175)  # Set a fixed width similar to the sliders
        self.third_object_layout = QVBoxLayout(self.third_object_frame)

        # Load Button
        self.load_button = QPushButton("Calculate Inventory")
        self.third_object_layout.addWidget(self.load_button)
        # Separator
        self.separator = QFrame()
        self.separator.setFrameShape(QFrame.HLine)
        self.third_object_layout.addWidget(self.separator)

        # Load Button
        self.load_button = QPushButton("Load Inventory")
        self.third_object_layout.addWidget(self.load_button)

        # Separator
        self.separator = QFrame()
        self.separator.setFrameShape(QFrame.HLine)
        self.third_object_layout.addWidget(self.separator)

        # Load Button
        self.load_button = QPushButton("Save Inventory")
        self.third_object_layout.addWidget(self.load_button)


        # Add any widgets or elements to this third object frame as needed
        self.bottom_row_layout.addWidget(self.third_object_frame)

        self.main_layout.addLayout(self.bottom_row_layout)

    def add_buttons(self, labels, group_label):
        group_label_widget = QLabel(group_label)
        group_label_widget.setAlignment(Qt.AlignCenter)
        self.button_bar_layout.addWidget(group_label_widget)
        for label in labels:
            button = QPushButton(label)
            self.button_bar_layout.addWidget(button)

    def setup_sliders_frame(self, labels, frame_label, slider_frame):
        slider_frame.setFixedSize(300, 200)  # Reduced size of the slider frame
        slider_layout = QVBoxLayout(slider_frame)
        slider_label = QLabel(frame_label)
        slider_label.setAlignment(Qt.AlignCenter)
        slider_layout.addWidget(slider_label)

        for label in labels:
            self.add_horizontal_sliders(label, slider_layout)

    def create_sliders_frame(self, labels, frame_label):
        slider_frame = QFrame()
        slider_frame.setFrameShape(QFrame.Box)
        slider_frame.setFixedWidth(300)  # Set a fixed width for the slider frame
        self.map_sliders_layout = QVBoxLayout(slider_frame) if frame_label == "Adjust Weights of Maps" else QVBoxLayout(
            slider_frame)
        slider_label = QLabel(frame_label)
        slider_label.setAlignment(Qt.AlignCenter)
        self.map_sliders_layout.addWidget(slider_label)

        for label in labels:
            self.add_horizontal_sliders(label, self.map_sliders_layout)

        return slider_frame

    def add_horizontal_sliders(self, label, container):
        slider_frame = QFrame()
        slider_layout = QHBoxLayout(slider_frame)
        slider_layout.setContentsMargins(5, 0, 5, 0)  # Reduced margins for compact layout
        slider_label = QLabel(label)
        slider_label.setAlignment(Qt.AlignCenter)
        slider_layout.addWidget(slider_label)

        slider = QSlider(Qt.Horizontal)
        slider.setMinimum(0)
        slider.setMaximum(100)
        slider.setValue(50)
        slider.setTickInterval(10)
        slider.setTickPosition(QSlider.TicksBelow)
        slider_layout.addWidget(slider)

        container.addWidget(slider_frame)


    def fill_inventory_table(self):
        inventory_data = {
            "White Matter Hyperintensities (WHM)": None,
            "Periventricular WMH (PVH)[In contact with the ventricles]": None,
            "PVH": "0 - 1 - 2 - 3",
            "Deep WMH [Between PVH and superficial WHM]": None,
            "Deep WMH": "0 - 1 - 2 - 3",
            "Superficial WMH [In Contact with U Fibers;]": None,
            "[Evaluate frontal and temporal pole white matter specifically,": None,
            "if different in the two locations, use the most severe one.]": None,
            "Superficial WMH": "0 - 1 - 2 - 3 - 4",
            "Lacunes": "0 - 1 - 2 - 3",
            "Cerebral Microbleeds (CMB)": "0 - 1 - 2 - 3",
            "Dilated perivascular spaces (dPVS)": None,
            "[Count in the slice with the highest number. T1 - sum of both sides,": None,
            "and T2 - the higher score on the other side.]": None,
            "Centrum semiovale (CSO)": "0 - 1 - 2",
            "Basal Ganglia": "0 -1 - 2",
            "Atrophy": None,
            "Superficial [Dilation of the Sulcus; Evaluate]": None,
            "sulcus and lateral sulcus specifically, if different  in": None,
            "the 2 locations, use the most severe one]": None,
            "Superficial": "0 - 1 - 2 - 3",
            "Deep [Dilation of the lateral ventricles]": "0 - 1 - 2 - 3",
            "Large Infarct": None,
            "(>20mm)": "0 - 1 - 2",
            "Macrobleeds": None,
            "(>15mm)": "0 - 1 - 2",
        }

        bold_font = QFont()
        bold_font.setBold(True)
        italic_font = QFont()
        italic_font.setItalic(True)

        for row, (label, response) in enumerate(inventory_data.items()):
            if response is None:  # Section title
                title_item = QTableWidgetItem(label)
                title_item.setFont(bold_font)  # Set font to bold
                title_item.setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)  # Left align and vertically center text
                self.inventory_table.setItem(row, 0, title_item)
                self.inventory_table.setSpan(row, 0, 1, 2)  # Span across two columns
            else:  # Regular item
                label_item = QTableWidgetItem(label)
                label_item.setFont(italic_font)
                response_item = QTableWidgetItem(response)
                label_item.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)  # Right align and vertically center text
                response_item.setTextAlignment(
                    Qt.AlignCenter | Qt.AlignVCenter)  # Center align and vertically center text
                self.inventory_table.setItem(row, 0, label_item)
                self.inventory_table.setItem(row, 1, response_item)
# Main loop

def main():
    app = QApplication(sys.argv)
    main_window = MRIAnomalyDetectionApp()
    main_window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
