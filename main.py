from array import array


def main():

    random_ints = [13, 5, 2, 9, 1, 33, 17, 4, 23, 29]

    def tri_insertion(numbers: array) -> array:
        index = 1
        while index < len(numbers):
            insideIndex = index
            while numbers[insideIndex] < numbers[insideIndex - 1] and insideIndex > 0:
                holder = numbers[insideIndex]
                numbers[insideIndex] = numbers[insideIndex - 1]
                numbers[insideIndex - 1] = holder
                insideIndex -= 1
            index += 1
        print(numbers)

    tri_insertion(random_ints)

if __name__ == "__main__":
    main()

