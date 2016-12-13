rawfile = ("C:\\Users\\Daniel\\Desktop\\python\\SchoolDayProject\\failedattempts.txt")

# Progression Methods / Rooms
def wakeUp():	
	# Booleans
	global outOfBed
	global bedMade
	global doorOpen
	global dressed
	global eaten
	global showered

	outOfBed = False
	bedMade = False
	doorOpen = True
	dressed = False
	eaten = False
	showered = False
	
	print "[BE SURE TO ONLY TYPE IN LOWERCASE LETTERS]\n"
	
	print "BRRRRRRRRRRRIIIING!!!"
	print "You groggily slap your alarm clock until it stops making noise."
	print "Light hurts and your joints groan. You rub the sleep out of your eyes."
	print "You sit in your bed, still under the covers, and heave a giant sigh."
	print "It's a fucking school day."
	
	while True:
		file = open(rawfile, 'a')
		
		print ""
		next = raw_input("> ")
		print ""
		
		if next == "quit game":
			quit()
		
		elif "sleep" in next:
			print "You can't go back to sleep! You have a test today!"
			
		elif "fuck" in next:
			"That's inappropriate."			
	
		elif "out of bed" in next:
			if outOfBed == False:
				outOfBed = True
				print "You kick your covers off and roll off your bed onto the floor."
				print "Rising slowly, you take a look at your mess of covers and sigh again."
			else:
				print "You already got out of bed, idiot!"
		
		elif next == "get up later":
			print "You can't go back to bed! You have a test today!"
		
		elif "get up" in next:
			if outOfBed == False:
				outOfBed = True
				print "You kick your covers off and roll off your bed onto the floor."
				print "Rising slowly, you take a look at your mess of covers and sigh again."
			else:
				print "You already got out of bed, idiot!"		
			
		elif "shower" in next:
			if showered == False:
				showered = True
				print "You go to the bathroom and take a quick shower. Putting your underwear back on, you head back to your room."
			
			else: 
				print "You don't need two showers. I appreciate your enthusiasm, though."
			
		elif "make bed" in next:
			if outOfBed == True:
				if bedMade == False:
					bedMade = True
					print "You realize your mom will probably be mad at you if you leave the covers like this."
					print "Sighing, you make your bed look nice, even though no one will see it anyway."
				
				else:
					print "You already made your bed!"
			else:
				print "You can't make your bed while you're still in it, dummy!"
		
		elif next == "eat breakfast":
			if eaten == False:
				eaten = True
				print "You grab a half eaten granola bar under your bed."
				print "It's probably still good. You shove it down your throat."
				
			else:
				print "You've already eaten!"
		
		elif "look around" in next:
			print "You look around at your mess of a room."
			print "In the corner of the room lies your desk and computer, where you spend your free time."
			print "In the other corner lies your closet, full of warm clothes for the winter."
			
			if doorOpen == True:
				print "The door to your room is open wide. Your mom must have peeked in on you during the night."
			
			else:
				print "Your door is closed. At least you have privacy."
		
		elif "close door" in next:
			if outOfBed == True:
				if doorOpen == True:
					doorOpen = False
					print "You close the door to your room. Now no one will hear you scream."
			
				else:
					print "You already closed your door, silly!"
					
			else:
				print "You try to close your door with force powers from your bed. After a few seconds, you give up."
		
		elif "drink" in next:
			print "You don't have a cup!"
			
		elif "kill" in next:
			print "You lack the proper tools."
			
		elif "cut" in next:
			print "You lack the proper tools."
			
		elif "eat" in next:
			print "You don't have a plate!"
			
		elif "wake up" in next:
			print "You're already awake!"
			
		elif "screw you" in next:
			print "That's not very nice."
			
		elif "pls" in next:
			print "No."
			
		elif "please" in next:
			print "No."
			
		elif "buy a tv" in next:
			print "You don't have any money."
		
		elif "tv" in next:
			print "You don't have a TV."
			
		elif "turn on light" in next:
			print "There's no point."
			
		elif "turn off light" in next:
			print "It's already off."
			
		elif "explode" in next:
			print "You don't have any explosives."
			
		elif "allahu" in next:
			print "Bush did 9/11."
			
		elif "youtube" in next:
			print "There's no time! You have to get to school!"
			
		elif "socks" in next:
			print "You don't believe in socks."
		
		elif "take off underwear" in next:
			print "The goal here is to put on more clothes, skippy."
			
		elif "take off clothes" in next:
			print "The goal here is to put clothes on dude."
			
		elif "strip" in next:
			print "You don't have a pole."
		
		elif "lay down" in next:
			print "You can't lay back down, dude. You'll be late for school."
			
		elif "upstairs" in next:
			print "You don't have an upstairs, and I don't think your mom would appreciate you going on the roof."
			
		elif "downstairs" in next:
			print "The basement is your mom's special area. You can't go there."
			
		elif "dad" in next:
			print "He's in Argentina."
			
		elif "cloth yourself" in next:
			if outOfBed == True:
				dressed = True
				print "You pull on your clothes for the day. Jeans, Sneakers and a T-Shirt. Classic."
				
			else:
				print "Your clothes are in your closet. You can't reach them from here."			
			
		elif "to bed" in next:
			print "You can't go back to bed, silly."
			
		elif next == "well":
			print "Well, what?"
			
		elif next == "stop":
			print "Hammertime."
			
		elif "clear" in next:
			print "What are you even talking about? Are you okay?"
			
		elif next == "no":
			print ":("
			
		elif next == "what":
			print "What?"
			
		elif "get dressed" in next:
			if outOfBed == True:
				dressed = True
				print "You pull on your clothes for the day. Jeans, Sneakers and a T-Shirt. Classic."
				
			else:
				print "Your clothes are in your closet. You can't reach them from here."
			
		elif "dress" in next:
			if outOfBed == True:
				dressed = True
				print "You pull on your clothes for the day. Jeans, Sneakers and a T-Shirt. Classic."
				
			else:
				print "Your clothes are in your closet. You can't reach them from here."

		elif "put on clothes" in next:
			if outOfBed == True:
				dressed = True
				print "You pull on your clothes for the day. Jeans, Sneakers and a T-Shirt. Classic."
				
			else:
				print "Your clothes are in your closet. You can't reach them from here."	
		
		elif "shoes" in next:
			if dressed == True:
				print "Your shoes are firmly on your feet."
				
			else:
				print "You should probably put on pants first."
				
		elif "put on" in next:
			if outOfBed == True:
				dressed = True
				print "You pull on your clothes for the day. Jeans, Sneakers and a T-Shirt. Classic."
				
			else:
				print "Your clothes are in your closet. You can't reach them from here."	
			
		elif "i don't know" in next:
			print "Well you better figure it out then!"
			
		elif "i dont know" in next:
			print "Well you better figure it out then!"

		elif "idk" in next:
			print "Well you better figure it out then!"			
			
		elif "masturbate" in next:
			print "Now is not the time for that. Gross."
			
		elif "wank" in next:
			print "Ew. No."
			
		elif "creepy" in next:
			print "I know right?"
					
		elif "sex" in next:
			print "You don't have a partner. No one loves you."
			
		elif "cry" in next:
			print "You weep for the loss of a good night's sleep. Wiping the tears away, you sigh again."
			
		elif "read" in next:
			print "You don't have anything to read."
			
		elif next == "go":
			print "Go where?"
			
		elif "desk" in next:
			if outOfBed == True:
				print "You walk over to your desk."
				print "On the surface is your computer, a couple cans of soda and some unfinished dinner from last night."
			
			else:
				print "You're in bed, silly. You can't do that."
		
		elif "computer" in next:
			if outOfBed == True:
				print "You can't use your computer right now. You have to get to school."
			
			else:
				print "You can't reach your computer from here."
			
		elif "closet" in next:
			if outOfBed == True:
				print "You walk over to your closet and open it."
				print "Looking inside, you see a mix of T-shirts, jeans and sweatshirts."
				print "You close your closet, sighing."
				
			else:
				print "You can't do that from here."
			
		elif "work out" in next:
			if outOfBed == True:
				print "You drop to the floor and bust out ten push-ups. You get up, sweating now."
			
			else:
				print "You can't do that while you're in bed."
			
		elif "sit" in next:
			if outOfBed == True:
				print "You sit on the ground, cross-legged. After a moment, you stand back up. That was pointless."
			
			else:
				print "You're in your bed, silly."
			
		elif "draw" in next:
			print "You draw a shitty picture."
			print "  O"
			print " /|\\"
			print " / \\"
			
		elif "class" in next:
			if outOfBed == True:
				if dressed == True:
					print "You go ask your mom to drive you to school."
					schoolEntrance()
					
				else:
					print "You're not ready for school yet! Why would you talk to your mom?"
					
			else:
				print "You're not even out of bed yet!"				
		
		elif "mom" in next:
			if outOfBed == True:
				if dressed == True:
					print "You go ask your mom to drive you to school."
					schoolEntrance()
					
				else:
					print "You're not ready for school yet! Why would you talk to your mom?"
					
			else:
				print "You're not even out of bed yet!"	
			
		elif "school" in next:
			if outOfBed == True:
				if dressed == True:
					print "You go ask your mom to drive you to school."
					schoolEntrance()
					
				else:
					print "You're not ready for school yet!"
					
			else:
				print "You're not even out of bed yet!"
				
		elif "roll around" in next:
			if outOfBed == True:
				print "You stop, drop and roll before getting back up. Why did you do that?"
				
			else:
				print "You roll around, mumbling. Hopefully no one sees this."
		
		elif "why not" in next:
			print "Because."
		
		elif "leave" in next:
			if outOfBed == True:
				if dressed == True:
					print "You go ask your mom to drive you to school."
					schoolEntrance()
					
				else:
					print "You're not ready for school yet!"
					
			else:
				print "You're not even out of bed yet!"		
		
		elif "call" in next:
			print "You take out your cellphone and begin to dial the number, then sigh."
			print "They probably don't want to talk to you. You put your phone away."
		
		elif "plate" in next:
			print "You head to the kitchen, but once you get there you forget what you were doing."
			print "You head back to your room, scratching your head."

		elif "pee" in next:
				print "You rush into the bathroom and empty your bladder."
				
		elif "bathroom" in next:
				print "You rush into the bathroom and empty yourself"	
				
		elif "poop" in next:
				print "You rush into the bathroom and empty yourself"		
				
		elif "poo" in next:
				print "You rush into the bathroom and empty yourself"			

		elif "poopy" in next:
				print "You rush into the bathroom and empty yourself"					
	
		else:
			print "I'm sorry, I didn't understand that."
			file.write("\n[wakeup] " + next)			
					
