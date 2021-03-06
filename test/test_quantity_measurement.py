from main.quantity_measurement import QuantityMeasurements


class TestQuantityMeasurement:

    def test_lengths_given_0_ft_and_0_ft_should_compare_and_return_true(self):
        assert (QuantityMeasurements().compare_length("ft", "ft", 0, 0))

    def test_lengths_given_1_ft_and_5_ft_should_compare_and_return_false(self):
        assert not (QuantityMeasurements().compare_length("ft", "ft", 1, 5))

    def test_lengths_given_None_ft_and_5_ft_should_return_none(self):
        assert not (QuantityMeasurements().compare_length("ft", "ft", 5, None))

    def test_lengths_given_5_ft_and_5_ft_should_return_not_none(self):
        assert (QuantityMeasurements().compare_length("ft", "ft", 5, 5))

    def test_lengths_given_0_in_and_0_in_should_compare_and_return_true(self):
        assert (QuantityMeasurements().compare_length("in", "in", 0, 0))

    def test_lengths_given_1_in_and_5_in_should_compare_and_return_false(self):
        assert not (QuantityMeasurements().compare_length("in", "in", 1, 5))

    def test_lengths_given_0_ft_and_0_in_should_compare_and_return_true(self):
        assert (QuantityMeasurements().compare_length("ft", "in", 0, 0))

    def test_lengths_given_1_ft_and_1_in_should_compare_and_return_false(self):
        assert not (QuantityMeasurements().compare_length("ft", "in", 1, 1))

    def test_lengths_given_1_in_and_1_ft_should_compare_and_return_false(self):
        assert not (QuantityMeasurements().compare_length("in", "ft", 1, 1))

    def test_lengths_given_1_ft_and_12_in_should_compare_and_return_true(self):
        assert (QuantityMeasurements().compare_length("ft", "in", 1, 12))

    def test_lengths_given_12_in_and_1_ft_should_compare_and_return_true(self):
        assert (QuantityMeasurements().compare_length("in", "ft", 12, 1))

    def test_lengths_given_1_5_ft_and_18_in_should_compare_and_return_true(self):
        assert (QuantityMeasurements().compare_length("ft", "in", 1.5, 18))

    def test_lengths_given_3_ft_and_1_yd_should_compare_and_return_true(self):
        assert (QuantityMeasurements().compare_length("ft", "yd", 3, 1))

    def test_lengths_given_1_ft_and_1_yd_should_compare_and_return_false(self):
        assert not (QuantityMeasurements().compare_length("ft", "yd", 1, 1))

    def test_lengths_given_1_in_and_1_yd_should_compare_and_return_false(self):
        assert not (QuantityMeasurements().compare_length("in", "yd", 1, 1))

    def test_lengths_given_36_in_and_1_yd_should_compare_and_return_true(self):
        assert (QuantityMeasurements().compare_length("in", "yd", 36, 1))

    def test_lengths_given_1_yd_and_36_in_should_compare_and_return_true(self):
        assert (QuantityMeasurements().compare_length("yd", "in", 1, 36))

    def test_lengths_given_1_yd_and_3_ft_should_compare_and_return_true(self):
        assert (QuantityMeasurements().compare_length("yd", "ft", 1, 3))

    def test_weight_given_2decimal20_pound_and_1_kg_should_compare_and_return_true(self):
        assert (QuantityMeasurements().compare_weight("pound", "kg", 2.20, 1))

    def test_weight_given_1kg_and_2decimal20_pound_should_compare_and_return_true(self):
        assert (QuantityMeasurements().compare_weight("kg", "pound", 1, 2.20))

    def test_weight_given_1_pound_and_1_kg_should_compare_and_return_false(self):
        assert not (QuantityMeasurements().compare_weight("pound", "kg", 1, 1))

    def test_weight_given_1_kg_and_1_pound_should_compare_and_return_false(self):
        assert not (QuantityMeasurements().compare_weight("kg", "pound", 1, 1))

    def test_temp_given_33decimal8_fahrenheit_and_1_celsius_should_compare_and_return_true(self):
        assert (QuantityMeasurements().compare_temperature("fahrenheit", "celsius", 33.8, 1))

    def test_temp_given_1celsius_and_33decimal8_fahrenheit_should_compare_and_return_true(self):
        assert (QuantityMeasurements().compare_temperature("celsius", "fahrenheit", 1, 33.8))

    def test_temp_given_1_fahrenheit_and_1_celsius_should_compare_and_return_false(self):
        assert not (QuantityMeasurements().compare_temperature("fahrenheit", "celsius", 1, 1))

    def test_temp_given_1_celsius_and_1_fahrenheit_should_compare_and_return_false(self):
        assert not (QuantityMeasurements().compare_temperature("celsius", "fahrenheit", 1, 1))
