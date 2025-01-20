

class Customer:
    def __init__(self, name, email, phone, address):
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address

    def __str__(self):
        return f"Name: {self.name}, Email: {self.email}, Phone: {self.phone}, Address: {self.address}"


class DataHandler:
    def __init__(self, file_path="customers.txt"):
        self.file_path = file_path

    def save(self, customer):
        with open(self.file_path, "a") as file:
            file.write(str(customer) + "\n")


class CustomerService:
    def __init__(self, data_handler):
        self.data_handler = data_handler

    def get_customer_info(self):
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        phone = input("Enter your phone number: ")
        address = input("Enter your address: ")
        return Customer(name, email, phone, address)

    def process_and_save(self):
        customer = self.get_customer_info()
        self.data_handler.save(customer)
        print("Customer information saved!")


if __name__ == '__main__':
    data_handler = DataHandler()
    service = CustomerService(data_handler)
    service.process_and_save()