def schoolEntrance():
	#Booleans
	global inFirstClass
	global atEntrance
	global gotMathBook
	
	inFirstClass = False
	atEntrance = True
	gotMathBook = False
	
	#Intro
	print "\n--------------------------------\n"
	if bedMade == True:
		momsMoodSentence = "It's a nice drive, and you have some pleasant conversation with your mother."
	else:
		momsMoodSentence = "Your mom seems to be in a terrible mood and it's a very awkward drive."
	
	print momsMoodSentence
	print "Once inside the double doors, you pause to look around."
	print "You're in a large hallway, leading to another set of double doors."
	print "To the right is the main office. If you kept walking, you could head to your first class."
	print "Off in one of the corners of the room is Cindy with a group of her friends."
	print "Taking a second to look at her, entranced, she looks back. You quickly look away, embarrassed."
	
	# ------------------------------ 
	# Choices
	while True:
		file = open(rawfile, 'a')
	
		print ""
		next = raw_input("> ")
		print ""
	
		if "to class" in next:
			firstClass()
			
		if "office" in next:
			print "You'd probably find a way to get in trouble. Better stay here."
			
		elif "locker" in next:
			print "There's nothing in your locker. Why would you want to go there?"
			
		elif "bathroom" in next:
			print "You go to the bathroom, take twenty minutes, then come back."
			
		elif "to cindy" in next:
			print "You start to walk towards her, but chicken out and pretend you dropped your phone, stooping to \"pick it up\""
		
		elif next == "quit game":
			quit()
			
		elif "ditch" in next:
			print "You can't ditch class! You'd never get away with it!"
			
		elif "keep staring" in next:
			print "Building up the courage, you stare at Cindy intensely for a few minutes."
			
		elif "look back at her" in next:
			print "You glance at Cindy, then away again."
			
		elif "jizz" in next:
			print "Gross."
			
		elif "sex" in next:
			print "Not very likely."
			
		elif "take a picture" in next:
			print "Your phone can't take pictures."
			
		elif "go to school" in next:
			print "You're already here, dummy."
			
		elif next == "school":
			print "What about school?"
			
		elif "look around" in next:
			print "You're in a large hallway, leading to another set of double doors."
			print "To the right is the main office. If you kept walking, you could head to your first class."
			print "Cindy is in the corner and you are alone."
			
		elif "screw you" in next:
			print "That's not nice."
			
		elif "fuck" in next:
			print "That's inappropriate."
			
		elif "cough" in next:
			print "You cough loudly, attracting stares."
			
		elif "sneeze" in next:
			print "If you could sneeze on command, you would be rich. Unfortunately, you can't."
			
		elif "sit" in next:
			print "You sit on the floor for a moment before standing back up. Pointless."
			
		elif "yell" in next:
			print "You screech as loudly as you can. Everyone looks at you before whispering to their friends. Why would you do that?"
		
		elif "shoot" in next:
			print "You lack the proper tools."
			
		elif "ditch class" in next:
			print "You can't ditch class! You mom would kill you!"
			
		elif "take off glasses" in next:
			print "You're not wearing any glasses..."
			
		elif "cry" in next:
			print "You try to cry, thinking it would be funny, but then you remember you don't have any friends to make laugh, so you stop trying."
			
		elif "screw you" in next:
			print "Well that's just not nice."
			
		elif "reflection" in next:
			print "There are no mirrors or windows in here. It's almost like a prison."
			
		elif "check out self" in next:
			print "You look down at yourself. You look okay I guess."
		
		elif "class" in next:
			print "What about class?"
			
		elif "throw up" in next:
			print "You try to throw up, but then remember you're at school. Not the time. Not the time."
			
		elif "puke" in next:
			print "You try to puke, but then remember you're at school. Not the time. Not the time."			

		elif "kill" in next:
			print "You lack the proper tools."
			
		elif "take off clothes" in next:
			print "That's inappropriate. You can't do that."
			
		elif "masturbate" in next:
			print "You start to unbutton your pants, then stop. Why the hell would you do that here?"
			
		elif "work out" in next:
			print "You tense to drop down and do pushups, but chicken out at the last second. You're in public after all."
			
		elif "walk around" in next:
			print "You wander aimlessly around the room and people look at you funny."
			
		elif "armpit" in next:
			if showered == True:
				print "You don't smell anything. Must be a good sign."
			else:
				print "You smell rancid. You really regret not showering."
		
		else:
			print "I'm sorry, I didn't understand that."
			file.write("\n[schoolEntrance] " + next)				
	
