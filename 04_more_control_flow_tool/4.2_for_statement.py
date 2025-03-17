'''
python ka for statement us sy thora different hai jo aap ne shayad dosri programming languages mein dekha ho.jesy C ya Pascal.
unmen for statement aik arithmatic progression ko iterate karta hai.jis men aapko manually iteration ki value deni parti hai.
python ka for statement sequence (list ya string) ko iterate karta hai.bina kisi manual iteration ki value denay ke.
'''

# for statement in different languages
# C
'''
for (i = 0; i < 10; i++) {
    printf("%d\n", i);
}

is men aapko manually iteration ki value deni parti hai.
jesy i = 0; i < 10; i++
'''

# Pascal
'''
for i := 1 to 10 do
    writeln(i);
'''

'''
lekin python ka for statement buhut smart ha aapko iteration ki value denay ki zaroorat nahi parti.
python ka for statement har sequence (string, tuple, list etc) type ko iterate kar sakta hai.
'''

# for statement in python
words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))
    
# agar aapko sequence ke index ki zaroorat hoti hai to aap range() aur len() functions ka istemal kar saktay hain.
for i in range(len(words)):
    print(i, words[i])

'''
jab ab kisi collection per loop chala rahy hain aur sath usko modify bhi kr rhy hen tu ya tricky hu skta ha aur unexpected results bhi de skta ha.
is liye behtar ha k aap collection ko copy kar k us per loop chalayen.
'''

# Example not good practice
numbers = [1, 2, 3, 4, 5]
for n in numbers:
    if n % 2 == 0:
        numbers.remove(n)
print(numbers)

'''
is example mein humne numbers list ko iterate kia aur agar number even tha tu usay remove kia.
lekin is ka result unexpected bhi hu skta hai. is liye behtar ha k aap collection ko copy kar k us per loop chalayen.

'''

# Better practice
numbers = [1, 2, 3, 4, 5]
for n in numbers.copy():
    if n % 2 == 0:
        numbers.remove(n)
print(numbers)

'''
is example mein humne numbers list ko iterate kia aur agar number even tha tu usay remove kia.
is baar humne numbers list ko copy kar k us per loop chalaya.
is se humne original list ko modify nahi kia aur expected result mila.
'''


# Example
# Suppose we have a dictionary of users and their status
# We want to
# 1. Remove inactive users
# 2. Create a new collection of active users
# 3. Do not modify the original collection

users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

# Strategy:  Iterate over a copy
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]

# Strategy:  Create a new collection
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status
