text_raw = input()
text = text_raw.replace(',', "")
array_text = text.split(' ')
fairytale = []
for i in range(len(array_text)):
    if i < (len(array_text) - 2):
        fairytale.extend(["от", array_text[i], "ушёл,"])
    if i == (len(array_text) - 2):
        fairytale.extend(["и от", array_text[i], "ушёл,"])
    if i == (len(array_text) - 1):
        fairytale.extend(["а лиса — ам его! и нету колобка..."])
        
print(*fairytale)