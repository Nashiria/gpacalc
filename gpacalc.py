f = open("gpa.txt", "r")
notes=["AA","BA","BB","CB","CC","DC","DD","F","P"]
important=[]
def returnharf(harf):
    if harf == "AA":
        return 4
    if harf == "BA":
        return 3.5
    if harf == "BB":
        return 3
    if harf == "CB":
        return 2.5
    if harf == "CC":
        return 2
    if harf == "DC":
        return 1.5
    if harf == "DD":
        return 1
    if harf == "FD":
        return 0.5
    if harf == "F":
        return 0
    if harf == "P":
        return 0
def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)
for line in f:
    if any(ext in line for ext in notes) and "Status" not in line and "Semester" not in line:
        important.append(line.split())
dersler=[]
for element in important:
    firstdigit=False
    noteon=False
    if hasNumbers(element[0])==False:
        element[0]=element[0]+element[1]
    element.remove(element[1])
    ders=element[0]
    while(element[0] not in notes):
        element.remove(element[0])
    note=element[0]
    kredi=element[1]
    dersler.append([ders,note,kredi])
derslerdict={}
for giris in dersler:
    ders=giris[0]
    note=giris[1]
    kredi=giris[2]
    if ders not in derslerdict:
        derslerdict[ders]={
            "not":note,
            "kredi":kredi
        }
    else:
        if derslerdict[ders]["not"]=="F" and note!="F":
            derslerdict[ders]["not"]==note
print("Dersler:")
print()
def gpahesap():
    toplamkredi=0
    toplamnot=0
    for ders in derslerdict:
        note=returnharf(derslerdict[ders]["not"])
        kredi=int(derslerdict[ders]["kredi"])
        print(ders,derslerdict[ders]["not"],derslerdict[ders]["kredi"])
        if derslerdict[ders]["not"]!="P":
            toplamnot+=note*kredi
            toplamkredi+=kredi
    return toplamnot/toplamkredi
gpa=gpahesap()
print()
print("GPA:",str(gpa)[:4])
