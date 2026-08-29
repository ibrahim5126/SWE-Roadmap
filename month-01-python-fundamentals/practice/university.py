'''name = ["Jin", "Lars", "Kazuya", "Aiko"]

family_name = ["Kazama", "Smith", "Mishima", "Nishimura"]

name ={
    "Jin": "Kazama",
    "Aiko": "Nishimura",
    "Kiryu": "Kazama", 
    "Kazuya": "Mishima"
}

for names in name:
    print(names, name[names], sep = ", ")'''


names = [
    {"Name": "Jin", "Family Name": "Kazama", "Occupation": "CEO"},
    {"Name": "Aiko", "Family Name": "Nishimura", "Occupation": "Journalist"},
    {"Name": "Alex", "Family Name": "Smith", "Occupation": None}
]

for name in names:
    print(name["Name"], name["Family Name"], name["Occupation"], sep = ", ")