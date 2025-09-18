def main():
    number = int(input('Enter a integer'))
    if number % 2 != 0:
        result = 1
    else:
        result = 0

    if result:
        print(f'The value {number} is an odd number')
    else:
        print(f'The value {number} is an even number')
    return result


if __name__ == '__main__':
    main()
