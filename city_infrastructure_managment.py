#Task 1: Vehicle Registration System
def task_one():

    print('Task 1')

    class Vehicle:
        def __init__(self,regestration_num,type,owner):
            self.reg_num = regestration_num
            self.type = type
            self.owner = owner

        def update_owner(self,new_owner):
            if not self.owner == new_owner:
                self.owner = new_owner
                print(f'{self.owner} is the new owner!')
            else:
                print(f'{self.owner} is already the owner!')

    toyota = Vehicle(123456789,'sedan','bob')
    bmw = Vehicle(123678,'sedan','jill')
    range_rover = Vehicle(78423,'suv','bob')

    toyota.update_owner('jill')
    bmw.update_owner('bob')
    range_rover.update_owner('bob')

#Task 2: Event Management System Enhancement
def task_two():

    print(f'\nTask 2')

    class Event:
        def __init__(self, name, date):
            self.name = name
            self.date = date
            self.participants = 0

        def add_participants(self):
            try:
                add = int(input('How many participants would you like to add?'))
                self.participants += add
            except:
                print('That is not a valid number, please try again')

        def get_participant_count(self):
            print(f'The current participant count is {self.participants}')

    birthday_party = Event('birthday','today')

    while True:
        birthday_party.add_participants()
        birthday_party.get_participant_count()
    
if __name__ == "__main__":
    task_one()
    task_two()