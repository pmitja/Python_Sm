from pathlib import Path

# reading dna file
data = Path(".", "data", "dna.txt")
data = data.read_text()

# creating dict for ice cream murder

suspect = {}

# creating dna for each
eva = {
    "gender": "female",
    "race": "white",
    "hair color": "blonde",
    "eye color": "blue",
    "face shape": "oval",
}
larisa = {
    "gender": "female",
    "race": "white",
    "hair color": "brown",
    "eye color": "brown",
    "face shape": "oval",
}
matej = {
    "gender": "male",
    "race": "white",
    "hair color": "black",
    "eye color": "blue",
    "face shape": "oval",
}
miha = {
    "gender": "male",
    "race": "white",
    "hair color": "brown",
    "eye color": "green",
    "face shape": "square",
}

# Info for dnas:
male = "TGCAGGAACTTC"
female = "TGAAGGACCTTC"

brown_hair = "GCCAGTGCCG"
black_hair = "CCAGCAATCGC"
blonde_hair = "TTAGCTATCGC"

square_shape = "GCCACGG"
round_shape = "ACCACAA"
oval_shape = "AGGCCTCA"

blue_eyes = "TTGTGGTGGC"
green_eyes = "GGGAGGTGGC"
brow_eyes = "AAGTAGTGAC"

white_race = "AAAACCTCA"
black_race = "CGACTACAG"
asian_race = "CGCGGGCCG"

# Gender check
if data.find(male) != -1:
    suspect["gender"] = "male"
elif data.find(female) != -1:
    suspect["gender"] = "female"
else:
    print("Hmmm...")

# Race check
if data.find(white_race) != -1:
    suspect["race"] = "white"
elif data.find(black_race) != -1:
    suspect["race"] = "black"
elif data.find(asian_race) != -1:
    suspect["race"] = "asian"
else:
    print("Alien.")

# Hair color check
if data.find(brown_hair) != -1:
    suspect["hair color"] = "brown"
elif data.find(black_hair) != -1:
    suspect["hair color"] = "black"
elif data.find(blonde_hair) != -1:
    suspect["hair color"] = "blonde"
else:
    print("No hair color, he is bald.")

# Eye color
if data.find(blue_eyes) != -1:
    suspect["eye color"] = "blue"
elif data.find(green_eyes) != -1:
    suspect["eye color"] = "green"
elif data.find(brow_eyes) != -1:
    suspect["eye color"] = "brown"
else:
    print("Suspect have no eyes.")

# Face shape
if data.find(square_shape) != -1:
    suspect["face shape"] = "square"
elif data.find(oval_shape) != -1:
    suspect["face shape"] = "oval"
elif data.find(round_shape) != -1:
    suspect["face shape"] = "round"
else:
    print("Triangle shape?.")

print(f"Killer characteristics matching with DNA: \n{suspect}\n")
if suspect == eva:
    print("Ice cream killer is Eva!")
elif suspect == larisa:
    print("Ice cream killer is Larisa!")
elif suspect == miha:
    print("Ice cream killer is Miha!")
else:
    print("Ice cream killer is Matej!")
