class Arrays():

    @staticmethod
    def print_in_col(array):
        for c in array:
            print(c)
            
    @staticmethod
    def print_in_row(array):
        n_Array = []
        for n in array:
            n_Array.append(str(n))
        print (";".join(n_Array))

    @staticmethod
    def crate_array(length,number):
        n_Array = []
        for n in range(length):
            n_Array.append(number)
        return n_Array

    @staticmethod
    def random_array(number,begin,end):
        import random
        n_Array = []
        for x in range(number):
            n_Array.append(random.randrange(begin,end))
        return n_Array

    @staticmethod
    def test(array,begin,end):
        count = 0
        for n in range(begin,end+1):
            for j in range(len(array)):
                if n==array[j]:
                    count +=1
        print(count)


if __name__ == '__main__':
    array01 = Arrays.crate_array(10,4)
    array02 = Arrays.random_array(20,-7,8)
    Arrays.test(array02,-1,1)


