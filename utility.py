# utility.py - Custom Module with Exception Handling [cite: 21, 24]

def calculate_area(radius):
    """Circle ka area nikalne ke liye [cite: 21]"""
    try:
        if radius < 0:
            raise ValueError("Radius negative nahi ho sakta.")
        area = 3.14159 * (radius ** 2)
        return f"Area: {area}"
    except TypeError:
        return "Error: Please radius mein sirf number likhein. [cite: 22]"
    except ValueError as ve:
        return f"Error: {ve} [cite: 22]"

def read_data_from_list(my_list, index):
    """List se data nikalne ke liye [cite: 21]"""
    try:
        value = my_list[index]
        return f"Value: {value}"
    except IndexError:
        return "Error: Yeh index list ki range se bahar hai. [cite: 22]"
    except TypeError:
        return "Error: Index hamesha ek integer hona chahiye. [cite: 22]"

def divide_numbers(a, b):
    """Do numbers ko divide karne ke liye [cite: 21]"""
    try:
        result = a / b
        return f"Result: {result}"
    except ZeroDivisionError:
        return "Error: Zero se divide karna allowed nahi hai. [cite: 22]"
    finally:
        # Yeh block hamesha chalega chahe error aaye ya na aaye [cite: 22]
        print("Division check complete.")