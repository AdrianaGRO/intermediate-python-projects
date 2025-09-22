class Bill:
    """Object that represents a bill, such as a utility bill,
    that needs to be paid by flatmates."""

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmate:
    """Creates a person who lives in the flat and pays a share of the bill."""

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill, other_flatmate):
        total_days = self.days_in_house + other_flatmate.days_in_house
        return bill.amount * self.days_in_house / total_days

