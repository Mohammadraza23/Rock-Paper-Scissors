# User input
input = str(input("Enter a sentence: "))
# split function being used in order to split the sentence
txt = input.split()
# storing acronym of a phrase in variable x
x = " "

# for loop over txt, representing split of user input
for i in txt:
    x = x + str(i[0]).upper()
print(x)
