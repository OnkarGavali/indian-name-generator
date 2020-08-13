import random

#Punjabi
#-----
mainNamePunjabi=["Gagan", "Har", "Bal", "Man", "Nav", "Sukh", "Kush", "Gur", "Karam", "Karan", "Dil", "Dharam", "Param", "Dal", "Jas", "Par", "Dul"]

maleSuffixPunjabi=["jeet", "jyot", "vinder", "preet", "meet"]

femleSuffixPunjabi=["preet", "jeet", "bir"]

unionSuffixPunjabi=maleSuffixPunjabi+femleSuffixPunjabi

def randomPunjabi():
	namePunjabi=random.choice(mainNamePunjabi)+random.choice(unionSuffixPunjabi)
	return namePunjabi
def malePunjabi():
	namePunjabi=random.choice(mainNamePunjabi)+random.choice(maleSuffixPunjabi)
	return namePunjabi
def femalePunjabi():
	namePunjabi=random.choice(mainNamePunjabi)+random.choice(femaleSuffixPunjabi)
	return namePunjabi
#-----

#Marathi
#-----
maleNameMarathi=["Aarav", "Kshitij", "Shantanu", "Onkar", "Aniket", "Atharva", "Prajwal", "Yash", "Abhijeet", "Ganesh", "Sachin", "Prathamesh", "Vaibhav", "Ninad", "Mihir", "Tejas", "Suyash", "Sanket", "Devang", "Darshan", "Soham", "Rohit", "Manish", "Aadesh", "Siddhesh",
"Aakash", "Anmol", "Chaitanya", "Dharmesh", "Gagan", "Gaurav", "Gopal", "Ishan", "Mehul", "Om", "Rahul", "Sandesh", "Tanmay", "Tushar", "Utkarsh",
"Vedang", "Varun", "Vinay", "Vivek", "Yogesh"]

femaleNameMarathi=["Vaishnavi", "Maithili", "Pooja", "Smital", "Shivani", "Veerja", "Shruti", "Aditi", "Manali", "Anuja", "Pranali", "Saloni",
"Aabha", "Aakriti", "Aruni", "Akanksha", "Akshata", "Aboli", "Ankita", "Chaitrali", "Divya", "Dhriti", "Gargi", "Gayatri", "Gauravi", "Gautami", "Isha", "Ishika",
"Kajal", "Kalyani", "Neha", "Nishi", "Tanvi", "Yuti"]

unionNameMarathi=maleNameMarathi+femaleNameMarathi

def randomMarathi():
	nameMarathi=random.choice(unionNameMarathi)
	return nameMarathi
def maleMarathi():
	nameMarathi=random.choice(maleNameMarath)
	return nameMarathi
def femaleMarathi():
	nameMarathi=random.choice(femaleNameMarath)
	return nameMarathi
#-----

#Bengali
#-----
maleNameBengali=["Abhik", "Abhoy", "Achintya", "Arnab", "Benoy", "Bhaskor",
"Bipin", "Daiwik", "Debesh", "Hrishab", "Indroneel", "Palash", "Paritosh", "Shirshendu", "Shubhang",
"Sourav", "Subrata", "Tapan", "Gairik", "Ujjwal"]

femaleNameBengali=["Ankolika", "Arundhati", "Bidisha", "Bibhuti", "Bipasha", "Chaitali", "Debjani", "Debolina", "Drishti", "Durba", "Joyeeta", "Kajol", "Kshamya", "Indrani", "Lotika", "Mishti",
"Naisha", "Pakhi", "Paromita", "Piyali", "Sagarika", "Shorbari", "Shoma", "Sushmita", "Tavishi", "Tvisha", "Yoshita"]

unionNameBengali=maleNameBengali+femaleNameBengali

def randomBengali():
	nameBengali=random.choice(unionNameBengali)
	return nameBengali
def maleBengali():
	nameBengali=random.choice(maleNameBengali)
	return nameBengali
def femaleBengali():
	nameBengali=random.choice(femaleNameBengali)
	return nameBengali
#-----

#Gujarati
#-----
maleNameGujarati=["Dhaval", "Haanish", "Herik", "Jigar", "Jignesh", "Joshil", "Mukund", "Munjal", "Oresh", "Prakat", "Pratul",
"Praful", "Praveen", "Prerit", "Devang", "Pujesh", "Raghubeer", "Sanam", "Yaksh", "Ahem", "Yug", "Yuvan", "Ronak"]

femaleNameGujarati=["Hinal", "Hiral", "Havya", "Jaimini", "Komal", "Jigna", "Raashi", "Kavya", "Nutan", "Pranauthi", "Puruvi",
"Tanishka", "Vaishnavi", "Vanshi", "Vrishti", "Vritika", "Kanchan"]

unionNameGujarati=maleNameGujarati+femaleNameGujarati

def randomGujarati():
	nameGujarati=random.choice(unionNameGujarati)
	return nameGujarati
def maleGujarati():
	nameGujarati=random.choice(maleNameGujarati)
	return nameGujarati
def femaleGujarati():
	nameGujarati=random.choice(femaleNameGujarati)
	return nameGujarati
#-----