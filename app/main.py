class Car:

    def __init__(self, comfort_class, clean_mark, brand) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:

    def __init__(
        self,
        distance_from_city_center,
        clean_power,
        average_ratings,
        count_of_ratings
    ) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_ratings = average_ratings
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list) -> None:
        income = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                income += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return round(income, 1)

    def calculate_washing_price(self, car: Car):
        return round(car.comfort_class * (self.clean_power - car.clean_mark)
                     * self.average_rating / self.distance_from_city_center, 1)

    def wash_single_car(self, car: Car):
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def rate_service(self, rate):
        total_rate = self.average_ratings * self.count_of_ratings + rate
        self.count_of_ratings += 1
        self.average_rating = round(total_rate / self.count_of_ratings, 1)
