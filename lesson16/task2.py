class Mathematician:

    def square_nums(self, your_list : list):
        return [num ** 2 for num in your_list]
    
    def remove_positives(self, your_list : list):
        return [num for num in your_list if num < 0]
    
    def filter_leaps(self, your_list : list):
        return [num for num in your_list if num % 400 == 0 or (num % 4 == 0 and num % 100 != 0)]

m = Mathematician()
assert m.square_nums([7, 11, 5, 4]) == [49, 121, 25, 16]
assert m.remove_positives([26, -11, -8, 13, -90]) == [-11, -8, -90]
assert m.filter_leaps([2001, 1884, 1995, 2003, 2020]) == [1884, 2020]