import re
lore = "Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit..."
words = re.findall("\w{6,}",lore)
validate = []
for word in words:
    validate.append(word)
print(validate)
