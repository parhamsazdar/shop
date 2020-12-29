# import io
# import json
# from pathlib import Path
#
# import openpyxl
# from werkzeug.utils import secure_filename
#
#
#
# #
# #
# # def return_category(filename):
# #     li = []
# #     with io.open(filename, encoding='utf-8') as f:
# #         f = json.load(f)
# #         category = f[0]
# #         for i in range(len(category['subcategories'])):
# #             cat2 = category['name']
# #             cat2 += r'/' + category['subcategories'][i]['name']
# #             for j in range(len(category['subcategories'][0]['subcategoreis'])):
# #                 cat3 = cat2
# #                 cat3 += r'/' + category['subcategories'][i]['subcategoreis'][j]['name']
# #                 li.append(cat3)
# #                 cat3 = cat2
# #     return li
# #
# #
# # def check_validation_exel():
# #     xlsx_file = Path(r'C:\Users\ASUS\Desktop\justfortest.xlsx')
# #     wb_obj = openpyxl.load_workbook(xlsx_file)
# #     sheet = wb_obj.active
# #     # print(sheet.iter_rows())
# #     category=set()
# #     for row in sheet.iter_rows(max_row=sheet.max_row):
# #         category.add(row[-2].value)
# #     for cat in category:
# #         if cat in return_category(r'category.json'):
# #             print(cat)
# #         # for cell in row:
# #         #     print(cell.value, end="/")
# #         # print()
# #
# #
# # # check_validation_exel()
# #
# # # print(return_category(r'category.json'))
# #
# # def check_validation_excel(path):
# #     category=[]
# #     xlsx_file = Path(path)
# #     wb_obj = openpyxl.load_workbook(xlsx_file)
# #     sheet = wb_obj.active
# #     for row in sheet.iter_rows(max_row=sheet.max_row):
# #         if row[-2].value not in return_category(r'category.json'):
# #             raise Exception('your category is wrong')
# #         else:
# #             category.append({
# #                 'name_product':row[-1].value,
# #                 'category':row[-2].value,
# #                 'descrption':row[-3].value,
# #                 'url_image':row[-4].value
# #             })
# #     return category
#
# # print(check_validation_excel(r'C:\Users\ASUS\Desktop\justfortest.xlsx'))
# from numpy import array
# from numpy.linalg import inv
# sx=2
# sy=13.1
# x2=1.2
# xy=6.84
# a=array([[5,sx],[sx,x2]])
# a=inv(a)
# b=array([[sy,xy]])
# print(b@a)
import io
import json

from datetime import datetime

from bson import ObjectId
from pymongo import MongoClient

# def return_category(filename):
#     li = []
#     with io.open(filename, encoding='utf-8') as f:
#         f = json.load(f)
#         category = f[0]
#         for i in range(len(category['subcategories'])):
#             cat2 = category['name']
#             cat2 += r'/' + category['subcategories'][i]['name']
#             for j in range(len(category['subcategories'][0]['subcategoreis'])):
#                 cat3 = cat2
#                 cat3 += r'/' + category['subcategories'][i]['subcategoreis'][j]['name']
#                 li.append(cat3)
#                 cat3 = cat2
#     return li

# print(return_category(r'category.json'))

# client = MongoClient('localhost', 27017)
# db = client.online_shop
# res = db.inventory.update_many({"_id": ObjectId('5fe81d7cc82e151f344df4a8'), "items.name_product": "shaiami"},
#                                {"$inc": {"items.$.quantity": 1000}, "$set": {"items.$.price": 17,"items.$.date_insert":datetime.now()}})
# print(res.modified_count)


b={2:1}

a={1:2}
a.update({2:2})
print(a)