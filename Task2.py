text = input()
array_text = text.split()
check_jeck = ["Джек", "Джека", "Джеком", "Джеку", "Джеке"]
index = [i for i, x in enumerate(array_text) if x in check_jeck]
# print(index)
for i, x in enumerate(index):
    if array_text[i + x] == "Джек":
        array_text.insert(i + x, "капитан")
    if array_text[i + x] == "Джека":
        array_text.insert(i + x, "капитана")
    if array_text[i + x] == "Джеком":
        array_text.insert(i + x, "капитаном")
    if array_text[i + x] == "Джеку":
        array_text.insert(i + x, "капитану")
    if array_text[i + x] == "Джеке":
        array_text.insert(i + x, "капитане")

print(*array_text)