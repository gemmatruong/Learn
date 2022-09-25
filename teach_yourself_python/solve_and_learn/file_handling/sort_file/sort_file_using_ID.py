import csv


with open('fakefacebook_write.txt','r', newline = "") as f:
    reader = csv.reader(f)
    sorted_list = list(reader) 
    sorted_list.sort(key = lambda x:x[0])
    print("\n".join(str(row) for row in sorted_list))
