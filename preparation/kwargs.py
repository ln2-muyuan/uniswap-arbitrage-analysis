def team(*members, **features):
    print(members)
    print(features)

    print(*members)
    print(*features)


team('John', 'Paul', 'George', 'Ringo', manager='Brian', drummer='Ringo', name="The Beatles")