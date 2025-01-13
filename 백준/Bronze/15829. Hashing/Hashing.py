
def hash(string):
    hash_sum = 0
    for i,s in enumerate(string):
        s = alphabet.index(s) + 1 # 알파벳의 값, ex) a = 1
        # hash_sum += 뒤의 숫자 * 31 ** 앞의 숫자
        hash_sum += s * (31**i)
    return hash_sum
    


if __name__ == '__main__':
    L = int(input())
    string = input()

    M = 1234567891
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    print(hash(string) % M)

