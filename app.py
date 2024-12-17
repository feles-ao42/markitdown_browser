from flask import Flask, request, render_template, send_file
from markitdown import MarkItDown
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max-limit

# アップロードを許可する拡張子
ALLOWED_EXTENSIONS = {
    'pdf', 'docx', 'xlsx', 'pptx', 'jpg', 'jpeg', 'png', 
    'html', 'txt', 'csv', 'json', 'xml'
}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return 'ファイルがありません'
        
        file = request.files['file']
        if file.filename == '':
            return 'ファイルが選択されていません'
            
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            
            # アップロードフォルダがない場合は作成
            os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
            
            file.save(filepath)
            
            # MarkItDownでファイル変換
            markitdown = MarkItDown()
            result = markitdown.convert(filepath)
            
            # 変換結果を一時ファイルとして保存
            output_path = os.path.join(app.config['UPLOAD_FOLDER'], 
                                     f'converted_{filename}.md')
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(result.text_content)
            
            # 変換したファイルをダウンロード
            return send_file(output_path,
                           as_attachment=True,
                           download_name=f'converted_{filename}.md')
            
    return render_template('upload.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

