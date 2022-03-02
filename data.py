#Data structures
#1. dictionaries
#2. lists / arrays
#3. sets

lst = [1, 11, 1, 7]
print(lst)
lst.append(2)
print(lst)
lst.remove(11)
print(lst)
lst.sort()
print(lst)

st = {1,1,11,7}
st.add(1)
st.add(1)
st.add(11)
print(st)

d = {
    'bob':0,
    'sarah': 0,
    'defeated_by': {'paper', 'wolf'},
    'defeats': {'scissors', 'sponge'}
}

print(d['bob'])
d['bob'] += 1
print(d['bob'])
print(d)
d['michael'] = 7
print(d)
print(f"You are defeated by {d['defeated_by']}")
print(d.get['other', 42])