import re

def name_of_email(addr):
    str_w_name = r'<([a-zA-Z]+\s+[a-zA-Z]+)>\s+[a-zA-Z]+@([a-zA-Z]+\.[a-zA-Z]+)' 
    str_wo_name = r'([a-zA-Z]+)@([a-zA-Z]+\.[a-zA-Z]+)' 
    if re.match(str_w_name, addr):
        return re.match(str_w_name, addr).group(1)
    elif re.match(str_wo_name, addr):
        return re.match(str_wo_name, addr).group(1)
    else:
        return None

 
# 测试:
assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
assert name_of_email('tom@voyager.org') == 'tom'
print('ok')
