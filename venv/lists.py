lucky_numbers = [45, 56,98,34,23]
friends = ["Harry", "Mary", "Janet", "Bob", "Halbert"]
friends.extend(lucky_numbers)
print(friends)

lucky_numbers = [45, 56,98,34,23]
friends = ["Harry", "Mary", "Janet", "Bob", "Halbert"]
friends.append("creed")
print(friends)


lucky_numbers = [45, 56,98,34,23]
friends = ["Harry", "Mary", "Janet", "Bob", "Halbert"]
friends.insert(2,"Charlie")
print(friends)

lucky_numbers = [45, 56,98,34,23]
friends = ["Harry", "Mary", "Janet", "Bob", "Halbert"]
friends.remove("Mary")
print(friends)


lucky_numbers = [45, 56,98,34,23]
friends = ["Harry", "Mary", "Janet", "Bob", "Halbert"]
friends.remove("Mary")
print(friends.index("Janet"))

lucky_numbers = [45, 56,98,34,23]
friends = ["Harry", "Mary", "Janet", "Bob", "Halbert"]
lucky_numbers.sort()
print(lucky_numbers)
