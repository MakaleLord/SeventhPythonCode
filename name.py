
<style>
@import url('https://fonts.googleapis.com/css?family=Roboto+Mono');
html{
   display:flex;
   justify-content:center;
   align-items: center;
   width: 100%;
   height: 100%;
   background-image: url('https://source.unsplash.com/collection/327760/1600x900');
   background-size:cover;
}

body{
   width:55%;
   height:60vh;
   border:1px solid lightgray;
   background-color:white;
   border-radius:8px;
   font-family: 'Roboto Mono', monospace;
   box-shadow: 0 14px 28px rgba(0,0,0,0.25), 0 10px 10px rgba(0,0,0,0.22);
   border-top:32px solid #eee;
   overflow-y:scroll;
}

body > div{
  height: calc(100% - 40px);
  overflow-y:auto;
  padding: 20px;
  font-size: 24px;
  white-space: pre;
}

pre{
  margin:inherit;
  font-family: inherit;
}
</style>

#!/usr/bin/python3
print("Content-type: text/html \n")

import magicwand, random


first_name_file = open("first-names.txt")
middle_name_file = open("middle-names.txt")
last_name_file = open("last-names.txt")

first_names = []
middle_names = middle_name_file.read().split("\n")
last_names = last_name_file.read().split("\n")

for line in first_name_file:
    new_line = line.rstrip()
    first_names.append(new_line)

first_name_file.close()  
middle_name_file.close()
last_name_file.close()
 
print("There are a total of:")
print(len(first_names), "first names")
print(len(middle_names), "middle names")
print(len(last_names), "last names")
print()

max_index = len(first_names) - 1
random_index = random.randint(0, max_index)
f_name = first_names[random_index]

random_index2 = random.randint(0, len(middle_names) - 1)
m_name = middle_names[random_index2]
random_index3 = random.randint(0, len(last_names) - 1)
l_name = last_names[random_index3]
print("Random name generator")
print(f_name, m_name, l_name)
