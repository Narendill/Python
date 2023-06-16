import serialization as ser

if __name__ == '__main__':
    ser.Task1.txt_to_json(r'C:\Users\Narendill\Desktop\9_Pogr_in_Python\HW\HW-8\example_1.txt')
    ser.Task2.write_data(r'C:\Users\Narendill\Desktop\9_Pogr_in_Python\HW\HW-8\task2.json')
    ser.Task3.json_to_csv(r'C:\Users\Narendill\Desktop\9_Pogr_in_Python\HW\HW-8\task2.json')
    ser.Task4.csv_to_json(r'C:\Users\Narendill\Desktop\9_Pogr_in_Python\HW\HW-8\task2.csv', 'task4.json')
    ser.Task5.json_to_pickle(r'C:\Users\Narendill\Desktop\9_Pogr_in_Python\HW\HW-8')
    ser.Task6.pickle_to_csv(r'C:\Users\Narendill\Desktop\9_Pogr_in_Python\HW\HW-8\task4.pickle')
    ser.Task7.print_csv_to_pickle(r'C:\Users\Narendill\Desktop\9_Pogr_in_Python\HW\HW-8\task4.csv')
    ser.TaskHW.get_files(r'C:\Users\Narendill\Desktop\9_Pogr_in_Python\Seminars\8')