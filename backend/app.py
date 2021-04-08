#!flask/bin/python
from flask import Flask, jsonify
from flask import abort
import sys
sys.path.append('./jieba/')
import jieba
# from jieba.test.extract_tags_with_weight import get_tag_with_weight
app = Flask(__name__)


@app.route('/')
def index():
    return "Hello, Flask!"


@app.route('/api/TFIDF/<string:content>', methods=['GET'])
def get_task(content, topK=3):
    # tags = get_tag_with_weight(content, withWeight=True, topK=topK)
    tags = jieba.analyse.extract_tags(content, topK=topK, withWeight=True)
    if len(content) == 0:
        abort(404)
    return jsonify({'data': tags, 'code': 1, 'msg': 'OK'})


if __name__ == '__main__':
    app.run(debug=True)