def firstClass():
	# Booleans
	global gotPencil
	
	gotPencil = False
	
	# Intro
	print "You walk to your Algebra II class, keeping your head down along the way."
	print "You have an exercise on the board you need to do before you leave."
		
	# Where You Are
	atEntrance = False
	inFirstClass = True	
	
	# Choices
	while True:
		file = open(rawfile, 'a')
	
		print ""
		next = raw_input("> ")
		print ""
			
		if "office" in next:
			print "You'd probably find a way to get in trouble. Better stay here."
			
		elif "locker" in next:
			print "There's nothing in your locker. Why would you want to go there?"
			
		elif "to next class" in next:
			print "You can't do that until you finish the exercise!"
			
		elif "go" in next:
			print "Go where?"
			
		elif "take pencil" in next:
			print "From where?"
			
		elif "bathroom" in next:
			print "You go to the bathroom, take twenty minutes, then come back."
		
		elif "cry" in next:
			print "You should probably not cry in class again."
			
		elif "well crap" in next:
			print "Sucks, don't it?"
			
		elif "take a picture" in next:
			print "Your phone can't take pictures."
			
		elif "fart" in next:
			print "You rip one so hard you black out for a minute. You hope it was silent."
			
		elif "sneeze" in next:
			print "You sneeze. No one says bless you."
			
		elif "burp" in next:
			print "Careful now, you don't want to attract TOO much attention."
			
		elif "work out" in next:
			print "This isn't the time to get buff. We have math to do."
			
		elif "get dressed" in next:
			print "Are you high? You're already dressed."
			
		elif "look down" in next:
			print "You look down to make sure you're wearing pants. Yup."

		elif "go to class" in next:
			print "You're already in a class..."
			
		elif "look up" in next:
			print "You forget whether or not you're in school. Looking up, you see a ceiling. Yup, this is school alright."
		
		elif "look for pencil" in next:
			print "Everyone seems to be holding a pencil, and there's a bunch of them on your teacher's desk."
			print "Unfortunately, none are on the floor."
			
		elif "find pencil" in next:
			print "Everyone seems to be holding a pencil, and there's a bunch of them on your teacher's desk."
			print "Unfortunately, none are on the floor."
			
		elif "from teacher's desk" in next:
			gotPencil = True
			print "You quickly get up an take a pencil from your teacher's desk."
		
		elif "get pencil" in next:
			print "How?"
			
		elif "borrow pencil" in next:
			print "No one wants to lend you one."\
			
		elif "masturbate" in next:
			print "It'd be very difficult to pull that off. Better not."
			
		elif "sleep" in next:
			print "You put your head down to catch a few Z's, but almost immediately your teacher raps your desk with a ruler."
			print "Everyone laughs and you turn all red. Way to go."
			
		elif "take from teacher" in next:
			gotPencil = True
			print "You sneak up to your teacher's desk, grabbing a pencil and sitting back down."
			print "Thinking about it, you probably weren't that sneaky. Oops."
			
		elif "stand up" in next:
			print "You stand up, drawing attention, then sit back down embarrassed. Why did you do that?"
			
		elif "go home" in next:
			print "Yeah, right. Like your mom would let you do that."
			
		elif "talk to neighbor" in next:
			print "No one wants to talk to you."
			
		elif "cindy" in next:
			print "She's not in this class! And you can't leave!"
			
		elif "ask someone" in next:
			print "You can't build up the courage."
			
		elif "fuck" in next:
			print "That's inappropriate."
			
		elif "whip it out" in next:
			print "You begin to unbutton your pants, then stop. Why would you do that?"
			
		elif "copy answers" in next:
			print "You'd get caught! Better not!"
			
		elif "ask teacher" in next:
			gotPencil = True
			print "Instead, of asking, you grab one from his desk really quick."
			
		elif "from teacher" in next:
			gotPencil = True
			print "Instead of asking, you just decide to take one from his desk."
			
		elif "ask friend" in next:
			print "You don't have any friends!"
		
		elif "from friend" in next:
			print "You don't have any friends!"
		
		elif "ask neighbor" in next:
			print "They'd probably say no."
			
		elif "from neighbor" in next:
			print "They'd probably say no."	
			
		elif "ask classmate" in next:
			print "They'd probably say no."
			
		elif "from classmate" in next:
			print "They'd probably say no."				
			
		elif "ask student" in next:
			print "They'd probably say no."
			
		elif "from student" in next:			
			print "They'd probably say no."
			
		elif "get a pencil" in next:
			print "From where?"
			
		elif "talk to" in next:
			print "You're too afraid."
			
		elif "steal" in next:
			print "You don't have the nerve."
			
		elif "draw" in next:
			print "You attempt to draw something, and the result is disastrous."
		
		elif "look at exercise" in next:
			print "It's a collection of math problems. What did you expect?"
		
		elif "do exercise" in next:
			if gotPencil == False:
				print "You reach into your backpack to get a pencil, only to find you don't have any! Crap!"
			
			else:
				print "You complete most of the questions, though you especially have trouble with the last one."
				print " __________"
				print "|          |"
				print "| **MATH** |"
				print "|          |"
				print "|  2 / 2   |"
				print "|          |"
				print "|          |"			
				print "|          |"		
				print "|          |"						
				print "\nWhat could the answer be?"
				
				answer = raw_input("\nAnswer: ")
				print ""
				
				if "1" in answer:
					print "That's it! You jot down your answer."
					print " __________"
					print "|          |"
					print "|          |"
					print "|   Juan   |"
					print "|          |"
					print "|          |"
					print "|          |"		
					print "|          |"	
					print "|          |"
					print "You walk up to your teacher's desk and turn in the exercise."
					print "After waiting an insanely long time for the bell to ring, you decide head to your next class, Spanish."
					secondClass()		
					
				elif "one" in answer:
					print "That's it! You jot down your answer."
					print " __________"
					print "|          |"
					print "|          |"
					print "|   Juan   |"
					print "|          |"
					print "|          |"
					print "|          |"		
					print "|          |"	
					print "|          |"
					print "You walk up to your teacher's desk and turn in the exercise."
					print "After waiting an insanely long time for the bell to ring, you decide head to your next class, Spanish."
					secondClass()					
					
					
				else:
					print "You doodle on the paper, unable to come up with an answer."
					print "Whatever, it doesn't matter. You walk up to your teacher's desk and turn in the exercise."
					print "After waiting an insanely long time for the bell to ring, you decide head to your next class, Spanish."
					secondClass()
			
		elif "complete exercise" in next:
			if gotPencil == False:
				print "You reach into your backpack to get a pencil, only to find you don't have any! Crap!"
			
			else:
				print "You complete most of the questions, though you especially have trouble with the last one."
				print " _________"
				print "|         |"
				print "|         |"
				print "|  2 / 2  |"
				print "|         |"
				print "|         |"
				print "|         |"			
				print "\nWhat could the answer be?"
				
				answer = raw_input("\nAnswer: ")
				print ""
				
				if 1 in next:
					print "That's it! You jot down your answer."
					print " __________"
					print "|          |"
					print "|          |"
					print "|   Juan   |"
					print "|          |"
					print "|          |"
					print "|          |"		
					print "|          |"	
					
				elif one in next:
					print "That's it! You jot down your answer."
					print " __________"
					print "|          |"
					print "|          |"
					print "|   Juan   |"
					print "|          |"
					print "|          |"
					print "|          |"		
					print "|          |"	
					
				else:
					print "You doodle on the paper, unable to come up with an answer."
					print "Whatever, it doesn't matter. You walk up to your teacher's desk and turn in the exercise."
					print "After waiting an insanely long time for the bell to ring, you decide head to your next class, Spanish."
					secondClass()			
		elif next == "quit game":
			quit()	
			
		else:
			print "I'm sorry, I didn't understand that."
			file.write("\n[firstClass] " + next)
	
