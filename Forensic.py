# coding=utf-8
gender = {"m": "TGCAGGAACTTC",
          "f": "TGAAGGACCTTC"}
hair_color = {"black": "CCAGCAATCGC",
              "brown": "GCCAGTGCCG",
              "ginger": "TTAGCTATCGC"}
face_shape = {"square": "GCCACGG",
              "round": "ACCACAA",
              "oval": "AGGCCTCA"}
eye_color = {"blue": "TTGTGGTGGC",
             "green": "GGGAGGTGGC",
             "brown": "AAGTAGTGAC"}
rase = {"c": "AAAACCTCA",
        "b": "CGACTACAG",
        "a": "CGCGGGCCG"}

characteristics = {"sex": gender,
                   "hair": hair_color,
                   "face": face_shape,
                   "eyes": eye_color,
                   "rase": rase}

person_charactaristics = {
    "ziga": {
        "sex": "m",
        "rase": "c",
        "hair": "orange",
        "eyes": "brown",
        "face": "round"
    },
    "matej": {
        "sex": "m",
        "rase": "c",
        "hair": "black",
        "eyes": "blue",
        "face": "oval"
    },
    "miha": {
        "sex": "m",
        "rase": "c",
        "hair": "brown",
        "eyes": "green",
        "face": "square"
    }

}

# suspect = open("DNA.txt", "r")
with open("DNA.txt", "r") as suspect:
    # print suspect
    suspect_dna = suspect.read()

suspect_characteristics = {}
for key, value in characteristics.iteritems():
    # print key
    for ch, ch_dna in value.iteritems():
        if ch_dna in suspect_dna:
            print "Match found", ch
            suspect_characteristics[key] = ch

print suspect_characteristics

out = []
for name, ch in person_charactaristics.iteritems():
    # print name, ch
    for c, c_data in ch.iteritems():
        # print "    ", c, c_data
        if suspect_characteristics[c] == c_data:
            print "match found", name, c
            out.append(name)
print out

out_unique = set(out)

max_count = 0
max_name = ""
for name in out_unique:
    # print name, out.count(name)
    if max_count < out.count(name):
        max_count = out.count(name)
        max_name = name

print max_name, max_count