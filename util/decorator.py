# 装饰器方法

def printResponse(response):
    def decorator(func):
        def infunc(*args, **kwargs):
            print(*args, **kwargs)

            return func(*args, **kwargs)

        # 打印接口返回数据
        if response != None:
            print(response)

        return infunc

    return decorator


@printResponse('123')
def test():
    print('test==')


if __name__ == '__main__':
    test()