def secondClass():
	print "\n--------------------------------\n"
	print "You walk into your spanish class, dreading every step. This is your least favorite class."
	print "Seriously, you don't understand a word of spanish. It all just sounds like gibberish to you."
	print "Sitting down, you prepare for an onslaught of embarrassment."
	print "The teacher, as always, decides to single you out and ask you a question. In Spanish."
		
	print "\n\"sodfjia asdjf  awbdsh asd fwsa diaufhoiwe as mdkf?\""
	
	print ""
	raw_input("> ")
	print ""	
		
	print "The class stares at you for a second, then, in unison, laughs."
	print "Even the teacher is laughing. God you hate this class."
	print "\"dsafuhs a sdf asuhf dsud!\", she exclaims, and the class laughs even harder."
	print "You try to keep your head down and not talk to anyone until the class is over."
		
	print "\nWhen the bell rings, you're the first one to leave. You head for the lunch room, your spirits crushed."
	
	print "\n-----------------------\n"
	
	thirdClass()
		
def thirdClass():
	print "After a disappointing lunch, you walk into your third period, Geography.\n"
	print "Taking a seat, you sigh, wishing you were home already. All this sitting is really getting boring."
	print "You look up as the teacher begins his lecture on the importance of goat milk to the natives of wherever."
	print "The lights are off, and you're finding it especially hard to stay awake."
	
	while True:
		file = open(rawfile, 'a')
		
		print ""
		next = raw_input("> ")
		print ""
	
		if "office" in next:
			print "You'd probably find a way to get in trouble. Better stay here."
			
		elif "locker" in next:
			print "There's nothing in your locker. Why would you want to go there?"
			
		elif "bathroom" in next:
			print "You go to the bathroom, take twenty minutes, then come back."	
			
		elif "quit game" in next:
			quit()
	
		elif "sleep" in next:
			print "You decide to rest your head and sleep through the lecture. What's the worst that could happen?"
			print "Your nap is uninterrupted by all but the bell. Rubbing your eyes, you grab your bag and make your way to the last class of the day: Art."
			
			print "\n-----------------------\n"
				
			fourthClass()
			
		else:
			print "I'm sorry, I didn't understand that."
			file.write("\n[thirdClass] " + next)	
	
