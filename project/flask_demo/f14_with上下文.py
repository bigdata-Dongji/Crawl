class Fun():
    # 进入Fun这个类时被调用
    def __enter__(self):
        print('Fun Entered!')

    # 离开Fun这个类的时候被调用
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Exit:')
        print(f'exc_type:{exc_type}') # 异常类型
        print(f'exc_val:{exc_val}') # 异常值
        print(f'exc_tb:{exc_tb}') # 异常追踪信息

# with会帮我们调用enter和exit方法

with Fun() as fun:
    print('hello world!')