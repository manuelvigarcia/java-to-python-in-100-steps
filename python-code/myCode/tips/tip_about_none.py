print(None)
print(type(None))

def email(subject, content, to, cc, bcc):
    print(f'{subject}, {content}, {to}, {cc}, {bcc}')

#email("subject","great work", 'info@nowhere.com') #compiler error: missing required positional arguments

def email2(subject, content, to, cc=None, bcc=None):
    print(f'{subject}, {content}, {to}, {cc}, {bcc}')


email2("subject","great work", 'info@nowhere.com')
email2(None, 'great work', 'info@nowhere.com', None,None)

var =('123')
if var is None: print('do something')