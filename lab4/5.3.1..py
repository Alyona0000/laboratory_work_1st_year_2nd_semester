from Rational import Rational

def Distribution(file_name):
    d=open(file_name) 
    
    for l in d:
            print(l)
            l = l.split()
            m = l[0]
            i = 1
            while  i < len(l): #перетворення рядка у список
                b = l[i]
                q = l[i + 1]
                m = Rational(m)
                q = Rational(q)

                if b == "+":
                    r = m + q
                elif b == "-":
                    r = m - q
                elif b == "*":
                    r = m * q
                elif b== "/":
                    r = m / q
                
                print(f"{m} {b} {q} = {r}")
                m = r
                i = i + 2

    print("***")
    

p = Rational("4/3")

print(f"p() = {p()}")
print(f"p[n] = {p["n"]}")
print(f"p[d] = {p["d"]}")
Distribution("input01 (1).txt")
