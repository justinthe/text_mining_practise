from sentistrength import sentistrength as ss

senti = ss.init()
#print(senti.main("film aladdin bagus juga ternyata"))

filename = open('txt_mine.txt', 'r')
fcontent = filename.readlines()
filename.close()
    
lst = []
for t in fcontent:
	lst.append(senti.main(t))


for x in lst:
	# x[1] = text
	# x[2] = max positive
	# x[3] = max negative
	# x[4] = result
	print(x[3])