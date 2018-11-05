class FizzBuzz(object):

    def fizzbuzz(self, num):
        if num % 15 == 0:
            return "FizzBuzz"
        elif num % 3 == 0:
            return "Fizz"
        elif num % 5 == 0:
            return "Buzz"
        else:
            return num

    def print_fizzbuzz(self, start, end):
        arr = []
        for i in range(start, (end + 1)):
            arr.append(str(self.fizzbuzz(i)))
            outcome = ', '.join(arr)
        return (outcome)
