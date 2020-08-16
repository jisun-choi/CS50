#정규 표현식
import re
s = input('Do you agree?')

if re.search('^y(es)?$', s, re.IGNORECASE):
    print('Agreed.')
elif re.search('^n(o)?$', s):
    print('Not agreed.')