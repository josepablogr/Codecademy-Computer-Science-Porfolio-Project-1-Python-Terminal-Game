#MODULES
from art import *
from random import *
from termcolor import colored

#GAME TITLE
tprint("World Cup Trivia")

#GREETING MESSAGE
print("Welcome to the most exciting FIFA World Cup Trivia Game! There will be multiple-choice questions about the biggest sports event. The first player to answer 5 questions correctly wins the game. Please enter the players' names.")

#INPUT PLAYERS NAMES
p1_name = input("P1 Name: ")
p2_name = input("P2 Name: ")

#DICTIONARY WITH TRIVIA QUESTIONS AND ANSWERS
dic_qa = {
    "Where was the very first World Cup held?\n a) Italy\n b) Uruguay\n c) Brazil\n d) West Germany":"b",
    "What was the fastest goal in World Cup history?\n a) 14.7 seconds\n b) 6.2 seconds\n c) 18.3 seconds\n d) 10.8 seconds":"d",
    "Who was the first player to score at five World Cup editions?\n a) Pelé\n b) Marta\n c) Lothar Matthäus\n d) Ronaldo": "b",
    "What did the Iranian national team lose a week before their 2018 World Cup match?\n a) Their shoes\n b) Their coach\n c) Their whole team\n d) Their passports": "a",
    "What was the longest wait between FIFA World Cup tournaments?\n a) 8 years\n b) 4 years\n c) 16 years\n d) 12 years": "d",
    "What was the first host country to be eliminated in the first round of World Cup play?\n a) Mexico\n b) Uruguay\n c) South Africa\n d) Qatar": "c",
    "Who was the first World Cup mascot?\n a) Goleo\n b) Striker The World Cup Pup\n c) World Cup Willie\n d) Zabivaka": "c",
    "What does the FIFA World Cup Trophy depict?\n a) A player kicking a soccer ball\n b) A champagne fountain\n c) The greek goddess Nike\n d) Two human figures holding up the Earth": "d",
    "Who was the oldest player to score a World Cup goal?\n a) Megan Rapinoe\n b) Formiga\n c) Gunnar Gren\n d) Roger Milla": "d",
    "What was the lowest recorded attendance at a World Cup match?\n a) 3,005\n b) 13,230\n c) 300\n d) 23,235": "c",
    "Which team went 559 consecutive minutes without conceding a goal in the 2006/2010 World Cups?\n a) United States\n b) Switzerland\n c) Ukraine\n d) Chile": "b",
    "Who was the first World Cup winning coach?\n a) Juan Lopez\n b) Luiz Felipe Scolari\n c) Alberto Suppici\n d) Vittorio Pozza": "c",
    "Which player appeared in the first two FIFA World Cup final matches, but with two different teams?\n a) Luis Monti\n b) Frncisco Varallo\n c) Pietro Acari\n d) Pablo Dorado": "a",
    "Who holds the record for most goals scored in a single World Cup match?\n a) Oleg Salenko\n b) Histo Stoichkov\n c) Ronaldo\n d) Pelé": "a",
    "What award is given to the most outstanding player at each World Cup?\n a) The Golden Ball\n b) The Golden Boot\n c) The Golden Pitch\n d) The Golden Glove": "a",
    "Which national World Cup qualifying team was nicknamed Les Elephants?\n a) Ghana\n b) Bangladesh\n c) Ivory Coast\n d) Sri Lanka": "c",
    "Which player scored the very first World Cup goal?\n a) Felipe Rosas\n b) Lucien Laurent\n c) Marcel Capelle\n d) Luis Perez": "b",
    "What was the name of the dog that helped recover the World Cup trophy after it was stolen in 1966?\n a) Striker\n b) Pickles\n c) Sweeper\n d) Winnie The Poodle": "b",
    "What was the first year the World Cup was held in two different countries?\n a) 2002\n b) 1996\n c) 1990\n d) 2008": "a",
    "Who was the first player to miss a penalty kick at the World Cup?\n a) Waldemar De Brito\n b) Rudolf Wetzer\n c) Ricardo Zamora\n d) Lucien Laurent": "a",
    "Which player holds the record for most World Cup matches played?\n a) Lionel Messi\n b) Lothar Matthäus\n c) Rafael Márquez\n d) Antonio Carbajal": "b",
    "Which two countries made their World Cup debuts in 2018?\n a) Costa Rica & Morocco\n b) Cameroon & Holland\n c) Croatia & Serbia\n d) Iceland & Panama": "d",
    "Who was the top scorer in the 2002 World Cup?\n a) Oleg Salenko\n b) Ronaldo\n c) Miroslav Klose\n d) David Villa":"b",
    "What does FIFA stand for?\n a) FOOTBALL INTERNATIONALE FÉDÉRATION ADMINISTRACIÓN\n b) FOOTBALL INTERNATIONALE FÉDÉRATION ATHLÉTIQUE\n c) FÉDÉRATION INTERNATIONALE DE FOOTBALL ASSOCIATION\n d) FÉDÉRATION INTERNATIONALE DE FOOTBALL ATHLÉTIQUE":"c",
    "Why did Zinedine Zidane head-butt Marco Materazzi in the 2006 World Cup?\n a) Materazzi tripped Zidane's teammate\n b) Materazzi insulted Zidane's sister\n c) Materazzi scored the winning goal\n d) Materazzi broke Zidane's nose":"b",
    "Which country hosted the World Cup for the first time in 2018?\n a) Russia\n b) China\n c) France\n d) Croatia": "a",
    "Which World Cup host chose an orange as the 1982 World Cup mascot?\n a) France\n b) Italy\n c) Mexico\n d) Spain": "d",
    "Which country has won the most FIFA World Cups?\n a) Brazil\n b) Italy\n c) Spain\n d) Argentina": "a",
    "Which country has won the second most number of World Cups?\n a) Argentina\n b) Spain\n c) Uruguay\n d) Italy": "d",
    "Which two countries have reached the final of the football World Cup the most number of times?\n a) Brazil & Italy\n b) Spain & Brazil\n c) Germany & Brazil\n d) Italy & Germany": "c",
    "How many times has Germany won the tournament?\n a) 4\n b) 2\n c) 3\n d) 1": "a",
    "In what year was the first World Cup held, and in which country?\n a) Uruguay, 1928\n b) Uruguay, 1930\n c) Italy, 1930\n d) Brazil, 1934": "b",
    "How many countries participated in the first tournament?\n a) 32\n b) 20\n c) 16\n d) 13": "d",
    "Which is the only country to have reached three finals without winning any?\n a) England\n b) France\n c) Netherlands\n d) Czechoslovakia": "c",
    "Which was the first team to win the World Cup twice?\n a) Spain\n b) Brazil\n c) Germany\n d) Italy": "d",
    "Which country holds the record for the worst defense of the World Cup (excluding teams that did not participate in the subsequent tournament)?\n a) Italy in 2006\n b) Argentina in 1990\n c) France in 2002\n d) West Germany in 1994": "c",
    "Which is the only country to have reached more than one World Cup final without losing any?\n a) Spain\n b) England\n c) Uruguay\n d) Brazil": "c",
    "Which player has scored the most number of goals at the FIFA World Cup?\n a) Pelé\n b) Miroslav Klose\n c) Ronaldo\n d) Zinedine Zidane": "b",
    "Which player holds the record for scoring the most goals at a single World Cup tournament?\n a) Ronaldo\n b) Just Fontaine\n c) Pelé\n d) Lionel Messi": "b",
    "Who is the only player to have won the World Cup three times?\n a) Diego Maradona\n b) Pelé\n c) Iker Casillas\n d) Franz Beckenbauer": "b",
    "Who is the first player to win the World Cup as both player and manager?\n a) Franz Beckenbauer\n b) Pelé\n c) Mario Zagallo\n d) Diego Maradona": "c",
    "Who is the oldest player to appear in the World Cup?\n a) Faryd Mondragon\n b) Gianluigi Buffon\n c) Dino Zoff\n d) Roger Milla": "a",
    "Who is the youngest player to appear in the World Cup?\n a) Cristiano Ronaldo\n b) Pelé\n c) Norman Whiteside\n d) Lionel Messi": "c",
    "Who is the youngest player to appear in a World Cup final?\n a) Norman Whiteside\n b) Pelé\n c) Diego Maradona\n d) Zinedine Zidane": "b",
    "Who is the oldest player to appear in a World Cup final?\n a) Franz Beckenbauer\n b) Mario Zagallo\n c) Dino Zoff\n d) Rivaldo": "c",
    "Who is the only player to play in three World Cup finals?\n a) Diego Maradona\n b) Pelé\n c) Cafu\n d) Paolo Maldini": "c",
    "Who is the only player to play in three World Cup finals?\n a) Diego Maradona\n b) Pelé\n c) Cafu\n d) Paolo Maldini": "c",
    "Who is the youngest goalscorer at the World Cup?\n a) Diego Maradona\n b) Pelé\n c) Lionel Messi\n d) Michael Owen": "b",
    "Who scored the first hattrick in the World Cup?\n a) Pelé\n b) Sandor Kocsis\n c) Bert Patenaude\n d) Guillermo Stabile": "c",
    "Which two teams contested the match that came to be known as the Maracanazo?\n a) Brazil & Argentina\n b) Brazil & Uruguay\n c) Uruguay & Italy\n d) Italy & Argentina": "b",
    "Who holds the record of scoring at least one goal in the most number of World Cup matches?\n a) Lionel Messi\n b) Cristiano Ronaldo\n c) Ronaldo\n d) Just Fontaine": "c",
    "Who is the only player to score a hattrick in a World Cup final?\n a) Ronaldo\n b) Pelé\n c) Just Fontaine\n d) Geoffrey Hurst": "d",
    "Which player scored in each of Brazil games at the 1970 World Cup?\n a) Jairzinho\n b) Pelé\n c) Tostao\n d) Gerson": "a",
    "Which are the only two countries to have reached three consecutive World Cup finals?\n a) Spain & Brazil\n b) Italy & Germany\n c) Germany & Brazil\n d) Brazil & Italy": "c",
    "In the 2014 World Cup, the Maracana became the second stadium to host two World Cup finals. Which was the first?\n a) Wembley Stadium, London\n b) Stadio Olimpico, Rome\n c) Santiago Bernabeu, Madrid\n d) Estadio Azteca, Mexico City": "d",
    "Which is the only country to have appeared in every World Cup tournament so far?\n a) Brazil\n b) England\n c) Germany\n d) Argentina": "a",
    "In which World Cup did players first wear jerseys with their surname on the back?\n a) 1998\n b) 1990\n c) 1986\n d) 1994": "d",
    "How many countries have made at least one appearance at the World Cup?\n a) 76\n b) 66\n c) 96\n d) 56": "a",
    "How many countries have played in the World Cup final?\n a) 10\n b) 9\n c) 8\n d) 12": "d",
    "What is the highest number of total goals scored in a single World Cup final?\n a) 5\n b) 8\n c) 7\n d) 6": "c",
    "What is the name of the ball used at the 2014 World Cup in Brazil?\n a) Jabulani\n b) Brazuca\n c) Teimgeist\n d) Maximum": "b",
    "What is the name of the mascot of the 2014 World Cup, and what animal does he represent?\n a) Fuleco, armadillo\n b) Fuleco, jaguar\n c) Trigger, jaguar\n d) Dilly, armadillo": "a",
    "Which country holds the record for the most matches won during a World Cup tournament?\n a) Brazil\n b) Germany\n c) Italy\n d) Spain": "a",
    "Which country has won the most matches in the World Cup?\n a) Brazil\n b) Germany\n c) Italy\n d) Spain": "a",
    "Which country has lost the most matches in the World Cup?\n a) Hungary\n b) Sweden\n c) Mexico\n d) Australia": "c",
    "Which is the only country to have been eliminated in three World Cup tournaments without losing a match in normal time (90 minutes)?\n a) Spain\n b) England\n c) Switzerland\n d) Portugal": "b",
    "Which was the first World Cup tournament to feature 32 teams, as is the current format?\n a) 1994\n b) 1998\n c) 2006\n d) 2014": "b",
    "In the 2006 World Cup, which English referee mistakenly handed out three yellow cards to the same player instead of sending him off at two?\n a) Howard Webb\n b) Martin Atkinson\n c) Lee Probert\n d) Graham Poll": "d",
    "What was the World Cup trophy called before 1974?\n a) World Championship Trophy\n b) FIFA World Cup Trophy\n c) Jules Rimet Trophy\n d) Edson Arantes do Nascimento Trophy": "c",
    "Which was the first World Cup final to be decided on penalties?\n a) 1990, Germany vs Argentina\n b) 1998, France vs Brazil\n c) 1962, Brazil vs Czechoslovakia\n d) 1994, Brazil vs Italy": "d",
    "Which country has been involved in two World Cup Final penalty shootouts?\n a) Brazil\n b) Italy\n c) Germany\n d) France": "b",
    "Which is the only South American country to win the World Cup in Europe?\n a) Brazil\n b) Argentina\n c) Uruguay\n d) Colombia": "a",
    "Which country has made the most appearances at the World Cup without ever advancing past the first round?\n a) Mexico\n b) Scotland\n c) Chile\n d) Austria": "b",
    "Which is the only country to twice enter a tournament as defending champions only to get eliminated in the first round?\n a) France\n b) Brazil\n c) Italy\n d) England": "c",
    "Which was the only debutant country in the 2014 World Cup?\n a) Ivory Coast\n b) Honduras\n c) Cameroon\n d) Bosnia and Herzegovina": "d",
    "Which is the only country to withdraw from the World Cup on the grounds that they were used to playing barefoot, which FIFA did not allow?\n a) Malaysia\n b) Zimbabwe\n c) India\n d) Ghana": "c",
    "What was the official song of the 2010 World Cup in South Africa?\n a) Ole Ole Ole\n b) Waka Waka\n c) The Cup of Life\n d) All Rise for Africa": "b",
    "Which instrument became world-famous thanks to its association to football in South Africa?\n a) Guitar\n b) Banjo\n c) Didegeridoo\n d) Vuvuzela": "d",
    "What was the official attendance for the 1950 World Cup Final between Brazil and Uruguay?\n a) 173,850\n b) 190,534\n c) 200,457\n d) 78,838": "a",
    "How many countries have won the football World Cup on home soil?\n a) None\n b) 5\n c) 6\n d) 8": "b",
    "Which World Cup had the highest average attendance?\n a) 2006\n b) 2010\n c) 1994\n d) 1998": "c",
    "Which country has won the most penalty shootouts in their football World Cup history?\n a) Italy\n b) Argentina\n c) Germany\n d) France": "c",
    "Which was the first team to win three World Cups?\n a) Italy\n b) Brazil\n c) Germany\n d) Argentina": "b",
    "What percentage of the world population watched the 2010 World Cup Final?\n a) 80%\n b) 30%\n c) 50%\n d) 60%": "c",
    "Including penalty shootouts, which goalkeeper holds the record for the most penalty saves in a single tournament?\n a) Iker Casillas\n b) Gianluigi Buffon\n c) Sergio Goycochea\n d) Lev Yashin": "c",
    "Which country has the record for the most successive successful qualifications to the World Cup (without being the host nation or the defending champion)?\n a) Italy\n b) Netherlands\n c) Mexico\n d) Spain": "d",
    "Which match saw the most amount of goals scored in World Cup history?\n a) Brazil vs Sweden, 1958 Final\n b) Brazil vs Italy, 1982 Semifinal\n c) Austria vs Switzerland, 1954 Quarterfinal\n d) Hungary vs El Salvador, 1982 Group Stage": "c",
    "Which two countries have played the most matches at the World Cup?\n a) Italy, Brazil\n b) Brazil, Germany\n c) Germany, Spain\n d) Brazil, Spain": "b"
}

