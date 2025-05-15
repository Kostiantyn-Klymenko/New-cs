
from cats import Cat

c1 = Cat("Tom", 5, "happy")
c2 = Cat("Jerry", 3, "playful")


print(c1.tell_what_cat_doing())
print(c1.change_status("sad"))
print(c1.tell_what_cat_doing())

c2.change_status("angry")
print(c2.tell_what_cat_doing())
