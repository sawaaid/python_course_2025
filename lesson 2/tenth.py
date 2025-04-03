camels = 42 
print('%d' % camels)

camels = 42 
print('In %d years I have spotted %g %s.' % (3, 0.1, 'camels') )

text = input("Enter text: ")
char_count = {}
for char in text:
    if text.count(char)>1:
        print('%s : %d' %(char,text.count(char)))
