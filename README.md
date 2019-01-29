

@[toc]
# Cookie


## #0 Blog


```
https://blog.csdn.net/Coxhuang/article/details/86696647
```

## #1 环境

```
Python3.6
Django==2.0.7
```

## #2 开始

### #2.1 存储

Cookie是将数据保存在用户的浏览器中,至于如何保存,不需要我们操作

### #2.2 设置

```
class get_data(APIView):

    def get(self,request): # 查看cookie

        ret = request.COOKIES.get('username')
        print(ret)

        return Response("success")

    def post(self,request): # 设置cookie

        res = Response("success")
        res.set_cookie("username", "cox") # 设置
        return res
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/20190129214335171.png)


```
res.set_cookie("age", "10",max_age=10) # 生命周期 10秒

res.set_cookie("age", "10",expires="2019-01-31") # 生命周期 时间(datetime)

rep.set_signed_cookie(key,value,salt,...)

# key:键
# value:值
# salt : 加密盐
# max_age=None,     超时时间
# expires=None,     超时时间(IE requires expires, so set it if hasn't been already.)
# path='/',         Cookie生效的路径，/ 表示根路径，特殊的：跟路径的cookie可以被任何url的页面访问
# domain=None,      Cookie生效的域名
# secure=False,     https传输
# httponly=False         只能http协议传输，无法被JavaScript获取（不是绝对，底层抓包可以获取到也可以被覆盖）

```

### #2.3 加密


```
res.set_signed_cookie("age", "10",salt="i am salt") # 加密的cookie , salt是盐值

request.get_signed_cookie('age',salt='i am salt') # 解密cookie, salt是盐值

```

**区别:**

- 设置cookie时,由原来的set_cookie 改成get_signed_cookie
- 获取cookie时,由原来的request.COOKIES.get('age') 改成request.get_signed_cookie('age',salt='i am salt')


## 3 session

```
https://blog.csdn.net/Coxhuang/article/details/86694441
```


