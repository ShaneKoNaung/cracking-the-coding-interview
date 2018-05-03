from threeInOne import FixedMultiStack


def main():
    a = FixedMultiStack(10)

    for i in range(10):
        a.push(0, i)
    for i in range(3):
        a.push(1, i)
    for i in range(3, 11):
        a.push(2, i)

    print(a.top(0))
    print(a.top(1))
    print(a.top(2))

    a.push(1, 34)
    print(a.top(1))


if __name__ == "__main__":
    main()
