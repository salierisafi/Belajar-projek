arr = [
        "1-ahmad-python,2008",
        "3-alfin-javascript,2007",
        "4-bayu-python,2008",
        "1-ahmad-python,2008",
        "2-bagas-c,2006",
        "3-alfin-javascript,2007",
        "3-alfin-javascript,2007",
        "5-dimas-csharp,2007"
        ]

arrunik = list(set(arr)) #tidak ada elemen yang sama
print(arrunik)

# tapi urutannya jadi acak, bisa pake list(dict.fromkeys(arr))

arrunik = [] #pake loop
for i in range(len(arr)): 
    #untuk bikin tidak ada elemen yg sama,urutan ambil plng awal
    if arr[i] not in arrunik: #ngecek apakah sebuah elemen ada dalam array :
        arrunik.append(arr[i])
print(arrunik)

splitarr = []
for i in range(len(arrunik)):
    x = arrunik[i].split("-")
    splitarr.append(x)

# urutkan, ini namanya cycling short, pakai looping manual
# kelemahan : tidak boleh ada angka double atau terloncati
temp = [1]
i = 0
while True:
    indikator = int(splitarr[i][0])
    temp2 = splitarr[i]
    splitarr[i] = temp
    temp = temp2
    if str(indikator) == splitarr[indikator-1][0]:
        i+=1
    else:
        i = int(temp2[0])-1
    if i>=len(splitarr): break

arrdict = []
for j in range(len(splitarr)):
    tempdict = {}
    tempdict["no"] = splitarr[j][0]
    tempdict["name"] = splitarr[j][1]
    tempdict["lang"] = splitarr[j][2].split(",")[0] #cara tadi, pake split
    # pake slicing [awal:akhir], cari index "," dalam string, +1 jadikan awal
    #akhir tidak usah diisi, berarti sampai akhir
    tempdict["year"] = splitarr[j][2][splitarr[j][2].index(",")+1:]
    arrdict.append(tempdict)

print(arrdict)



