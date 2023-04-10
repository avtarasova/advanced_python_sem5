"""
Веб-приложение. Сайт-визитка с возможностью разделения pdf-файла
"""
from os import remove
from flask import Flask, render_template, request, send_file
import pdfsplitter


app = Flask(__name__)  # Создание приложения


@app.route("/more")
def more() -> str:
    """
    Рендеринг страницы "more"
    :return:
    """
    return render_template('more.html')


@app.route('/')
def index() -> str:
    """
    Рендеринг главной страницы
    :return:
    """
    return render_template('index.html')


@app.route("/upload")
def upload() -> str:
    """
    Рендеринг страницы загрузки файлов для разделения
    :return:
    """
    return render_template("file_upload.html")


@app.route("/success", methods=["POST"])
def success() -> str:
    """
    Вызов функции деления файла + Рендеринг страницы,
    на которой можно скачать разделенный файл,
    ЛИБО рендеринг страницы "Попробуйте снова",
    если загруженный файл имеет неправильное разрешение (не pdf)
    :return:
    """
    file = request.files['file']
    file_name = file.filename
    if file_name[-4:] == '.pdf':
        file.save(file_name)
        pdfsplitter.cropper(file_name)
        remove(file_name)
        return render_template("success.html")
    return render_template("try_again.html")


@app.route("/download")
def download():
    """
    Загрузка разделенного файла на компьютер пользователя
    :return:
    """
    return send_file('cropped_pdf.zip', as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)
