l=int(raw_input())
n=int(raw_input())

for i in range(n):
    w,h= map(int , raw_input().split())
    if w < l or h < l :
        print "UPLOAD ANOTHER"
    elif w ==  h :
        print "ACCEPTED"
    else : 
        print "CROP IT"