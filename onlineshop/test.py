# # import io
# # import json
# # from pathlib import Path
# #
# # import openpyxl
# # from werkzeug.utils import secure_filename
# #
# #
# #
# # #
# # #
# # # def return_category(filename):
# # #     li = []
# # #     with io.open(filename, encoding='utf-8') as f:
# # #         f = json.load(f)
# # #         category = f[0]
# # #         for i in range(len(category['subcategories'])):
# # #             cat2 = category['name']
# # #             cat2 += r'/' + category['subcategories'][i]['name']
# # #             for j in range(len(category['subcategories'][0]['subcategoreis'])):
# # #                 cat3 = cat2
# # #                 cat3 += r'/' + category['subcategories'][i]['subcategoreis'][j]['name']
# # #                 li.append(cat3)
# # #                 cat3 = cat2
# # #     return li
# # #
# # #
# # # def check_validation_exel():
# # #     xlsx_file = Path(r'C:\Users\ASUS\Desktop\justfortest.xlsx')
# # #     wb_obj = openpyxl.load_workbook(xlsx_file)
# # #     sheet = wb_obj.active
# # #     # print(sheet.iter_rows())
# # #     category=set()
# # #     for row in sheet.iter_rows(max_row=sheet.max_row):
# # #         category.add(row[-2].value)
# # #     for cat in category:
# # #         if cat in return_category(r'category.json'):
# # #             print(cat)
# # #         # for cell in row:
# # #         #     print(cell.value, end="/")
# # #         # print()
# # #
# # #
# # # # check_validation_exel()
# # #
# # # # print(return_category(r'category.json'))
# # #
# # # def check_validation_excel(path):
# # #     category=[]
# # #     xlsx_file = Path(path)
# # #     wb_obj = openpyxl.load_workbook(xlsx_file)
# # #     sheet = wb_obj.active
# # #     for row in sheet.iter_rows(max_row=sheet.max_row):
# # #         if row[-2].value not in return_category(r'category.json'):
# # #             raise Exception('your category is wrong')
# # #         else:
# # #             category.append({
# # #                 'name_product':row[-1].value,
# # #                 'category':row[-2].value,
# # #                 'descrption':row[-3].value,
# # #                 'url_image':row[-4].value
# # #             })
# # #     return category
# #
# # # print(check_validation_excel(r'C:\Users\ASUS\Desktop\justfortest.xlsx'))
# # from numpy import array
# # from numpy.linalg import inv
# # sx=2
# # sy=13.1
# # x2=1.2
# # xy=6.84
# # a=array([[5,sx],[sx,x2]])
# # a=inv(a)
# # b=array([[sy,xy]])
# # print(b@a)
# import io
# import json
#
# from datetime import datetime
# import datetime
# from bson import ObjectId
# <<<<<<< HEAD
# =======
# from flask import session
# >>>>>>> 507abe23b5614082b0284863b387328d301cb070
# from pymongo import MongoClient
# from persiantools.jdatetime import JalaliDateTime, JalaliDate
# from persiantools import characters, digits
#
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
#
# # print(return_category(r'category.json'))
#
# client = MongoClient('localhost', 27017)
# db = client.online_shop
# <<<<<<< HEAD
# res = list(db.basket.find())
#
# for i in res:
#     i["time_record"] = digits.en_to_fa(JalaliDate((JalaliDateTime.to_jalali(i["time_record"]))).strftime("%Y/%m/%d"))
#
#     # print(digits.en_to_fa(i["time_record"]))
#     print(i["time_record"])
#     # i["time_record"]=JalaliDate(i["time_record"]).strftime("%Y/%m/%d")
#     # print(i["time_record"])
# # b={2:1}
# #
# # a={1:2}
# # a.update({2:2})
# # print(a)
# =======
# # res = list(db.inventory.aggregate(
# #     [{"$unwind": {"path": "$items"}}, {"$match": {"items.name_product": "Lg"}}, {"$sort": {"items.price": 1}},
# #      {"$limit": 1}]))
# # print(res)
# #
# # li=[{"name_product": "Lg", "quantity": 3}, {"name_product": "Apple", "quantity": 3}]
# # # li=list(filter(lambda x:del x if x['name_product']=="Lg",li))
# # li=list(filter(lambda x:x["name_product"]!="Lg",li))
# #
# # print(li)
#
# # li=[i for i in li if i["name_product"]!="Lg"]
# # print(li)
# # li=list(map(lambda x:li.remove(x),filter(lambda x:x["name_product"]=="Lg",li)))
# # print(li)
# # import datetime
# # a='2011-09-09T13:45'
# # # print(datetime.datetime(2011,09,09))
# # a=datetime.datetime.fromisoformat(a)
# # print(type(a))
#
# a='ali'
# if a.startswith('ali'):
#     print(2)
#
