import re
lore = "Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit..."
words =re.findall("\w+",lore)
#jebac to

print(words)