class QuantityMeasurements:

    @staticmethod
    def compare_length(unit1, unit2, quantity1, quantity2):
        """
        :param unit1: unit of 1st length
        :param unit2: unit of 2nd length
        :param quantity1: 1st length
        :param quantity2: 2nd length
        :return: equality of the lengths if both are not null
        """
        try:
            unit_dict = {"ft": 3, "in": 36, "yd": 1}
            if quantity1 is not None and quantity2 is not None:
                quantity1 /= unit_dict[unit1]
                quantity2 /= unit_dict[unit2]
                if quantity1 == quantity2:
                    return True
                else:
                    return False
            else:
                return None
        except Exception as e:
            print(e)

    @staticmethod
    def compare_weight(unit1, unit2, quantity1, quantity2):
        """
        :param unit1: unit of 1st weight
        :param unit2: unit of 2nd weight
        :param quantity1: 1st weight
        :param quantity2: 2nd weight
        :return: equality of the weights if both are not null
        """
        try:
            unit_dict = {"kg": 1, "pound": 2.20}
            if quantity1 is not None and quantity2 is not None:
                quantity1 /= unit_dict[unit1]
                quantity2 /= unit_dict[unit2]
                if quantity1 == quantity2:
                    return True
                else:
                    return False
            else:
                return None
        except Exception as e:
            print(e)

    @staticmethod
    def compare_temperature(unit1, unit2, quantity1, quantity2):
        """
        :param unit1: unit of 1st temp
        :param unit2: unit of 2nd temp
        :param quantity1: 1st temp
        :param quantity2: 2nd temp
        :return: equality of the temperatures if both are not null
        """
        try:
            unit_dict = {"celsius": 1, "fahrenheit": 33.8}
            if quantity1 is not None and quantity2 is not None:
                quantity1 /= unit_dict[unit1]
                quantity2 /= unit_dict[unit2]
                if quantity1 == quantity2:
                    return True
                else:
                    return False
            else:
                return None
        except Exception as e:
            print(e)


