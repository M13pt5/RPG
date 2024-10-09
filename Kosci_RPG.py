from random import randint
from random import choices

def Rzut():
    Kant = input("Czy chcesz kanować (wartość, prawdopodobieństwo) : ")
    Kant = Kant.rsplit(",")

    if len(Kant) == 2:
        n = int(Kant[0])
        if int(Kant[1]) >= 95:
            output = n
            return output
        else:
            p = int(Kant[1])/100 * 6
            output = choices([1,2,3,4,5,6,n], weights = [1,1,1,1,1,1,p], k=1)
            return output[0]
    else:
        output = randint(1,6)
        return output
    
def Wstaw(ro, Board_1, Board_2):
    tr = True
    while tr:
        try:
            x = int(input("Team: "))
            a = int(input("Kolumna: "))-1
            b = int(input("Wiersz: "))-1
            if x == 1 and a in {0,1,2} and b in {0,1,2} and Board_1[b,a] == "-":
                Board_1[b,a] = ro
                print("Team 1")
                print(Board_1)
                for i in [0,1,2]:
                    if Board_2[i,a] == Board_1[b,a]:
                        Board_2[i,a] = '-'
                print("Team 2")
                print(Board_2)
                tr = False
            
            elif x == 2 and a in {0,1,2} and b in {0,1,2} and Board_2[b,a] == "-":
                Board_2[b,a] = ro
                print("Team 2")
                print(Board_2)
                for i in [0,1,2]:
                    if Board_1[i,a] == Board_2[b,a]:
                        Board_1[i,a] = '-'
                print("Team 1")
                print(Board_1)
                tr = False
            
            else:
                print("Zły numer drużyny/kolumny/wiersza")
        except ValueError:
            print("Zły numer drużyny/kolumny/wiersza")
            
def Wynik(y):
    sum = 0
    z = transpose(y)
    z = z.tolist()
    for i in [0,1,2]:
        for j in [0,1,2]:
            value = z[i][j]
            nr = z[i].count(value) 
            sum = sum + int(value) * nr
    return sum
    
from numpy import array, transpose

def main():
    
    Board_1 = array([["-","-","-"],["-","-","-"],["-","-","-"]])
    Board_2 = array([["-","-","-"],["-","-","-"],["-","-","-"]])

    print("Team 1")
    print(Board_1)

    print("Team 2")
    print(Board_2)

    round = 100
    condition = True

    while condition:
        roll = Rzut() 
        print(roll)
        Wstaw(roll, Board_1, Board_2)
        round = round +1
        if round >=18:
            res_1 = any('-' in sub for sub in Board_1)
            res_2 = any('-' in sub for sub in Board_2)
            if not res_1 and not res_2:
                Wynik(Board_1)
                Wynik(Board_2)
                break

main()
