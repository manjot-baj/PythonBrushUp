a = "Manjot"
para = """ Hi, My name is Manjot """
para = ''' Hi, My name is Manjot. '''
print(len(a))
print(a[0], a[3])
print(len(para))
print(para[16], para[19])
print(para[para.find("Ma"):para.find(".")])
a = "Govardhan"
print(a[0:2],a[3:5:2])

a = "My \n Name \n is \n \' Manjot \' \n \t\t Thanks \n \\ bbb"

print(a)