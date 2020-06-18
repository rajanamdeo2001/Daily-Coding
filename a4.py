
#pattern recogniser(application on for string datatype)


if __name__ == '__main__': 

    txt = input("put your text here :-")

    pat = input("put your pattern here :-")

    search(pat, txt) 

def search(pat, txt): 

    M = len(pat) 

    N = len(txt) 

    for i in range(N - M + 1): 

        j = 0

          

        while(j < M): 

            if (txt[i + j] != pat[j]): 

                break

            j += 1

  

        if (j == M):  

            print("Pattern found at index ", i) 
