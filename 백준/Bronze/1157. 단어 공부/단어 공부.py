def count_alpha(N):
    N = N.upper()
    alpha_dict = {}

    for ch in N:
        if ch in alpha_dict:
            alpha_dict[ch] += 1
        else:
            alpha_dict[ch] = 1

    max_alpha = max(alpha_dict.values())
    
    max_chars = []
    for k,v in alpha_dict.items():
        if v == max_alpha:
            max_chars.append(k)
            
    if len(max_chars) > 1:
        print("?")
    else:
        print(max_chars[0])


if __name__ == "__main__":
    N = input()
    count_alpha(N)

