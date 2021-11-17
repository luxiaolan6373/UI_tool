def get_mode_connect(name,signal):
    connect=f'''def {signal['name']}_{name}(self):
    #{signal['text']}
    #{signal['note']}
    print('{signal['text']}')'''

    bound=f'''#如果需要传参数可以使用functools库\nself.{name}.{signal['name']}.connect(self.{signal['name']}_{name})'''
    return connect,bound
def get_mode_qevent(name,signal):
    connect=f'''def {signal['name']}_{name}(self):
    #{signal['text']}
    #{signal['note']}
    print('{signal['text']}')'''

    bound=f'''#如果需要传参数可以使用functools库\nself.{name}.{signal['name']}=self.{signal['name']}_{name}'''
    return connect,bound