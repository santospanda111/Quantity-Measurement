import json
import logging

logger = logging.getLogger()


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
            data_dict = {unit1: quantity1, unit2: quantity2}
            QuantityMeasurements.json_file_operation(data_dict)
            if quantity1 is not None and quantity2 is not None:
                quantity1 /= unit_dict.get(unit1)
                quantity2 /= unit_dict.get(unit2)
                if quantity1 == quantity2:
                    return True
            return False
        except Exception as e:
            logger.error(e)

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
            data_dict = {unit1: quantity1, unit2: quantity2}
            QuantityMeasurements.json_file_operation(data_dict)
            if quantity1 is not None and quantity2 is not None:
                quantity1 /= unit_dict.get(unit1)
                quantity2 /= unit_dict.get(unit2)
                if quantity1 == quantity2:
                    return True
            return False
        except Exception as e:
            logger.error(e)

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
            data_dict = {unit1: quantity1, unit2: quantity2}
            QuantityMeasurements.json_file_operation(data_dict)
            if quantity1 is not None and quantity2 is not None:
                quantity1 /= unit_dict.get(unit1)
                quantity2 /= unit_dict.get(unit2)
                if quantity1 == quantity2:
                    return True
            return False
        except Exception as e:
            logger.error(e)

    @staticmethod
    def json_file_operation(dict_data):
        with open('D:\PythonBridgelabz\QuantityMeasurement\main\data.json', 'a+') as json_file:
            json.dump(dict_data, json_file)
            json_file.write("\n")
