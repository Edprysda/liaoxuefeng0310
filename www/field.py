'''
Author: Exarlos
Date: 2023-03-13 16:57:04
LastEditors: Exarlos
LastEditTime: 2023-03-14 08:58:31
Description: 世界上没有低级的法术,只有低级的法师!
'''


# 新建field类
# 定义Field类，它负责保存数据库表的字段名和字段类型：

class Field(object):
    def __init__(self, name, column_type, primary_key, default):
        self.name = name
        self.column_type = column_type
        self.primary_key = primary_key
        self.default = default

    def __str__(self):
        return '<%s, %s:%s>' % (self.__class__.__name__, self.column_type, self.name)

# 在Field的基础上，进一步定义各种类型的Field，比如StringField，IntegerField等等：


#  StringField的作用是保存varchar类型的字段
class StringField(Field):
    def __init__(self, name=None, primary_key=False, default=None, ddl='varchar(100)'):
        super().__init__(name, ddl, primary_key, default)


# BooleanField的作用是保存boolean类型的字段
class BooleanField(Field):
    def __init__(self, name=None, default=False):
        super().__init__(name, 'boolean', False, default)


# IntegerField的作用是保存bigint类型的字段
class IntegerField(Field):
    def __init__(self, name=None, primary_key=False, default=0):
        super().__init__(name, 'bigint', primary_key, default)


# - FloatField的作用是保存float类型的字段
class FloatField(Field):
    def __init__(self, name=None, primary_key=False, default=0):
        super().__init__(name, 'real', primary_key, default)


# TextField的作用是保存text类型的字段
class TextField(Field):
    def __init__(self, name=None, default=None):
        super().__init__(name, 'text', False, default)
