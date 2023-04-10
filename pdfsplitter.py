"""
Функция разделения pdf-файла и записи отдельных страниц в zip-архив
"""
from os import remove
from zipfile import ZipFile
from PyPDF2 import PdfWriter, PdfReader


def cropper(file: str) -> None:
    """
    Функция разделения pdf-файла и записи отдельных страниц в zip-архив
    :param file: название файла, который нужно разделить
    :return:
    """
    input_pdf = PdfReader(open(file, "rb"))
    with ZipFile('cropped_pdf.zip', 'w') as zip_object:
        for i, page in enumerate(input_pdf.pages):
            out_pdf = PdfWriter()
            name = file.split(".")[0] + f"_{i}.pdf"
            with open(name, "wb") as myf:
                out_pdf.add_page(page)
                out_pdf.write(myf)
            zip_object.write(name)
            remove(name)
