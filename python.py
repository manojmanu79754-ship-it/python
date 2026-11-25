'''import keyword
print(keyword.kwlist)

a = None
print(a)

a = True
print(a)

a = 0.222
print(bool(a))'''

'''a = [10, 2.5, True,'hello']
print(a[3][-1])'''

'''a = [10, 2.5, True,'hello']
a.append(100)
print(a)'''

'''a = (10)
print(a,type(a))'''

'''a = (10, 20, 30)
print(a,type(a))'''

'''a = {'a': 10, 'b': 20}
print(a)'''

'''a = {'a': 10, 'b': 20}
a['c'] = 30
print(a)'''

'''a = {'a':[10, 20, 30], 'b': 40}
print(a['a'][1])'''

'''a = 'Hello'
print(a[2:3+1:1])'''

'''a = 'manjunath'
print(a[1:4+1:2])'''

'''a = 'Good Morning'
print(a[7:10+1:1])'''

'''a = 'Good Morning'
print(a[-5:-2+1:1])'''

'''a = 'Hello'
print(a[3:1-1:-1])'''

'''a = 'Hello'
print(a[-2:-4-1:-1])'''

'''a = 'Hello'
print(a[::-1])'''

'''a = 'Good Morning'
print(a[5::3])
print(a[-7::3])'''

'''a = int(input('Enter a number: '))
print(a,type(a))'''

'''a = list(input('Enter a number: '))
print(a,type(a))'''

'''a = eval(input('Enter: '))
print(a,type(a))'''

'''a  = int(input('Enter a number: '))
if a%2 == 0:
    print('Even')
else:
    print('Odd')'''

'''a = eval(input('Enter a number: '))
if len(str(a))== 5:
    print('five digit')
else:
    print('not five digit')'''


'''print(ord('a'))
print(ord('A'))
print(chr(97))
print(chr(65))
print(ord('a')-ord('A'))'''

'''ch = input('Enter a character: ')
if 'A' <= ch <= 'Z':
    print('Uppercase')
elif 'a' <= ch <= 'z':
    print('Lowercase')
else:
    print('Not an alphabet')'''

'''un= input("Enter:")
if un == "itz_me_manu_jogie_88":
    pw = input("Enter password:")
    if pw == "manu@123":
        print("Login successful")
    else:
        print("Incorrect password")
else:
    print("Incorrect username")'''

'''i = 1
while i <= 100:
    print(i)
    i += 1'''

'''i = 1
while i <= 50:
    if i%2 == 0:
        print(i)
    i += 1  ''' 

'''i = 2
while i <= 50:
    print(i)
    i += 2  '''

'''i = 1
while i <= 50:
    if i%2 != 0:
        print(i)
    i += 1'''

'''n = int(input('Enter a number: '))
rev = 0
while n > 0:
    ld = n % 10
    n = n // 10
    rev = rev * 10 + ld
print(rev)'''

'''for i in range(1, 100):
    print(i)'''

'''for i in range(1, 100):
    if i%2 == 0:
        print(i,"even")'''

'''a = [10, 20, 30, 40, 50]
for i in a:
    print(i)'''

'''s = input('Enter a string: ')
for i in s:
    if 'A' <= i <= 'Z':
        print(i, 'Uppercase')
    elif 'a' <= i <= 'z':
        print(i, 'Lowercase')
    else:
        print(i, 'Not an alphabet')'''

'''s = input('Enter a string: ')
out = ''
for i in s:
    if 'A' <= i <= 'Z':
        out += chr(ord(i) + 32)
    elif 'a' <= i <= 'z':
        out += chr(ord(i) - 32)
    else:
        out += i
print(out)'''

'''s = input('Enter a string: ')
rev = ''
for i in s:
    rev = i + rev
print(rev)'''

'''for i in range(1, 6):
    for j in range(1, 6):
        print("*", end = ' ')
    print()'''

'''for i in range(1, 6):
    for j in range(1, 6):
        if i == j:
            print('1', end = ' ')
        else:
            print('@', end = ' ')
    print()'''

#With arg and without return
'''def convert(s):
    out  = ''
    for i in s:
        if 'a' <= i <= 'z':
            out += chr(ord(i) - 32)
        else:
            out += i
    return out
print(convert(input('Enter a string: ')))'''

'''def convert():
    s = input('Enter a string: ')
    out  = ''
    for i in s:
        if 'a' <= i <= 'z':
            out += chr(ord(i) - 32)
        else:
            out += i
    return out
print(convert())'''


'''class college:
    cname = 'GCEM'
    cloc = 'Hoodi'
s1 = college()
print(s1.cname, s1.cloc)

college.cname = 'GCET'
print(s1.cname)
print(college.cname)

print('changing college location')
s1.cloc = 'Hoodi, Bangalore'
print(s1.cloc)
print(college.cloc)'''


'''class college:
    cname = 'GCEM'
    cloc = 'Hoodi'
s1 = college()

s1.name = 'Manoj S'
s1.phone = 1234567890

s2 = college()
s2.name = 'Manjunath'
s2.phone = 9876543210

print(s1.name)
print('After changing college name')
s1.name = 'GCET'
print(s1.name)'''


class college:
    @classmethod
    def display(cls):
        print('College Name:', cls.cname)
        print('College Location:', cls.cloc)
    def __init__(self, name, phone, usn):
        self.name = name
        self.phone = phone
        self.usn = usn

    def display(self):
        print('Name:', self.name)
        print('Phone:', self.phone)
        print('USN:', self.usn)

    def change_name(self, name):
        self.name = name
    def change_phone(self, phone):
        self.phone = phone
    def change_usn(self, usn):
        self.usn = usn

s1 = college('Manoj S', 1234567890, '1GC20CS001')
s2 = college('Manjunath', 9876543210, '1GC20CS002')
s1.display()
s2.display()

s1.change_name('Manoj')
s1.change_phone(9786756798)
s1.change_usn('1GC20CS003')
s1.display()

s2.change_name('Manjunath B')
s2.change_phone(9876543210)
s2.change_usn('1GC20CS004')
s2.display()



