from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from gui.utils import *
from datetime import *

class RunWindow(TableWindow):
    def add_to_table(self, run_table) :

        date = self.logdate_widget.selectedDate().toString("yyyy-MM-dd")
        date = datetime.strptime(date, "%Y-%m-%d")
        date = date.date()
        distance = self.distance.text()
        elavation = self.elavation_box.text()
        comment = self.comment_box.text()
        rating = self.rating_box.text()

        write_data = (date, float(distance), int(elavation), comment, float(rating))

        data_check = run_table.run_data_check(write_data)

        if data_check:
            run_table.write_to_table(write_data)
            self.tablelayout.addWidget(QLabel("added to database successfully"), 7, 0, 1, 2)

    def __init__(self, param_dict, run_table):
        super().__init__(param_dict)
        self.success_message = MessageWindow("success")

        #LOGDATE
        self.logdate_widget = QCalendarWidget()

        date_label = QLabel()
        date_label.setText("Date")
        self.tablelayout.addWidget(date_label, 1, 0)
        self.tablelayout.addWidget(self.logdate_widget, 1, 1)

        #DISTANCE
        distance_widget = QWidget()
        distance_sublayout = QHBoxLayout()

        self.distance = QLineEdit()
        self.distance.setValidator(QDoubleValidator())

        unit = QComboBox()
        unit.addItems(["km", "miles"])

        distance_sublayout.addWidget(self.distance, alignment=Qt.AlignCenter)
        distance_sublayout.addWidget(unit, alignment=Qt.AlignCenter)

        distance_widget.setLayout(distance_sublayout)

        distance_label = QLabel()
        distance_label.setText("Distance")

        self.tablelayout.addWidget(distance_label, 2, 0)
        self.tablelayout.addWidget(distance_widget, 2, 1)

        #ELAVATION
        elavation_widget = QWidget()
        elavation_sublayout = QHBoxLayout()

        self.elavation_box = QSpinBox()
        self.elavation_box.setMinimum(0)
        self.elavation_box.setMaximum(500)
        self.elavation_box.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Preferred)
        self.elavation_box.setMinimumSize(70, 10)

        unit_label = QLabel()
        unit_label.setText("metres")

        elavation_sublayout.addWidget(self.elavation_box, alignment=Qt.AlignCenter)
        elavation_sublayout.addWidget(unit_label, alignment=Qt.AlignCenter)

        elavation_widget.setLayout(elavation_sublayout)

        elavation_label = QLabel()
        elavation_label.setText("Elavation")

        self.tablelayout.addWidget(elavation_label, 3, 0)
        self.tablelayout.addWidget(elavation_widget, 3, 1)


        #COMMENTS
        self.comment_box = QLineEdit()
        self.comment_box.setMinimumSize(100, 50)
        comment_label = QLabel()
        comment_label.setText("Comments")

        self.tablelayout.addWidget(comment_label, 4, 0)
        self.tablelayout.addWidget(self.comment_box, 4, 1)


        #RATING
        rating_widget = QWidget()
        rating_sublayout = QHBoxLayout()

        self.rating_box = QDoubleSpinBox()
        self.rating_box.setDecimals(1)
        self.rating_box.setSingleStep(0.5)
        self.rating_box.setMinimum(0.0)
        self.rating_box.setMaximum(10.0)
        rating_label = QLabel()
        rating_label.setText("Rating")

        rating_sublayout.addWidget(self.rating_box, alignment=Qt.AlignCenter)
        rating_widget.setLayout(rating_sublayout)

        self.tablelayout.addWidget(rating_label, 5, 0)
        self.tablelayout.addWidget(rating_widget, 5, 1)

        #ADD
        add_button = QPushButton()
        add_button.setText("ADD")
        add_button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        add_button.toggle()
        add_button.clicked.connect(lambda : self.add_to_table(run_table))

        self.tablelayout.addWidget(add_button, 6, 0, 1, 2)

        self.tablewin.setLayout(self.tablelayout)
