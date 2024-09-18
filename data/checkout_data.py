from faker import Faker


class CheckoutData:
    """
    Генерация случайных данных для полей формы заказа
    """

    def __init__(self):
        self.faker = Faker()

    def generate_data(self):
        return {
            "first_name": self.faker.first_name(),
            "last_name": self.faker.last_name(),
            "postal_code": self.faker.zipcode(),
        }
