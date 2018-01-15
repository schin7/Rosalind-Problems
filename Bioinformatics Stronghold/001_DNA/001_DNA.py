f = open("C:\Users\Owner\Google Drive\Bioinformatics", 'r')
raw_seq = f.readline().rstrip()
f.close()

print raw_seq.count("A"),
print raw_seq.count("C"),
print raw_seq.count("G"),
print raw_seq.count("T")
