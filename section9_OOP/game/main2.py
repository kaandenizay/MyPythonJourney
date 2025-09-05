from enemy import Enemy, Troll, Vampyre, VampyreKing

random_monster = Enemy("Basic enemy", 12, 1)
print(random_monster)

random_monster.take_damage(4)
print(random_monster)

random_monster.take_damage(8)
print(random_monster)

ugly_troll = Troll("Pug")
# So when we don't specify any arguments,the default values that we specified in enemy's init method are used.
print("Ugly troll - {} ".format(ugly_troll))
another_troll = Troll("Uggg")
print(another_troll)
another_troll.grunt()
another_troll.take_damage(4)
print(another_troll)


vamp = Vampyre("Vlad")
print(vamp)
vamp.take_damage(8)
print(vamp)

while vamp._alive:
    if not vamp.dodges():
        vamp.take_damage(2)
        print(vamp)


dracula = VampyreKing("Dracula")
print(dracula)
dracula.take_damage(8)
print(dracula)