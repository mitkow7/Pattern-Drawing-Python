def right_triangle(rows):
    for i in range(1, rows + 1):
        print(i * '*')


def pyramid(rows):
    for i in range(1, rows + 1):
        for j in range(rows - i):
            print(' ', end='')
        for k in range(2 * i - 1):
            print('*', end='')
        print()


def square(size):
    for i in range(size):
        for j in range(size):
            if i == 0 or i == size - 1 or j == 0 or j == size - 1:
                print('*', end='')
            else:
                print(' ', end='')
        print()


def full_square(rows):
    for i in range(rows):
        for j in range(rows):
            print('*', end='')
        print()


def diamond(height):
    for i in range(height):
        print(" " * (height - i) + " *" * (i + 1))

    for i in range(height - 1):
        print(" " * (i + 2) + " *" * (height - i - 1))


while True:
    print("Choose a pattern you want to draw\n"
          "Right-angled Triangle (1)\n"
          "Pyramid (2)\n"
          "Square with Hollow Center (3)\n"
          "Full square (4)\n"
          "Diamond (5)")

    pattern = input('Enter pattern: ')

    if pattern == 'Right-angled Triangle' or pattern == '1':
        rows_ = int(input('Enter number of rows: '))
        right_triangle(rows_)
    elif pattern == 'Pyramid' or pattern == '2':
        rows = int(input('Enter number of rows: '))
        pyramid(rows)
    elif pattern == 'Square with Hollow Center' or pattern == '3':
        size = int(input('Enter a square size: '))
        square(size)
    elif pattern == 'Full square' or pattern == '4':
        size = int(input('Enter a square size: '))
        full_square(size)
    elif pattern == 'Diamond' or pattern == '5':
        height = int(input('Enter height of the Diamond: '))
        diamond(height)
    else:
        print('Invalid pattern! ')

    continue_choice = input('Do you want to continue? (y/n): ')
    if continue_choice == 'n':
        break
    print()

print('Finished!')

