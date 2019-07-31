import csv
import json
import pickle
from toolz import pipe, curry

map = curry(map)

def read_csv(filename):
    with open(filename, 'r') as f:
        rows = csv.reader(f)
        return list(rows)

def get_rows():
    return pipe(
        read_csv('data.csv'),
        map(lambda row: (row[0], row[17])),
        list,
        lambda xs: xs[:2200]
    )

def write_json(d, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(d, f, ensure_ascii=False)

def write(d, filename):
    with open(filename, 'wb') as f:
        pickle.dump(d, f, protocol=pickle.HIGHEST_PROTOCOL)

def main():
    rows = get_rows()
    ke = {k:v for k, v in rows}
    ek = {k:v for v, k in rows}
    write(ke, 'ke.pickle')
    write(ek, 'ek.pickle')




print(main())
