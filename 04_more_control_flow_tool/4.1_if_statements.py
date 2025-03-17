# perhaps the most well-known statement type is the if statement. For example:

x = int(input("Please enter an integer: "))
if x < 0:
    x = 0
    print("Negative changed to zero")
elif x == 0:
    print("Zero")
elif x == 1:
    print("Single")
else:
    print("More")
    
'''Python mein if-elif-else ka istemal switch-case statements ka alternative hai jo dusray programming languages mein hotay hain.
Agar aap aik value ko multiple constants se compare kar rahe hain ya kisi specific type ya attribute ko check kar rahe hain, to match statement bhi istemal ho sakti hai.'''