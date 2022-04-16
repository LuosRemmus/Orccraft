from dataclasses import dataclass, field
from operator import attrgetter

global counter
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
            mp = int(input("Enter mp(digit): "))
            strength = int(input("Enter strength(digit): "))
            agility = int(input("Enter agility(digit): "))
            intelligence = int(input("Enter intelligence(digit): "))
            armor = int(input("Enter armor(digit): "))
            arrows = int(input("Enter arrows(digit): "))

            new_user = User(id_, race, class_, hp, mp, strength, agility, intelligence, armor, arrows)
            self.users.append(new_user)
            print("Inserting success\n")
            return unit_data_manager()
        except Exception as e:
            print(f"Error, {e}")
            return unit_data_manager()

    # Update user
    def update(self):
        pass

    # Delete user
    def delete(self):
        pass

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
