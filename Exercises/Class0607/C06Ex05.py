import shelve
fname = ('Galab', 'Rizvi')
lname = {1:'Bista', 2:'Khanal'}
with shelve.open('out.shelf') as shelfie:
    shelfie['First Name'] = fname
    shelfie['Last Name'] = lname

with shelve.open('out.shelf') as shelfie:
  print("keys --->",list(shelfie.keys()))
  print("values ->", list(shelfie.values()))