import sys
from PySide6.QtWidgets import (QLineEdit, QPushButton, QApplication, QVBoxLayout, QDialog, QLabel, QMessageBox)

class Form(QDialog):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        self.setWindowTitle("My Form")
        # Create widgets
        self.label_first_name = QLabel("Write my first name here..")
        self.edit_first_name = QLineEdit()
        self.label_last_name = QLabel("Write my last name here..")
        self.edit_last_name = QLineEdit()
        self.button_ok = QPushButton("Ok")
        self.button_annuler = QPushButton("Annuler")

        # Create layout and add widgets
        layout = QVBoxLayout(self)
        layout.addWidget(self.label_first_name)
        layout.addWidget(self.edit_first_name)
        layout.addWidget(self.label_last_name)
        layout.addWidget(self.edit_last_name)
        layout.addWidget(self.button_ok)
        layout.addWidget(self.button_annuler)

        # Add button signal to greetings slot
        self.button_ok.clicked.connect(self.write_in_file)
        # Add button signal to clear slot
        self.button_annuler.clicked.connect(self.clear)

    # Greets the user
    def write_in_file(self):
        #print("Hello {} {}".format(self.edit_first_name.text(),self.edit_last_name.text()))
        # ne pas oublier de creer un txt !
        f = open(r"C:\Users\hdafa\Documents\Python Scripts\data_5055.txt","a")
        ready1 = ''.join(self.edit_first_name.text().split()).strip()
        ready2 = ''.join(self.edit_last_name.text().split()).strip()
        #ready1!='' and ready2!=''
        if not (ready1=='' or ready2=='') :
            #print(dir(self.edit_first_name))
            f.write("{},{}\n".format(self.edit_first_name.text(),self.edit_last_name.text()))
            self.edit_first_name.setText("")
            self.edit_last_name.setText("")
        else:
            # lancer un messag d'alert
            msgBox = QMessageBox()
            msgBox.setText("champs obligatoires non saisis!")
            msgBox.exec()
        

    def clear(self):
        print(dir(self.edit_first_name))


if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(sys.argv)
    # Create and show the form
    form = Form()
    # we can resize the form 
    form.resize(300,400)
    form.show()
    # Run the main Qt loop
    sys.exit(app.exec())
