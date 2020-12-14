import hashlib

<<<<<<< HEAD
import json


def register(user,password):
    password = str(password)
    obj = hashlib.sha256()
    obj.update(password.encode())
    li=[user,obj.hexdigest()]
    with open('manager_info.json','r') as f:
        f=json.load(f)
    if li in f:
        print('yes')


register('parham','22561342Ps')
# hash_password_hack()
=======
from collections import OrderedDict




def hash_password_hack():
    d=OrderedDict()
    j=OrderedDict()
    y=OrderedDict()
    for i in ['22561342Ps','22122860','admin']:
        i=str(i)
        obj=hashlib.sha256()

        obj.update(i.encode())

        d[i]=d.get(i,obj.hexdigest())
    d =OrderedDict([(value, key) for key, value in d.items()])
    print(d)

hash_password_hack()
>>>>>>> 8280c89586c994151c7132887b855d83b0de1af3
