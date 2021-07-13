num = int(input("adad movred nazar ra vared konid:\n"))
amaliat = 0
for i in range(1, num+1):
    if num%i == 0:
        amaliat+=1

if amaliat==2:
    print("adad aval ast")
else:
    print("adad aval nist")
