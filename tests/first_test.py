import pytest

from app.calculator import Calculator


class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_adding_success(self):
        assert self.calc.adding(self, 5, 1) == 6

    def test_adding_unsuccess(self):
        assert self.calc.adding(self, 1, 4) == 3

    def test_zero_division(self):
        with pytest.raises(ZeroDivisionError):
            self.calc.division(self, 1, 0)

    def test_division(self):
        assert self.calc.division(self, 9, 3) ==3

    def test_multiply_success(self):
        assert self.calc.multiply(self, 10, 5) ==50

    def test_multiply_unsuccess(self):
        assert self.calc.multiply(self, 2, 0) ==2

    def test_subtraction(self):
        assert self.calc.subtraction(self,5, 2) ==3

    def test_substraction(self):
        assert self.calc.subtraction(self, 2,8) == -6

    def teardown(self):
        print('Выполнение метода Teardown')

