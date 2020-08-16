#1 파이썬은 C보다 느림.. 
words = set()

def check(word):
    if word.lower() in words:
        return True
    else:
        return False

def load(dictionary):
    file = open(dictionary, 'r')
    for line in file:
        words.add(line.rstrip('\n'))
    file.close()
    return True

def size():
    return len(words)

def unload():
    return True

#2 if문에서 single , double quote 구분해야 제대로 프린트 됨
people = {
    'Emma': '617-555-0100',
    'Rodrigo': '617-555-0101',
    'Brian': '617-555-0102',
    'David': '617-555-0103'
}

if 'Emma' in people:
    print(f"Found {people['Emma']}")