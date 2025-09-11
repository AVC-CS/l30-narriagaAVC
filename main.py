def main():
    ##################################################
    # Comlete your code here
    ##################################################
    number = int(input('Enter your input: '))

    if number % 2 != 0:
        result = 1
    else:
        result = 0

    ########################################
    # Do not delete the return statement
    ########################################
    if result:
        print(f'The value {number} is an odd number')
    else:
        print(f'The value {number} is an even number')
    return result


if __name__ == '__main__':
    main()
