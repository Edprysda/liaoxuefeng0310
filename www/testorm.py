'''
Author: Exarlos
Date: 2023-03-15 16:43:47
LastEditors: Exarlos
LastEditTime: 2023-03-15 16:46:57
Description: 世界上没有低级的法术,只有低级的法师!
'''

# 第四步：把下面这部分代码放在 python 里跑 （直接跑我这个 test_sql.py 也行）
import orm
import asyncio
from models import User, Blog, Comment
# 这部分源码来自 https://aodabo.tech/blog/001546713871394a2814d2c180b4e6f8d30c62a3eaf218a000


async def test(loop):                      # *** 注意此处的密码填自己设的密码 ***
    await orm.create_pool(loop=loop, user='root', password='747937aaA', db='moe')
    # *** 注意此处的密码填自己设的密码 ***
    u = User(name='Test', email='test@qq.com',
             passwd='1234567890', image='about:blank')
    await u.save()
    # 网友指出添加到数据库后需要关闭连接池，否则会报错 RuntimeError: Event loop is closed
    orm.__pool.close()
    await orm.__pool.wait_closed()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(test(loop))
    loop.close()

# 第五步：在 sql 命令行里输入 'SELECT * FROM users;'  然后回车（别漏了分号）
# 显示 test@qq.com 代表测试成功了
