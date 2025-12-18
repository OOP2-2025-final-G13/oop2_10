from datetime import datetime, date
import json
from peewee import fn
from .order import Order
from .product import Product


class Report:
    @staticmethod
    def get_total_sales():
        """全期間の総売上を取得"""
        try:
            query = (Order
                    .select(fn.SUM(Product.price * Order.quantity.cast('decimal')).alias('total'))
                    .join(Product)
                    .scalar())
            return float(query) if query else 0
        except:
            return 0
    
    @staticmethod
    def get_monthly_sales(year=None, month=None):
        """指定された月の売上を取得（デフォルトは当月）"""
        if year is None or month is None:
            today = date.today()
            year = today.year
            month = today.month
        
        start_date = datetime(year, month, 1)
        if month == 12:
            end_date = datetime(year + 1, 1, 1)
        else:
            end_date = datetime(year, month + 1, 1)
        
        try:
            query = (Order
                    .select(fn.SUM(Product.price * Order.quantity.cast('decimal')).alias('monthly_total'))
                    .join(Product)
                    .where(Order.order_date.between(start_date, end_date))
                    .scalar())
            return float(query) if query else 0
        except:
            return 0
    
    @staticmethod
    def get_monthly_sales_data():
        """月別売上データを取得（過去12ヶ月分）"""
        monthly_data = []
        today = date.today()
        
        for i in range(12):
            if today.month - i > 0:
                year = today.year
                month = today.month - i
            else:
                year = today.year - 1
                month = 12 + (today.month - i)
            
            sales = Report.get_monthly_sales(year, month)
            monthly_data.append({
                'year': year,
                'month': month,
                'sales': sales
            })
        
        return monthly_data[::-1]  # 古い順に並び替え
    
    @staticmethod
    def get_monthly_sales_json():
        """月別売上データをJSON形式で取得（グラフ用）"""
        monthly_data = Report.get_monthly_sales_data()
        
        # グラフ用のデータ形式に変換
        chart_data = {
            "title": "月別売上推移",
            "x_axis_label": "購入月",
            "y_axis_label": "売上（円）",
            "data": []
        }
        
        for data in monthly_data:
            chart_data["data"].append({
                "month": f"{data['year']}年{data['month']}月",
                "sales": data['sales']
            })
        
        return chart_data
    
    @staticmethod
    def export_monthly_sales_json(file_path='monthly_sales_chart.json'):
        """月別売上データをJSONファイルとしてエクスポート"""
        chart_data = Report.get_monthly_sales_json()
        
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(chart_data, f, ensure_ascii=False, indent=2)
            return True, f"データを {file_path} に出力しました"
        except Exception as e:
            return False, f"エラーが発生しました: {str(e)}"