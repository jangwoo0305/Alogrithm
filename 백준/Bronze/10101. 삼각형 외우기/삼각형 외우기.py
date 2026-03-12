def find_Rec(Rec):
    if Rec[0]==Rec[1]==Rec[2]==60:
        return "Equilateral"
    elif Rec[0]+Rec[1]+Rec[2]==180 and (Rec[0]==Rec[1] or Rec[1]==Rec[2] or Rec[0]==Rec[2]):
        return "Isosceles"
    elif Rec[0]+Rec[1]+Rec[2]==180 and (Rec[0]!=Rec[1] or Rec[1]!=Rec[2] or Rec[0]!=Rec[2]):
        return "Scalene"
    else:
        return "Error"

if __name__ == "__main__":

    Rec= []

    for _ in range(3):
        N = int(input())
        Rec.append(N)

    print(find_Rec(Rec))