questions = list(dic_qa.keys())

#CREATION OF PLAYER CLASS
class Player:
    score = 0
    def __init__(self, name):
        self.name = name

p1 = Player(p1_name)
p2 = Player(p2_name)

#GAME LOOP
turn = 1

while p1.score < 5 or p2.score < 5:
    chosen_question = randint(0, len(questions) - 1)
    if turn % 2 != 0:
        print("\n" + p1.name + " answer the following question:\n")
        p1_answer = input(questions[chosen_question] + "\nAnswer: ")
        if p1_answer.lower() == dic_qa.get(questions[chosen_question]):
            p1.score += 1
            print(colored("Your answer is CORRECT!", "green"))
        else:
            p1.score += 0
            print(colored("Your answer is INCORRECT", "red"))
    elif turn % 2 == 0:
        print("\n" + p2.name + " answer the following question:\n")
        p2_answer = input(questions[chosen_question] + "\nAnswer: ")
        if p2_answer.lower() == dic_qa.get(questions[chosen_question]):
            p2.score += 1
            print(colored("Your answer is CORRECT!", "green"))
        else:
            p2.score += 0
            print(colored("Your answer is INCORRECT", "red"))
    questions.remove(questions[chosen_question])
    turn += 1

if p1.score == 5:
    print("\nCongratulation " + p1.name + ", you are THE WINNER!")
elif p2.score == 5:
    print("\nCongratulation " + p2.name + ", you are THE WINNER!")