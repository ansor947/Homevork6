

from pprint import pprint

with open(r"C:\Users\Андрей-сан\Desktop\py-homework-basic-files\2.4.files\sorted\1.txt", 'rt', encoding='utf-8') as f:
                data_1 = f.readlines()
                data_1 = [line.rstrip() for line in data_1]
with open(r"C:\Users\Андрей-сан\Desktop\py-homework-basic-files\2.4.files\sorted\2.txt", 'rt', encoding='utf-8') as f:
                data_2 = f.readlines()
                data_2 = [line.rstrip() for line in data_2]
with open(r"C:\Users\Андрей-сан\Desktop\py-homework-basic-files\2.4.files\sorted\3.txt", 'rt', encoding='utf-8') as f:
                data_3 = f.readlines()
                data_3 = [line.rstrip() for line in data_3]       

words_2 = data_2
words_1 = data_1
words_3 = data_3

file1 = open('neu1.txt', 'x', encoding='utf-8')
file1.write("2.txt\n")
file1.write("1\n")
file1.write('\n'.join(words_2))
file1.write("\n1.txt\n")
file1.write("8\n")
file1.write('\n'.join(words_1))
file1.write("\n3.txt\n")
file1.write("9\n")
file1.write('\n'.join(words_3))

