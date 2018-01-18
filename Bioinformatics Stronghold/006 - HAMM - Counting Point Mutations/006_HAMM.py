def hamm_dist(dna):
    hamm = 0

    for i in range(len(dna[0])):
        if dna[0][i] != dna[1][i]:
            hamm +=1

    return hamm

def main():
    with open('C:/Users/Owner/Desktop/rosalind_hamm.txt', 'r') as f:
        seqs = f.read().split('\n')

    print(hamm_dist(seqs))


if __name__ =='__main__':
	main()