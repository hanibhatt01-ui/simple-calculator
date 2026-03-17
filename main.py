# main.py - Task execution script 
import utility # Custom module import 

def run_task():
    print("--- Week 4: Module & Exception Handling Task ---")

    # 1. Circle Area Test
    print(utility.calculate_area(5))
    print(utility.calculate_area("panch")) # Yeh error handle karega [cite: 22]

    # 2. List Access Test
    data = ["Python", "PHP", "MySQL"]
    print(utility.read_data_from_list(data, 1))
    print(utility.read_data_from_list(data, 10)) # Yeh Index error handle karega [cite: 22]

    # 3. Division Test
    print(utility.divide_numbers(10, 2))
    print(utility.divide_numbers(10, 0)) # Yeh ZeroDivision error handle karega [cite: 22]

if __name__ == "__main__":
    run_task()