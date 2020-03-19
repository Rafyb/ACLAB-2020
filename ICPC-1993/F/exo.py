import os
working_directory = os.getcwd().replace("\\",'/')
file_path = working_directory + '/ICPC-1993/F/test.txt'
mon_fichier = open(file_path,"r")
print(file_path)
line = mon_fichier.readline()
mon_fichier.close()