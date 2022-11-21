this = input()
this_nxt=input()
this_chr=this_nxt[-1]
c = 0
for i in this:
	if i == this_chr:
		c = c + 1
print (c)
