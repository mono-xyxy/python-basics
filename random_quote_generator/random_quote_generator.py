import random

quotes=[
      "The best way to get started is to quit talking and begin doing.",
    "Success is not final, failure is not fatal: it is the courage to continue that counts.",
    "Don’t let yesterday take up too much of today.",
    "Dream big and dare to fail.",
    "Do something today that your future self will thank you for."
]
quote = random.choice(quotes)

print("Random Quote: ")
print(quote)

quotes_dict = {
    "Albert Einstein": "Life is like riding a bicycle. To keep your balance you must keep moving.",
    "Walt Disney": "The way to get started is to quit talking and begin doing.",
    "Confucius": "It does not matter how slowly you go as long as you do not stop.",
    "Steve Jobs": "Stay hungry, stay foolish.",
}

author = random.choice(list(quotes_dict.keys()))
print("💡 Quote of the Moment\n")
print(f'"{quotes_dict[author]}"')
print(f"-{author}")