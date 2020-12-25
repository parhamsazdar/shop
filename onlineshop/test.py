import io
from json import load, loads

with io.open(r'category.json', encoding='utf-8') as f:
    f = load(f)
    print(f)

category = f[0]

cat = category['name'] + r'/' + category['subcategories'][0]['name'] + r'/' + \
      category['subcategories'][0]['subcategoreis'][0]['name']
print(category['subcategories'][0]['subcategoreis'])

print(cat)
li=[]
category=f[0]

for i in range(len(category['subcategories'])):
    cat2 = category['name']
    cat2+=r'/'+category['subcategories'][i]['name']
    for j in range(len(category['subcategories'][0]['subcategoreis'])):
        cat3=cat2
        cat3+= r'/'+category['subcategories'][i]['subcategoreis'][j]['name']
        li.append(cat3)
        cat3=cat2
#
print(li)


# def return_category(filename):
#     li = []
#     with io.open(filename, encoding='utf-8') as f:
#         f = load(f)
#         category = f[0]
#         for i in range(len(category['subcategories'])):
#             cat2 = category['name']
#             cat2 += r'/' + category['subcategories'][i]['name']
#             for j in range(len(category['subcategories'][0]['subcategoreis'])):
#                 cat2 += r'/' + category['subcategories'][i]['subcategoreis'][j]['name']
#                 li.append(cat2)
#     return li


# print(return_category(r'category.json'))

# for i in category['subcategoreis']:
#     cat+=i[name]


# for i in f[0]
#     cat=''
#     if type(f[0][i]) is not list:
#         cat+=f[0][i]+r'/'
#     else:
#         for j in f[0][i]:
#             if type(f[0][i][j]) is not list:
#                 cat += f[0][i][j] + r'/'
#             else:
#                 for z in f[0][i][j]:
#                     cat += f[0][i][j][z] + r'/'
#
#     print(cat)
