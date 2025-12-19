from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import os
from models import initialize_database, Order, Product, Report, User
from peewee import fn
from flask import jsonify
from routes import blueprints

app = Flask(__name__)

# data フォルダ（JSON 保存用）
DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')
os.makedirs(DATA_DIR, exist_ok=True)

# データベースの初期化
initialize_database()

# 各Blueprintをアプリケーションに登録
for blueprint in blueprints:
    app.register_blueprint(blueprint)

# ホームページのルート
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload-json', methods=['POST'])
def upload_json():
    """アップロードされた JSON ファイルを data/<type>.json として保存する
    フォームには `file` と `type`(order|report) を含めること。
    """
    f = request.files.get('file')
    jsontype = request.form.get('type')
    if not f or jsontype not in ('order', 'report'):
        return redirect(url_for('index'))

    filename = f'{jsontype}.json'
    dest = os.path.join(DATA_DIR, filename)
    f.save(dest)
    return redirect(url_for('index'))


@app.route('/data/<path:filename>')
def serve_data(filename):
    """保存した JSON を返す（開発用）。存在しない場合は 404 を返す。"""
    return send_from_directory(DATA_DIR, filename)


@app.route('/api/order/product_counts')
def api_order_product_counts():
    """商品ごとの販売数量合計を返す JSON。
    形式: [{"product_id": 1, "product_name": "xxx", "count": 10}, ...]
    """
    try:
        q = (Product
             .select(Product.id.alias('product_id'), Product.name.alias('product_name'), fn.SUM(Order.quantity).alias('count'))
             .join(Order, on=(Order.product == Product.id))
             .group_by(Product.id))
        result = []
        for row in q.dicts():
            result.append({
                'product_id': row.get('product_id'),
                'product_name': row.get('product_name'),
                'count': int(row.get('count') or 0)
            })
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/report/monthly_json')
def api_report_monthly_json():
    """Report.get_monthly_sales_json を返すエンドポイント"""
    try:
        return jsonify(Report.get_monthly_sales_json())
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/user/age_distribution')
def api_user_age_distribution():
    """User.get_age_distribution を返すエンドポイント"""
    try:
        return jsonify(User.get_age_distribution())
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
