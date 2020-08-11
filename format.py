example_dict = {
    'float_number': 1324.321325493,
    'very_large_integer': 43890923148390284,
    'percentage': .324
}
string_print = 'float: {float_number:.4f}\n'
string_print += 'interger: {very_large_integer:,}\n'
string_print += 'percentage: {percentage:.2%}'
print(string_print.format(**example_dict))


data = ("John", "Doe", 53.44)
format_string = "Hello %s %s. Your current balance is $%s."
print(format_string % data)


name = "Jon"  
age = 28  
fave_food = "burritos"
fave_color = "green" 
gpa = 3.725
string = "Hey, I'm {0} and I'm {1} years old. I love {2} and my favorite color is {3}.".format(name, 
age, fave_food, fave_color)
print(string)

#(name, age, fave_food, fave_color, gpa)
print("Hey, I'm %s and I'm %s years old.\nI love %s and my favorite color is %s.\nMy gpa is %.2f" % (name, age, fave_food, fave_color, gpa))



print('{:.3f}'.format(3.1415926))
print('{:.1%}'.format(0.157))
print('{:,}'.format(2999334))


"""print a list with format"""
a = []
for i in range(1000):
    if i % 3 == 0:
       a.append(-i)
    elif i % 3 == 1:
        a.append(2*i)
    else:
         a.append(float(i/3))
# reverse the last 10 numbers
b = a[-10:][::-1]

print('\n'.join('{}: {:.2f}'.format(*k) for k in enumerate(b)))

for k in b:
    print('{:.2f}'.format(k))
