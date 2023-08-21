class Person:
    def __init__(self, name, phone, address, email) -> None:
        self.name = name
        self.phone = phone
        self.address = address
        self.email = email

    def update_conatct(self, new_phone):
        self.phone = new_phone


class Courier(Person):
    def __init__(self, name, phone, address, email) -> None:
        super().__init__(name, phone, address, email)

    def deliver_packages():
        print("delivered")


class Customer(Person):
    def __init__(self, id, name, phone, address, email) -> None:
        super().__init__(name, phone, address, email)
        self.customer_id = id

    def purchase():
        print("purchase")


class Employee(Person):
    def __init__(self, employee_number, name, phone, address, email) -> None:
        super().__init__(name, phone, address, email)
        self.employee_number = employee_number

    def promote():
        print("promote")

    def retire():
        print("retire")
