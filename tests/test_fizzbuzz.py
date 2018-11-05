from fizzbuzz import FizzBuzz

def test_fizz_when_num_is_3():
    instance = FizzBuzz()
    assert instance.fizzbuzz(3) == "Fizz"

def test_buzz_when_num_is_5():
    instance = FizzBuzz()
    assert instance.fizzbuzz(5) == "Buzz"

def test_fizzbuzz_when_num_is_15():
    instance = FizzBuzz()
    assert instance.fizzbuzz(15) == "FizzBuzz"

def test_print_fizzbuzz_given_range():
    instance = FizzBuzz()
    assert instance.print_fizzbuzz(4, 7) == "4, Buzz, Fizz, 7"
