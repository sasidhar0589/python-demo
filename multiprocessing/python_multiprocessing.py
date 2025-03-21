import multiprocessing

def number_cube(number):
    print( number * number * number)
def number_square(number):
    print(number * number)
if __name__ == '__main__':
    process1 = multiprocessing.Process(target=number_cube, args=(5,))
    process2 = multiprocessing.Process(target=number_square, args=(5,))
    process1.start()
    process2.start()
    process1.join()
    process2.join()
    print("done")
    
# multi processing  pool setup assignment