def fib(n, k):
    if n <= 1:
        return 1
    else:
        return fib(n-1, k) + fib(n-2, k) * k

def main():
    with open('C:/Users/Owner/Desktop/rosalind_fib.txt', 'r') as f:
        n, k = [int(i) for i in f.read().strip().split(' ')]

    print(fib(n-1, k))
    
        
if __name__ == '__main__':
	main()