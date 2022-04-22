from dataclasses import field, dataclass
from operator import attrgetter

import Orccraft


@dataclass
class Storage:
    users: list[Orccraft.User] = field(default_factory=list[Orccraft.User])

    # Auxiliary functions for function "show"
    def all_users(self):
        for user in self.users:
            print(user)
        return unit_data_manager()

    def order_by(self):
        order = int(input("Chose ordering:\n1. race\n2. class_\n3. hp\n4. mp\n5. strength\n"
                          "6. agility\n7. intelligence\n8. armor\n9. arrows\n"))
        orders = {1: "race", 2: "class_", 3: "hp", 4: "mp", 5: "strength", 6: "agility",
                  7: "intelligence", 8: "armor", 9: "arrows"}
        result = []
        for user in self.users:
            try:
                getattr(user, orders[order])
                result.append(user)
            except AttributeError:
                continue
        print(*sorted(result, key=attrgetter(orders[order])), sep='\n')
        return unit_data_manager()

    def get_user_by_id(self):
        inp_id = int(input("Enter id: "))
        for user in self.users:
            if user.id_ == inp_id:
                print(user)
        return unit_data_manager()

    def get_warrior(self):
        fld = int(input("Choose field:\n1. race\n2. class\n3. hp\n4. strength\n5. armor\n"))
        fld_dct = {1: 'race', 2: 'class_', 3: 'hp', 4: 'strength', 5: 'armor'}
        value = input("Enter value: ")
        for user in self.users:
            if user.__getattribute__(fld_dct[fld]) and str(user.__getattribute__(fld_dct[fld])) == value:
                print(user)
        return unit_data_manager()

    def get_archer(self):
        fld = int(input("Choose field:\n1. race\n2. class\n3. hp\n4. agility\n5. arrows\n"))
        fld_dct = {1: 'race', 2: 'class_', 3: 'hp', 4: 'agility', 5: 'arrows'}
        value = input("Enter value: ")
        for user in self.users:
            if getattr(user, fld_dct[fld]) and str(getattr(user, fld_dct[fld])) == value:
                print(user)
        return unit_data_manager()

    def get_wizard(self):
        fld = int(input("Choose field:\n1. race\n2. class\n3. hp\n4. intelligence\n5. mp\n"))
        fld_dct = {1: 'race', 2: 'class_', 3: 'hp', 4: 'intelligence', 5: 'mp'}
        value = input("Enter value: ")
        for user in self.users:
            if user.__getattribute__(fld_dct[fld]) and str(user.__getattribute__(fld_dct[fld])) == value:
                print(user)
        return unit_data_manager()

    def get_user_by_field(self):
        user_class = int(input("Enter class:\n1. Warrior\n2. Archer\n3. Wizard\n"))
        get_dct = {1: self.get_warrior, 2: self.get_archer, 3: self.get_wizard}
        if 1 < user_class > 3:
            return 0
        return get_dct[user_class]()

    # Select one mode to show user/users
    def show(self):
        if self.users:
            mode = int(input("1. All\n2. Order by <field>\n3. <id>\n4. Where <field> == <value>\n"))
            if 1 < mode > 4:
                return 0
            mode_dct = {1: self.all_users, 2: self.order_by, 3: self.get_user_by_id, 4: self.get_user_by_field}
            return mode_dct[mode]()
        else:
            print("No users yet\n")
            return unit_data_manager()

    # Insert user
    def insert(self):
        try:
            id_ = 0
            race = input("Enter race (str): ").capitalize()
            class_ = input("Enter class(str): ").capitalize()
            hp = int(input("Enter hp(digit): "))
            if class_.capitalize() == "Warrior":
                strength = int(input("Enter strength(digit): "))
                armor = int(input("Enter armor(digit): "))
                warrior = Orccraft.Warrior(id_, race, class_, hp, strength, armor)
                self.users.append(warrior)
                print("Inserting success\n")
            elif class_.capitalize() == "Archer":
                agility = int(input("Enter agility(digit): "))
                arrows = int(input("Enter arrows(digit): "))
                archer = Orccraft.Archer(id_, race, class_, hp, agility, arrows)
                self.users.append(archer)
                print("Inserting success\n")
            elif class_.capitalize() == "Wizard":
                intelligence = int(input("Enter intelligence(digit): "))
                mp = int(input("Enter mp(digit): "))
                wizard = Orccraft.Wizard(id_, race, class_, hp, intelligence, mp)
                self.users.append(wizard)
                print("Inserting success\n")
            else:
                print("There is no such race in the game")
            return unit_data_manager()
        except Exception as e:
            print(f"Error, {e}")
            return unit_data_manager()

    # Update user
    def update(self):
        user_id = int(input("Enter user id u want to update: "))
        fields = []
        fld = int(input("Enter field u want to update:\n0. race\n"
                        "1. class_\n2. hp\n3. mp\n4. strength\n"
                        "5. agility\n6. intelligence\n7. armor\n8. arrows\n9. Stop choosing fields\n"))
        while True:
            if fld != 9:
                fields.append(fld)
            else:
                print("Choosing fields have been stopped")
                break
            fld = int(input())

        for user in self.users:
            if user_id == user.id_:
                for f in fields:
                    if f == 0:
                        try:
                            user.race = input("Enter new value for race: ")
                            print("Updating was successful!")
                        except Exception as e:
                            print(f"Error, {e}")
                    elif f == 1:
                        try:
                            user.class_ = input("Enter new value for class: ")
                            print("Updating was successful!")
                        except Exception as e:
                            print(f"Error, {e}")
                    elif f == 2:
                        try:
                            user.hp = int(input("Enter new value for hp: "))
                            print("Updating was successful!")
                        except Exception as e:
                            print(f"Error, {e}")
                    elif f == 3:
                        try:
                            if user.class_ == 'Wizard':
                                user.mp = int(input("Enter new value for mp: "))
                                print("Updating was successful!")
                            else:
                                print("This unit is not wizard!")
                        except Exception as e:
                            print(f"Error, {e}")
                    elif f == 4:
                        try:
                            user.strength = int(input("Enter new value for strength: "))
                            print("Updating was successful!")
                        except Exception as e:
                            print(f"Error, {e}")
                    elif f == 5:
                        try:
                            user.agility = int(input("Enter new value for agility: "))
                            print("Updating was successful!")
                        except Exception as e:
                            print(f"Error, {e}")
                    elif f == 6:
                        try:
                            user.intelligence = int(input("Enter new value for intelligence: "))
                            print("Updating was successful!")
                        except Exception as e:
                            print(f"Error, {e}")
                    elif f == 7:
                        try:
                            if user.class_ == 'Warrior':
                                user.armor = int(input("Enter new value for armor: "))
                                print("Updating was successful!")
                            else:
                                print("This unit is not warrior!")
                        except Exception as e:
                            print(f"Error, {e}")
                    elif f == 8:
                        try:
                            if user.class_ == 'Archer':
                                user.arrows = int(input("Enter new value for arrows: "))
                                print("Updating was successful!")
                            else:
                                print("This unit is not archer!")
                        except Exception as e:
                            print(f"Error, {e}")
                return unit_data_manager()

    # Delete user
    def delete(self):
        user_id = int(input("Enter user id: "))
        try:
            for user in self.users:
                if user.id_ == user_id:
                    self.users.remove(user)
                    break
            print("Deletion was successful!\n")
        except Exception as e:
            print(f"Error: {e}")
        return unit_data_manager()

    # Exit from program
    def exit(self):
        return 0


# Choose command to do what u need
storage = Storage()


def unit_data_manager():
    command = int(input("1. Show\n2. Insert\n3. Update\n4. Delete\n5. Exit\n"))
    commands_dct = {1: storage.show, 2: storage.insert, 3: storage.update, 4: storage.delete, 5: storage.exit}
    if 1 < command > 5:
        return storage.exit()
    return commands_dct[command]()
