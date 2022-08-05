import json
import os
import shutil
import ijson
import json

base = 'C:\\Users\\8851218\\Desktop\\ffhq\\'
thumbs = 'C:\\Users\\8851218\\Desktop\\ffhq\\thumbnails128x128\\'

def ParseByCountry() :
    file = open('C:\\Users\\8851218\\Desktop\\ffhq\\ffhq-dataset-v2.json', 'r')
    countries = []
    by_countries = {}
    i = 50
    for prefix, the_type, value in ijson.parse(file):
        if 'country' in prefix:
            val = value
            if val == '':
                val = 'undefined'
            if val not in countries:
                countries.append(val)
                by_countries[val] = []
            by_countries[val].append(prefix.split('.')[0].zfill(5))
    print(by_countries)
    print(countries)

    for item in by_countries.items():
        for i in item[1]:
            sub_path = str(int(i) // 1000 * 1000).zfill(5)
            f = os.path.join(thumbs, sub_path, f'{i}.png')
            target = os.path.join(base, 'parsed', item[0])
            if f'{i}.png' in os.listdir(os.path.join(thumbs, sub_path)):
                shutil.copy(f, target)

def ParseFemaleByHair() :
    file_path = 'C:\\Users\\8851218\\Desktop\\ffhq-features-dataset\\json\\'
    for f in os.listdir(file_path):
        sub_path = str((int(f[:-5]) // 1000) * 1000).zfill(5)
        if f'{f[:-5]}.png' in os.listdir(os.path.join(thumbs, sub_path)):
            file = open(os.path.join(file_path, f))
            js = json.load(file)
            if len(js) != 0:
                if 'faceAttributes' in js[0].keys():
                    max = 'other'
                    max_val = 0
                    for i in js[0]["faceAttributes"]["hair"]["hairColor"]:
                        if i["confidence"] > max_val:
                            max_val = i["confidence"]
                            max = i["color"]
                    file = os.path.join(thumbs, sub_path, f'{f[:-5]}.png')
                    target = os.path.join(base, 'female', max)
                    shutil.copy(file, target)

if __name__ == '__main__':
    ParseFemaleByHair()

    