import re
lore = "Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit..."
words = re.findall("\w+",lore)
validate = []
for word in words:
    if len(word) >= 6:
        validate.append(word)
print(validate)