def fourthClass():
	print "You saunter into the art room. This just happens to be your favorite class!"
	print "Sitting down, you pull out a pencil and a paper."
	print "Your teacher explains that all you have to do today is draw a picture."
	print "She says that since you have all period, she expects it to be good."
	
	print "\nWhat do you want to draw a picture of?"
	
	while True:
		file = open(rawfile, 'a')
		
		print ""
		next = raw_input("> ")
		print ""

		if "man" in next:
			print "You take your time and very carefully make your drawing. When it's complete, you're quite proud.\n"
			print "  O"
			print " /|\\"
			print " / \\"
			endArt()
			
		elif "boy" in next:
			print "You take your time and very carefully make your drawing. When it's complete, you're quite proud.\n"
			print "  O"
			print " /|\\"
			print " / \\"
			endArt()			
			
		elif "guy" in next:
			print "You take your time and very carefully make your drawing. When it's complete, you're quite proud.\n"
			print "  O"
			print " /|\\"
			print " / \\"
			endArt()			
			
		elif "woman" in next:
			print "You take your time and very carefully make your drawing. When it's complete, you're quite proud.\n"
			print "   O"
			print " /O-O\\"
			print "  / \\"
			endArt()	

		elif "girl" in next:
			print "You take your time and very carefully make your drawing. When it's complete, you're quite proud.\n"			
			print "   O"
			print " /O-O\\"
			print "  / \\"
			endArt()			

		elif "gal" in next:
			print "You take your time and very carefully make your drawing. When it's complete, you're quite proud.\n"
			print "   O"
			print " /O-O\\"
			print "  / \\"
			endArt()	
			
		elif "penis" in next:
			print "You take your time and very carefully make your drawing. When it's complete, you're quite proud.\n"
			print " ^"
			print " |"
			print "O O"
			endArt()
			
		elif "dick" in next:
			print "You take your time and very carefully make your drawing. When it's complete, you're quite proud.\n"			
			print " ^"
			print " |"
			print "O O"			
			endArt()
			
		elif "boob" in next:
			print "You take your time and very carefully make your drawing. When it's complete, you're quite proud.\n"					
			print "( . ) ( . )"
			endArt()
			
		elif "tit" in next:
			print "You take your time and very carefully make your drawing. When it's complete, you're quite proud.\n"					
			print "( . ) ( . )"
			endArt()			
			
		elif "nothing" in next:
			print "You're too lazy to draw anything, so you don't."
			
		elif "quit game" in next:
			quit()
		
		else:
			print "That's dumb. Choose something else."
			file.write("\n[fourthClass] " + next)		

