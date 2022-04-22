from dataclasses import dataclass, field
from operator import attrgetter

counter: int = 0


@dataclass
class User:
    # **********    user data fields   **********
    id_: int
    race: str
    class_: str
    hp: int
    mp: int
    strength: int
    agility: int
    intelligence: int
    armor: int
    arrows: int


@dataclass
class Storage:
    users: list[User] = field(default_factory=list[User])

    # Auxiliary functions for function "show"
    def all_users(self):
        for user in self.users:
            print(user)
        print()
        return unit_data_manager()

    def order_by(self):
        order = int(input("Chose ordering:\n0. race\n1. class_\n2. hp\n3. mp\n4. strength\n"
                          "5. agility\n6. intelligence\n7. armor\n8. arrows\n"))
        orders = ["race", "class_", "hp", "mp", "strength", "agility",
                  "intelligence", "armor", "arrows"]
        print(*sorted(self.users, key=attrgetter(orders[order])), sep='\n')
        return unit_data_manager()

    def get_user_by_id(self):
        inp_id = int(input("Enter id: "))
        for user in self.users:
            if user.id_ == inp_id:
                print(f"{user}\n")
                return unit_data_manager()

    def get_user_by_field(self):
        inp_field = int(input("Choose field:\n0. race\n1. class_\n2. hp\n3. mp\n4. strength\n"
                              "5. agility\n6. intelligence\n7. armor\n8. arrows\n"))
        value = input("Enter value of field: ").capitalize()
        for user in self.users:
            if inp_field == 0:
                if user.race == value:
                    print(user)
            elif inp_field == 1:
                if user.class_ == value:
                    print(user)
            elif inp_field == 2:
                if str(user.hp) == value:
                    print(user)
            elif inp_field == 3:
                if str(user.mp) == value:
                    print(user)
            elif inp_field == 4:
                if str(user.strength) == value:
                    print(user)
            elif inp_field == 5:
                if str(user.agility) == value:
                    print(user)
            elif inp_field == 6:
                if str(user.intelligence) == value:
                    print(user)
            elif inp_field == 7:
                if str(user.armor) == value:
                    print(user)
            elif inp_field == 8:
                if str(user.arrows) == value:
                    print(user)
        return unit_data_manager()

    # Select one mode to show user/users
    def show(self):
        if self.users:
            mode = int(input("1. All\n2. Order by <field>\n3. <id>\n4. Where <field> == <value>\n"))
            mode_dct = {1: self.all_users, 2: self.order_by, 3: self.get_user_by_id, 4: self.get_user_by_field}
            return mode_dct[mode]()
        else:
            print("No users yet\n")
            return unit_data_manager()

    # Insert user
    def insert(self):
        global counter
        try:
            id_ = counter
            counter += 1
            race = input("Enter race (str): ").capitalize()
            class_ = input("Enter class(str): ").capitalize()
            hp = int(input("Enter hp(digit): "))
            if class_.lower() == 'wizard':
                mp = int(input("Enter mp(digit): "))
            else:
                mp = 0
            strength = int(input("Enter strength(digit): "))
            agility = int(input("Enter agility(digit): "))
            intelligence = int(input("Enter intelligence(digit): "))
            if class_.lower() == 'warrior':
                armor = int(input("Enter armor(digit): "))
            else:
                armor = 0
            if class_.lower() == 'archer':
                arrows = int(input("Enter arrows(digit): "))
            else:
                arrows = 0

            new_user = User(id_, race, class_, hp, mp, strength, agility, intelligence, armor, arrows)
            self.users.append(new_user)
            print("Inserting success\n")
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
            print("Deletion was successful!")
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
    return commands_dct[command]()


if __name__ == '__main__':
    unit_data_manager()
