class Feet:
    def __init__(self, feet):
        self.feet = feet

    def __eq__(self, other):
        """
        -Here i have used isinstance method will check whether the other value is inch or feet.
        :param other:
        :return:Boolean value
        """
        if isinstance(other, Feet):
            return self.feet == other.feet
        elif isinstance(other, Inch):
            return self.feet == other.inch / 12
        elif isinstance(other, Yard):
            return self.feet == other.yard * 3
        return False


class Inch:
    def __init__(self, inch):
        self.inch = inch

    def __eq__(self, other):
        """
        -Here i have used isinstance method will check whether the other value is inch or feet.
        :param other:
        :return:Boolean Value
        """
        if isinstance(other, Inch):
            return self.inch == other.inch
        elif isinstance(other, Feet):
            return self.inch == other.feet * 12
        elif isinstance(other, Yard):
            return self.inch == other.yard * 36
        return False


class Yard:
    def __init__(self, yard):
        self.yard = yard

    def __eq__(self, other):
        """
        -Here i have used isinstance method will check whether the other value is inch or feet.
        :param other:
        :return:Boolean Value
        """
        if isinstance(other, Yard):
            return self.yard == other.yard
        elif isinstance(other, Feet):
            return self.yard == other.feet / 3
        elif isinstance(other, Inch):
            return self.yard == other.inch / 36
        return False


if __name__ == '__main__':
    print("Welcome to Quantity_Measurement Program")