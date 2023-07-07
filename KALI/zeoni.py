baseword = "Orion"
dollaro = "$"
zeroni = "10000"

file_path = 'NotesUltra.txt'#Path to File

file = open(file_path, 'w')

for x in range (0,10000):
    true_x = x

    print(true_x)


    cap_x = str(true_x)
    word_num = baseword+cap_x
    file.write(word_num + "\n")

    for a in range (1,11):
        dinero = word_num + str(dollaro * a)
        #print(dinero)
        file.write(dinero + "\n")
        #temp=y


    cap_x = "0"+str(true_x)
    word_num = baseword + cap_x
    file.write(word_num + "\n")

    for b in range (1,11):
        dinero = word_num + str(dollaro * b)
        #print(dinero)
        file.write(dinero + "\n")
        #temp=y


    cap_x = "00"+str(true_x)
    word_num = baseword + cap_x
    file.write(word_num + "\n")

    for c in range (1,11):
        dinero = word_num + str(dollaro * c)
        #print(dinero)
        file.write(dinero + "\n")
        #temp=y


    cap_x = "000"+str(true_x)
    word_num = baseword + cap_x
    file.write(word_num + "\n")

    for d in range (1,11):
        dinero = word_num + str(dollaro * d)
        #print(dinero)
        file.write(dinero + "\n")
        #temp=y


    cap_x = "0000"+str(true_x)
    word_num = baseword + cap_x
    file.write(word_num + "\n")




    for y in range (1,11):
        dinero = word_num + str(dollaro * y)
        #print(dinero)
        file.write(dinero + "\n")
        #temp=y

print("Well if we got this far, there are no syntax errors :)")
#4 - Closing the File

file.close() #Close the file