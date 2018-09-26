import random
import  pickle
import sys
import signal, os




class User:
	name=''
	total_coin=0
	

def print_string(a):
	s=''.join(a)
	print str.upper(s)
	

def populate_data ():

	f = "/usr/share/dict/american-english"
	with open(f) as t :
		content = t.read().split('\n')
	t.close()
	l=len(content)
	for i in range(0,l):	
		if '\'' in content[i] or len(content[i]) < 5:
			continue
	 	words.append(content[i])


def validate_user():
	global user
	global userlist
	x=raw_input("Do u have login ID? (y/n)")
        if x == 'y':
        	username= raw_input("Enter your user id:")
        	print "Searching for user"
        	try :
                	pickle_in = open(db,"rb")
	        except(IOError):
        	        pickle_in = open(db,"wb")
                	pickle_in.close()
	                pickle_in = open(db,"rb")
        	while 1:
                	try:
                        	userlist.append(pickle.load(pickle_in))

	                except (EOFError):
        	                break
        	for i in userlist:
                	if username == i.name:
				print "User found"
                        	user=i
                        	break
        	if user.name =='':
                	print "Not a Valid user"
                	sys.exit(0)
	else :
        	x=raw_input("Do u wanna create one?(y/n)" );
	        if x == 'y':
	                user.name= raw_input("name?")
	                user.total_coin =100
        	        pickle.dump(user, open(db, "ab"))
                	#create one
        	else:
                	print "playing as guest, ur data will not be saved"
                	user.name ="guest"
	                user.total_coin = 30








##### pgm starts here
db="/tmp/mine.db"
userlist=[]
words=[]
user=User()
populate_data()
validate_user()
l=len(words)
while user.total_coin > 0:
	
	start=raw_input("Coninue ?(y/n)")
	if start != "y":
		print " COINS LEFT is ",user.total_coin
		print " Thankyou Visit again"
		break
	user.total_coin-=9
	word = list(words[random.randint(0,l)])
	temp=list(word)
	random.shuffle(temp)

	print_string(word)
	l = len(word)
	if len(word) > 7:
		chances =7
	else:
		chances = 5

	tries = 0
	h1=random.randint(0,l);
#	h2=random.randint(0,l);
	print_string(temp)
	points=0.0
	
	hint=[]
	for i in range (0,l):
		if i==h1 :
			hint.append(word[i])
		else:
			hint.append('.')
	print_string(hint)
	coin_multiple=1;
	while chances != tries:
		try :
			h1=int(raw_input("which index u want to unlock: "))
			if h1 >= l:
				print "invalid index "
				continue
		except(ValueError):
			print "Invalid index"
			continue
		hint[h1]=word[h1]
		user.total_coin -=coin_multiple
		coin_multiple*=2
		print "hint is:" 
		print_string(hint)

		answer=raw_input("please input the answer:")
		answer= str.upper(answer)
		tmp = ''.join(word)
		tmp=str.upper(tmp)
		if answer == tmp :#''.join(word):
			print "crct answer"
			user.total_coin +=20
			break
		else:
			print "answer incrct"
			tries += 1
	
	if chances == tries:
		print "Maximum chances used , the answer is *****"
		print_string(word)
		print "****"
	c=0
	for i in userlist:
		if c==0:
			t= open(db, "wb")
			c=1
			pickle.dump(i, t)
		else:
			fil= open(db, "wa")
			pickle.dump(i, t)
	t.close()
	print " u got ",user.total_coin," coins"
	print "Continuing to next word"

