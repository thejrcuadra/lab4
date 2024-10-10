def main():
    import csv

    # Create list to import data
    data = []
    with open("budget_data-1.csv") as file:
        rawData = csv.reader(file)
        # Passing data onto list
        for lines in rawData:
            data.append(lines)

    print("Unsorted Datset:")
    for line1 in data[:8]:
        print(line1)

    # Data sorted by Selection Sort
    selSortData = sortSelection(data)
    
    # Data sorted by Insertion Sort
    insSortData = sortInsertion(data)

    print("\nSelection Sort Dataset:")
    for line2 in selSortData[:8]:
        print(line2)

    print("\nInsertion Sorted Dataset:")
    for line3 in insSortData[:8]:
        print(line3)
    
def sortSelection(data):
    for x in range(1, len(data)):
        min = x
        # finding if there is a smaller value than the established one
        for y in range(x + 1, len(data)):
            # if there is, switching the values
            if data[y][0] < data[min][0]:
                min = y
        # changing the positions of the newest smallest value
        data[x], data[min] = data[min], data[x]

    return data

def sortInsertion(data):
    # starting in the 3rd position to ignore the first position which is the title/header of the csv file
    for i in range(2, len(data)):
        # establishing the key and second variable for sorting
        key = data[i]
        j = i-1
        # insertion sort algorithm
        while j >= 0 and key[0] < data[j][0]:
            data[j+1] = data[j]
            j -= 1
        data[j+1] = key

    return data

main()