name = input('Enter Name: ')
eng = float(input('Enter marks in English: '))
math = float(input('Enter marks in maths: '))
sci = float(input('Enter marks in science: '))
sst = float(input('Enter marks in social: '))
hindi = float(input('Enter marks in hindi: '))
total = eng+math+sci+sst+hindi
per=total / 5
print('Report card for: ',name)
print('Total marks scored: ',total)
print('percentange Marks: ',per, '%')
if per>= 40:
    print('Congratulations !!!')
else:
    print('Sorry, Try again')
    
