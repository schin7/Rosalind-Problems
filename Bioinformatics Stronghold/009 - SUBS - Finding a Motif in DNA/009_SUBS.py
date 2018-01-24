def main():
    with open('C:/Users/Owner/Desktop/rosalind_subs.txt', 'r') as infile:
        s, t = infile.read().strip().split('\n')

    pos = []
    for i in range(len(s)):
        if s.startswith(t, i):
            pos.append(i+1) # Rosalind example uses 1-based numbering

    print(' '.join(map(str, pos)))


if __name__ == '__main__':
    main()