def endArt():
	print "\nThe bell rings, and you wait for your teacher to come around and grade you."
	print "Coming to you, she frowns."
	print "\"What the fuck is that?\", she asks, marking a big F on your paper."
	print "Depressed now, you slowly go to the pickup lot so you can go home."
	homeSweetHome()

def homeSweetHome():
	print "\n--------------------------------\n"
	
	print "You find your mom waiting for you, smiling."
	print "You hop in the car and don't say a word the whole drive."
	print "Once in your room, you sigh. What a terrible day."
	
	print "\nWhat do you want to do now?"
	
	print ""
	next = raw_input("> ")
	print ""
	
	if "sleep" in next:
		print "Hell yeah! You throw yourself on your bed and get a well deserved rest."
		
	elif "nap" in next:
		print "Hell yeah! You throw yourself on your bed and get a well deserved rest."
		
	elif "lay down" in next:
		print "Hell yeah! You throw yourself on your bed and get a well deserved rest."
	
	elif "rest" in next:
		print "Hell yeah! You throw yourself on your bed and get a well deserved rest."
	
	elif "bed" in next:
		print "Hell yeah! You throw yourself on your bed and get a well deserved rest."
	
	else:
		print "Fuck that. You throw yourself on your bed and get a well deserved rest."
	
	print "\n--------------------------------\n"
	print "\n\n\nThe End! Thank you very much for playing!"
	print "Anything you were unable to do has been saved and will be included soon."
	print "Press Enter to exit the game, or type \"replay\" to play again :)"
	
	print ""
	final = raw_input("> ")
	print ""
	
	if final == "replay":
		wakeUp()
		
	else:
		quit()
	
wakeUp()