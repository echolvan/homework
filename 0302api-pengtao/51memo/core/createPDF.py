import PyPDF2
import os


def create_output_file():
    base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.mkdir(base_path + r'\output')


def createPDF(data_file_path):
    data_path = os.path.dirname(data_file_path)                      # 数据文件目录
    pdf_name = (os.path.splitext(data_file_path)[0]).split(os.path.sep)[-1] + '.\
    pdf'
    pdf_write = PyPDF2.PdfFileWriter()
    with open(pdf_name, 'wb') as f:
        pass