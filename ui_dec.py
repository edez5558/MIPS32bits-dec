import sys
from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtq
import PySide6.QtGui
import decoder as dec
from code_editor import CodeEditor

from ui.texteditor import Ui_MainWindow

import re

#Comment
class Highlighter(qtq.QSyntaxHighlighter):
    def __init__(self, parent=None):
        qtq.QSyntaxHighlighter.__init__(self, parent)

        self._mappings = {}
    

    def add_mapping(self, pattern, format):
        self._mappings[pattern] = format

    def highlightBlock(self, text):
        for pattern, format in self._mappings.items():
            for match in re.finditer(pattern, text):
                start, end = match.span()
                self.setFormat(start, end - start, format)



class EditorWindow(qtw.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.textEdit = CodeEditor()
        self.codeText = qtw.QPlainTextEdit()

        self.splitter = qtw.QSplitter()
        self.splitter.addWidget(self.textEdit)
        self.splitter.addWidget(self.codeText)

        self.mainPanel.layout().addWidget(self.splitter)

        self.setStyleSheet(''' 
        QWidget{
            background-color: #282d35;
            color: #9ca4b4;
        }

        QMenuBar::item:selected{
            color: #000000;
        }

        ''');

        self.highlighter = Highlighter()
        self.syntax_highlighter()

        self.setWindowTitle("Untitled")
        self.current_path = None
        self.current_bin  = None

        self.textEdit.installEventFilter(self)

        self.codeText.setReadOnly(True)
        self.errorText.setReadOnly(True)

        self.lastBlock = self.textEdit.textCursor().block().text()
        self.currentRow = self.textEdit.textCursor().blockNumber()

        self.actionNew.triggered.connect(self.new_file)
        self.actionOpen.triggered.connect(self.open_file)
        self.actionSave.triggered.connect(self.save_file)
        self.actionSave_as.triggered.connect(self.save_file_as)

        self.actionSave_2.triggered.connect(self.save_bin)
        self.actionSave_as_2.triggered.connect(self.save_bin_as)

        self.actionDecode.triggered.connect(self.decoding)

        self.decoder = dec.Decoder(self.show_errors)
    
    
    def show_errors(self,errors : []):
        if not errors:
            self.errorText.clear()
            return

        self.errorText.document().setPlainText("\n".join( error for error in errors))
    
    def decoding(self):
        self.codeText.document().setPlainText(self.decoder.text_to_binary(self.textEdit.toPlainText()))
    
    def new_file(self):
        self.textEdit.clear()
        self.codeText.clear()
        self.setWindowTitle("Untitled")
        self.current_path = None
    
    def save_file_as(self):
        pathname = qtw.QFileDialog.getSaveFileName(self, 'Save file',filter='Text files (*.asm)')
        with open(pathname[0],'w') as f:
            f.write(self.textEdit.toPlainText())
        
        self.current_path = pathname[0]
        self.setWindowTitle(pathname[0])
        
        self.decoding()
    
    def save_file(self):
        if self.current_path is not None:
            filetext = self.textEdit.toPlainText()
            with open(self.current_path, 'w') as f:
                f.write(filetext)
            self.decoding()
        else:
            self.save_file_as()

    def save_bin_as(self):
        pathname = qtw.QFileDialog.getSaveFileName(self, 'Save output file',filter='Text files (*.txt)')

        with open(pathname[0],'w') as f:
            f.write(self.codeText.toPlainText())
        
        self.current_bin = pathname[0]
    
    def save_bin(self):
        if self.current_bin is not None:
            filetext = self.codeText.toPlainText()
            with open(self.current_bin, 'w') as f:
                f.write(filetext)
        else:
            self.save_bin_as()
        
    
    def open_file(self):
        fname = qtw.QFileDialog.getOpenFileName(self, 'Open file', filter= 'Text files (*.asm)')

        self.setWindowTitle(fname[0])

        with open(fname[0],'r') as f:
            file_read = f.read()
            self.textEdit.document().setPlainText(file_read)
            self.decoding()

        self.current_path = fname[0]


    def syntax_highlighter(self):
        self.textEdit.setStyleSheet("background-color: #282d35; color: #bababb; font-weight: bold")
        self.codeText.setStyleSheet("background-color: #282d35; color: #676f7d; font-weight: bold")
        self.errorText.setStyleSheet("background-color: #282d35; color: #e16c74; font-weight: bold")

        self.textEdit.font = qtq.QFont("Monospace")
        self.codeText.font = qtq.QFont("Monospace")
        self.textEdit.font.setStyleHint(qtq.QFont.TypeWriter)


        instruction_format = qtq.QTextCharFormat()
        instruction_format.setFontWeight(qtq.QFont.Bold)
        instruction_format.setForeground(qtq.QColor('#56b7c3'))
        pattern = r'^\s*\w+\s'
        self.highlighter.add_mapping(pattern,instruction_format)

        register_format = qtq.QTextCharFormat()
        register_format.setFontWeight(qtq.QFont.Bold)
        register_format.setForeground(qtq.QColor('#98c278'))
        pattern = r'\$\d+'
        self.highlighter.add_mapping(pattern,register_format)

        comment_format = qtq.QTextCharFormat()
        comment_format.setFontWeight(qtq.QFont.Bold)
        comment_format.setForeground(qtq.QColor('#676f7d'))
        pattern = r';.*$'
        self.highlighter.add_mapping(pattern,comment_format)

        immediate_format = qtq.QTextCharFormat()
        immediate_format.setFontWeight(qtq.QFont.Bold)
        immediate_format.setForeground(qtq.QColor('#d19a66'))
        pattern = r'(,|\s+)(\d|#|\+|-)\d*'
        self.highlighter.add_mapping(pattern,immediate_format)

        def_label_format = qtq.QTextCharFormat()
        def_label_format.setFontWeight(qtq.QFont.Bold)
        def_label_format.setForeground(qtq.QColor('#e16d75'))
        pattern = r'\w+:'
        self.highlighter.add_mapping(pattern,def_label_format)

        label_format  = qtq.QTextCharFormat()
        label_format.setFontWeight(qtq.QFont.Bold)
        label_format.setForeground(qtq.QColor('#d19a66'))
        pattern = r'[a-zA-Z]\w*\s*$'
        self.highlighter.add_mapping(pattern,label_format)

        self.highlighter.setDocument(self.textEdit.document())
        


if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)

    window = EditorWindow()
    window.show()

    sys.exit(app.exec())