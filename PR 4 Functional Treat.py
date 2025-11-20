# PR4 Functional Treat
# Name Kunj Mistry
# GR ID : 12078
# Batch : RW6
# Date : 20/11/25

print("Welcome to data analyzer and transformer Program!")
data = []

while True:

    print(" ")
    print("Main Menu:")
    print("1. Input data")
    print("2. Display data summary")
    print("3. Calculate factorial")
    print("4. Filter data by threshold")
    print("5. Sort data")
    print("6. Display dataset statistics")
    print("7. Exit")

    print(" ")
    choice = int(input("Enter your choice (1-7): "))
    print(" ")

    match choice:

        case 1:
            data = input("Enter data for 1D array (separated by spaces):").split(" ")
            data = [int(x) for x in data]
            print("Data input successful.")

        case 2:
            if not data:
                print("Please input data first.")
            else:
                summery(data)

        case 3:
            fac = int(input("Enter a number to calculate its factorial: "))
            def factorial(fac):
                if fac == 0 or fac == 1:
                    return 1
                return fac * factorial(fac - 1) 
            result = factorial(fac)
            print(result)

        case 4:
            if not data:
                print("Please input data first!")
            else:
                filter_by_threshold(data)

        case 5:
            if not data:
                print("Please input data first.")
            else:
                sort_dataset(data)

        case 6:
            if not data:
                print("Please input data first.")
            else:
                display_multiple_values(data)

        case 7:
            print("Thankyou for using Data Analyzer Program and Transformer Program. Goodbye!")
            break



    def summery(data):
        print("Data Summary:")
        print(f"Total elements:{len(data)}")
        print(f"Min value:{min(data)}")
        print(f"Max value:{max(data)}")
        print(f"sum of elements:{sum(data)}")
        print(f"Average value:{sum(data) / len(data)}")

    def sort_dataset(data):
        print("1. Sort in ascending order")
        print("2. Sort in descending order")
        sort_1 = int(input("Enter your choice: "))
        if sort_1 == 1:
            data.sort()
            print("Data sorted in ascending order:", data)
        elif sort_1 == 2:
            data.sort(reverse=True)
            print("Data sorted in descending order:", data)
        
    def display_multiple_values(data):
        print("Dataset Statistics:")
        print(f" Minimum value: {min(data)}")
        print(f" Maximum value: {max(data)}")
        print(f" Sum of all values: {sum(data)}")
        print(f" Average value: {calculate_average(data):}")

    def calculate_average(data):
        return sum(data) / len(data)
    
    def filter_by_threshold(data):
        threshold = int(input("Enter a threshold value: "))
        filtered_data = list(filter(lambda x: x <= threshold, data))
        print(f"Filtered Data (values <= {threshold}): {filtered_data}")