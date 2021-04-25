def get_mode_connect(name, suffix,signal,args,note):
    connect=f'''def {signal}_{suffix}(self{args}):
    #{note}
    print('{signal}'{args})'''

    bound=f'''#如果需要传参数可以使用functools库\nself.{name}.{signal}.connect(self.{signal}_{suffix})'''
    return connect,bound