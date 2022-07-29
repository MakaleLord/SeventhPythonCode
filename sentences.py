
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
import magicwand
import random
 
sentances_tuple = ("The toy brought back fond memories",
                   "You have every right to be angry",
                   "I liked their first two albums", 
                   "He loved eating bananas in hot dog buns")

print("Can you complete the sentences:")
print()

for sentance in sentances_tuple:
    jumbled_sentance = ""
    s_list = sentance.split(" ")
    max_index = len(s_list) - 1 
    rand_index1 = random.randint(0, max_index)
    rand_index2 = random.randint(0, max_index)
    rand_index3 = random.randint(0, max_index)
    
    for word in s_list:
        if word == s_list[rand_index1] or word == s_list[rand_index2] or word == s_list[rand_index3]:
            jumbled_sentance = jumbled_sentance + ("_" * len(word)) + " "
        else: 
            jumbled_sentance = jumbled_sentance + word + " "
    print(jumbled_sentance)
    print()

print()
print()
print()
print()
print()
print()
print()

print("Correct Answers:")
for sentance in sentances_tuple:
    print(sentance)
