Score=[15,25,123,145,87,98,789,985,795,987,952,655]
#We have to find highest number by using loop (else we can use max())

max_scr=0
for value in Score:
    if(value>max_scr):
        max_scr=value

print (f"Maximum Value {max_scr}")
