
import random

questions = [
    "Why can't I sleep at night?",
    "I got 99 problems but _ ain't one.",
    "What's a girl's best friend?",
    "What's that smell?",
    "This is the way the world ends / This is the way the world ends / Not with a bang but with _.",
    "What is Batman's guilty pleasure?",
    "TSA guidelines now prohibit _ on airplanes.",
    "What ended my last relationship?",
    "MTV's new reality show features eight washed-up celebrities living with _.",
    "I drink to forget _.",
    "I'm sorry, Professor, but I couldn't complete my homework because of _.",
    "Alternative medicine is now embracing the curative powers of _.",
    "What's that sound?",
    "What's the next Happy Meal toy?",
    "It's a pity that kids these days are all getting involved with _.",
    "In the new Disney Channel Original Movie, Hannah Montana struggles with _ for the first time.",
    "_. That's how I want to die.",
    "What does Dick Cheney prefer?",
    "What's the most emo?",
    "Instead of coal, Santa now gives the bad children _.",
    "Next from J.K. Rowling: Harry Potter and the Chamber of _.",
    "A romantic, candlelit dinner would be incomplete without _.",
    "White people like _.",
    "_. Betcha can't have just one!",
    "War! What is it good for?",
    "BILLY MAYS HERE FOR _.",
    "_. High five, bro.",
    "During sex, I like to think about _.",
    "What did I bring back from Mexico?",
    "What are my parents hiding from me?",
    "What will always get you laid?",
    "What would grandma find disturbing, yet oddly charming?",
    "What did the U.S. airdrop to the children of Afghanistan?",
    "What helps Obama unwind?",
    "What's there a ton of in heaven?",
    "Major League Baseball has banned _ for giving players an unfair advantage.",
    "When I am a billionaire, I shall erect a 50-foot statue to commemorate _.",
    "What's the new fad diet?",
    "When I am the President of the United States, I will create the Department of _.",
    "_. It's a trap!",
    "How am I maintaining my relationship status?",
    "What will I bring back in time to convince people that I am a powerful wizard?",
    "While the United States raced the Soviet Union to the moon, the Mexican government funneled millions of pesos into research on _.",
    "Coming to Broadway this season, _: The Musical.",
    "What's my secret power?",
    "What gives me uncontrollable gas?",
    "But before I kill you, Mr. Bond, I must show you _.",
    "What never fails to liven up the party?",
    "What am I giving up for Lent?",
    "What do old people smell like? ",
    "The class field trip was completely ruined by _.",
    "When Pharaoh remained unmoved, Moses called down a plague of _.",
    "I do not know with which weapons World War III will be fought, but World War IV will be fought with _.",
    "What's Teach for America using to inspire inner city students to succeed?",
    "In Michael Jackson's final moments, he thought about _.",
    "Why do I hurt all over?",
    "Studies show that lab rats navigate mazes 50% faster after being exposed to _.",
    "Why am I sticky?",
    "What's my anti-drug?",
    "And the Academy Award for _ goes to _.",
    "For my next trick, I will pull _ out of _.",
    "_: Good to the last drop.",
    "What did Vin Diesel eat for dinner?",
    "_: kid-tested, mother-approved.",
    "What gets better with age?",
    "I never truly understood _ until I encountered _.",
    "Rumor has it that Vladimir Putin's favorite delicacy is _ stuffed with _.",
    "Lifetime presents _, the story of _.",
    "Make a haiku.",
    "In M. Night Shyamalan's new movie, Bruce Willis discovers that _ had really been _ all along.",
    "_ is a slippery slope that leads to _.",
    "In a world ravaged by _, our only solace is _.",
    "That's right, I killed _. How, you ask? _.",
    "When I was tripping on acid, _ turned into _.",
    "_ + _ = _.",
    "What's the next superhero/sidekick duo?",
    "Dear Abby, I'm having some trouble with _ and would like your advice.",
    "After the earthquake, Sean Penn brought _ to the people of Haiti.",
    "In L.A. County Jail, word is you can trade 200 cigarettes for _.",
    "Maybe she's born with it. Maybe it's _.",
    "Life for American Indians was forever changed when the White Man introduced them to _.",
    "Next on ESPN2, the World Series of _.",
    "Step 1: _. Step 2: _. Step 3: Profit.",
    "Here is the church. Here is the steeple. Open the doors. And there is _.",
    "How did I lose my virginity?",
    "In 1,000 years, when paper money is a distant memory, how will we pay for goods and services?",
    "What don't you want to find in your Kung Pao chicken?",
    "The Smithsonian Museum of Natural History has just opened an exhibit on _.",
    "Daddy, why is Mommy crying?",
]

anwsers = [
    "Coat hanger abortions.",
    "Man meat.",
    "Autocannibalism.",
    "Vigorous jazz hands.",
    "Flightless birds.",
    "Pictures of boobs.",
    "Doing the right thing.",
    "The violation of our most basic human rights.",
    "Viagra.",
    "Self-loathing.",
    "Spectacular abs.",
    "A balanced breakfast.",
    "Roofies.",
    "Concealing a boner.",
    "Amputees.",
    "The Big Bang.",
    "Former President George W. Bush.",
    "The Rev. Dr. Martin Luther King, Jr.",
    "Smegma.",
    "Being marginalized.",
    "Cuddling.",
    "Laying an egg.",
    "The Pope.",
    "Aaron Burr.",
    "Genital piercings.",
    "Fingering.",
    "A bleached asshole.",
    "Horse meat.",
    "Fear itself.",
    "Science.",
    "Elderly Japanese men.",
    "Stranger danger.",
    "The terrorists.",
    "Praying the gay away.",
    "Same-sex ice dancing.",
    "Ethnic cleansing.",
    "Cheating in the Special Olympics.",
    "German dungeon porn.",
    "Bingeing and purging.",
    "Making a pouty face.",
    "William Shatner.",
    "Heteronormativity.",
    "Nickelback.",
    "Tom Cruise.",
    "The profoundly handicapped.",
    "The placenta.",
    "Chainsaws for hands.",
    "Arnold Schwarzenegger.",
    "An icepick lobotomy.",
    "Goblins.",
    "Object permanence.",
    "Dying.",
    "Foreskin.",
    "A falcon with a cap on its head.",
    "Hormone injections.",
    "Dying of dysentery.",
    "Sexy pillow fights.",
    "The invisible hand.",
    "A really cool hat.",
    "Sean Penn.",
    "Heartwarming orphans.",
    "The clitoris.",
    "The Three-Fifths compromise.",
    "A sad handjob.",
    "Men.",
    "Historically black colleges.",
    "A micropenis.",
    "Raptor attacks.",
    "Agriculture.",
    "Vikings.",
    "Pretending to care.",
    "The Underground Railroad.",
    "My humps.",
    "Being a dick to children.",
    "Geese.",
    "Bling.",
    "Sniffing glue.",
    "The South.",
    "An Oedipus complex.",
    "Eating all of the cookies before the AIDS bake-sale.",
    "Sexting.",
    "YOU MUST CONSTRUCT ADDITIONAL PYLONS.",
    "Mutually-assured destruction.",
    "Sunshine and rainbows.",
    "Count Chocula.",
    "Sharing needles.",
    "Being rich.",
    "Skeletor.",
    "A sausage festival.",
    "Michael Jackson.",
    "Emotions.",
    "Farting and walking away.",
    "The Chinese gymnastics team.",
    "Necrophilia.",
    "Spontaneous human combustion.",
    "Yeast.",
    "Leaving an awkward voicemail.",
    "Dick Cheney.",
    "White people.",
    "Penis envy.",
    "Teaching a robot to love.",
    "Sperm whales.",
    "Scrubbing under the folds.",
    "Panda sex.",
    "Whipping it out.",
    "Catapults.",
    "Masturbation.",
    "Natural selection.",
    "Opposable thumbs.",
    "A sassy black woman.",
    "AIDS.",
    "The KKK.",
    "Figgy pudding.",
    "Seppuku.",
    "Gandhi.",
    "Preteens.",
    "Toni Morrison's vagina.",
    "Five-Dollar Footlongs.",
    "Land mines.",
    "A sea of troubles.",
    "A zesty breakfast burrito.",
    "Christopher Walken.",
    "Friction.",
    "Balls.",
    "Dental dams.",
    "A can of whoop-ass.",
    "A tiny horse.",
    "Waiting 'til marriage.",
    "Authentic Mexican cuisine.",
    "Genghis Khan.",
    "Old-people smell.",
    "Feeding Rosie O'Donnell.",
    "Pixelated bukkake.",
    "Friends with benefits.",
    "The token minority.",
    "A thermonuclear detonation.",
    "Take-backsies.",
    "The Rapture.",
    "A cooler full of organs.",
    "Sweet, sweet vengeance.",
    "RoboCop.",
    "Keanu Reeves.",
    "Drinking alone.",
    "Giving 110%.",
    "Flesh-eating bacteria.",
    "The American Dream.",
    "Taking off your shirt.",
    "Me time.",
    "A murder most foul.",
    "The inevitable heat death of the universe.",
    "The folly of man.",
    "That thing that electrocutes your abs.",
    "Cards Against Humanity.",
    "Fiery poops.",
    "Poor people.",
    "Edible underpants.",
    "Britney Spears at 55.",
    "All-you-can-eat shrimp for $4.99.",
    "Pooping back and forth. Forever.",
    "Fancy Feast.",
    "Jewish fraternities.",
    "Being a motherfucking sorcerer.",
    "Pulling out.",
    "Picking up girls at the abortion clinic.",
    "The homosexual agenda.",
    "The Holy Bible.",
    "Passive-agression.",
    "Ronald Reagan.",
    "Vehicular manslaughter.",
    "Nipple blades.",
    "Assless chaps.",
    "Full frontal nudity.",
    "Hulk Hogan.",
    "Daddy issues.",
    "The hardworking Mexican.",
    "Natalie Portman.",
    "Waking up half-naked in a Denny's parking lot.",
    "God.",
    "Sean Connery.",
    "Saxophone solos.",
    "Gloryholes.",
    "The World of Warcraft.",
    "Homeless people.",
    "Scalping.",
    "Darth Vader.",
    "Eating the last known bison.",
    "Guys who don't call.",
    "Hot Pockets.",
    "A time travel paradox.",
    "The milk man.",
    "Testicular torsion.",
    "Dropping a chandelier on your enemies and riding the rope up.",
    "World peace.",
    "A salty surprise.",
    "Poorly-timed Holocaust jokes.",
    "Smallpox blankets.",
    "Licking things to claim them as your own.",
    "The heart of a child.",
    "Robert Downey, Jr.",
    "Lockjaw.",
    "Eugenics.",
    "A good sniff.",
    "Friendly fire.",
    "The taint; the grundle; the fleshy fun-bridge.",
    "Wearing underwear inside-out to avoid doing laundry.",
    "Hurricane Katrina.",
    "Free samples.",
    "Jerking off into a pool of children's tears.",
    "A foul mouth.",
    "The glass ceiling.",
    "Republicans.",
    "Explosions.",
    "Michelle Obama's arms.",
    "Getting really high.",
    "Attitude.",
    "Sarah Palin.",
    "The Uebermensch.",
    "Altar boys.",
    "My soul.",
    "My sex life.",
    "Pedophiles.",
    "72 virgins.",
    "Pabst Blue Ribbon.",
    "Domino's; Oreo; Dessert Pizza.",
    "A snapping turtle biting the tip of your penis.",
    "The Blood of Christ.",
    "Half-assed foreplay.",
    "My collection of high-tech sex toys.",
    "A middle-aged man on roller skates.",
    "Bitches.",
    "Bill Nye the Science Guy.",
    "Italians.",
    "A windmill full of corpses.",
    "Adderall.",
    "Crippling debt.",
    "A stray pube.",
    "Prancing.",
    "Passing a kidney stone.",
    "A brain tumor.",
    "Leprosy.",
    "Puppies!",
    "Bees?",
    "Frolicking.",
    "Repression.",
    "Road head.",
    "A bag of magic beans.",
    "An asymmetric boob job.",
    "Dead parents.",
    "Public ridicule.",
    "A mating display.",
    "A mime having a stroke.",
    "Stephen Hawking talking dirty.",
    "African children.",
    "Mouth herpes.",
    "Overcompensation.",
    "Riding off into the sunset.",
    "Being on fire.",
    "Tangled Slinkys.",
    "Civilian casualties.",
    "Auschwitz.",
    "My genitals.",
    "Not reciprocating oral sex.",
    "Lactation.",
    "Being fabulous.",
    "Shaquille O'Neal's acting career.",
    "My relationship status.",
    "Asians who aren't good t math.",
    "Alcoholism.",
    "Incest.",
    "Grave robbing.",
    "Hope.",
    "8 oz. of sweet Mexican black-tar heroin.",
    "Kids with ass cancer.",
    "Winking at old people.",
    "The Jews.",
    "Justin Bieber.",
    "Doin' it in the butt.",
    "A lifetime of sadness.",
    "The Hamburglar.",
    "Swooping.",
    "Classist undertones.",
    "New Age music.",
    "Not giving a shit about the Third World.",
    "The Kool-Aid Man.",
    "A hot mess.",
    "Tentacle porn.",
    "Lumberjack fantasies.",
    "The gays.",
    "Scientology.",
    "Estrogen.",
    "GoGurt.",
    "Judge Judy.",
    "Dick fingers.",
    "Racism.",
    "Surprise sex!",
    "Police brutality.",
    "Passable transvestites.",
    "The Virginia Tech Massacre.",
    "When you fart and a little bit comes out.",
    "Oompa-Loompas.",
    "A fetus.",
    "Obesity.",
    "Tasteful sideboob.",
    "Hot people.",
    "BATMAN!!!",
    "Black people.",
    "A gassy antelope.",
    "Sexual tension.",
    "Third base.",
    "Racially-biased SAT questions.",
    "Porn stars.",
    "A Super Soaker full of cat pee.",
    "Muhammed (Praise Be Unto Him).",
    "Puberty.",
    "A disappointing birthday party.",
    "An erection that lasts longer than four hours.",
    "White privilege.",
    "Getting so angry that you pop a boner.",
    "Wifely duties.",
    "Two midgets shitting into a bucket.",
    "Queefing.",
    "Wiping her butt.",
    "Golden showers.",
    "Barack Obama.",
    "Nazis.",
    "A robust mongoloid.",
    "An M. Night Shyamalan plot twist.",
    "Getting drunk on mouthwash.",
    "Lunchables.",
    "Women in yogurt commercials.",
    "John Wilkes Booth.",
    "Powerful thighs.",
    "Mr. Clean, right behind you.",
    "Multiple stab wounds.",
    "Cybernetic enhancements.",
    "Serfdom.",
    "Kanye West.",
    "Women's suffrage.",
    "Children on leashes.",
    "Harry Potter erotica.",
    "The Dance of the Sugar Plum Fairy.",
    "Lance Armstrong's missing testicle.",
    "Parting the Red Sea.",
    "The Amish.",
    "Dead babies.",
    "Child beauty pageants.",
    "AXE Body Spray.",
    "Centaurs.",
    "Copping a feel.",
    "Grandma.",
    "Famine.",
    "The Trail of Tears.",
    "The miracle of childbirth.",
    "Finger painting.",
    "A monkey smoking a cigar.",
    "The Make-A-Wish Foundation.",
    "Anal beads.",
    "The Force.",
    "Kamikaze pilots.",
    "Dry heaving.",
    "Active listening.",
    "Ghosts.",
    "The Hustle.",
    "Peeing a little bit.",
    "Another goddamn vampire movie.",
    "Shapeshifters.",
    "The Care Bear Stare.",
    "Hot cheese.",
    "A mopey zoo lion.",
    "A defective condom.",
    "Teenage pregnancy.",
    "A Bop It.",
    "Expecting a burp and vomiting on the floor.",
    "Horrifying laser hair removal accidents.",
    "Boogers.",
    "Unfathomable stupidity.",
    "Breaking out into song and dance.",
    "Soup that is too hot.",
    "Morgan Freeman's voice.",
    "Getting naked and watching Nickelodeon.",
    "MechaHitler.",
    "Flying sex snakes.",
    "The true meaning of Christmas.",
    "My inner demons.",
    "Pac-Man uncontrollably guzzling cum.",
    "My vagina.",
    "A homoerotic volleyball montage.",
    "Actually taking candy from a baby.",
    "Crystal meth.",
    "Exactly what you'd expect.",
    "Natural male enhancement.",
    "Passive-aggressive Post-it notes.",
    "Inappropriate yodeling.",
    "Lady Gaga.",
    "The Little Engine That Could.",
    "Vigilante justice.",
    "A death ray.",
    "Poor life choices.",
    "A gentle caress of the inner thigh.",
    "Embryonic stem cells.",
    "Nicolas Cage.",
    "Firing a rifle into the air while balls deep in a squealing hog.",
    "Switching to Geico.",
    "The chronic.",
    "Erectile dysfunction.",
    "Home video of Oprah sobbing into a Lean Cuisine.",
    "A bucket of fish heads.",
    "50,000 volts straight to the nipples.",
    "Being fat and stupid.",
    "Hospice care.",
    "A pyramid of severed heads.",
    "Getting married, having a few kids, buying some stuff, retiring to Florida, and dying.",
    "A subscription to Men's Fitness.",
    "Crucifixion.",
    "A micropig wearing a tiny raincoat and booties.",
    "Some god-damn peace and quiet.",
    "Used panties.",
    "A tribe of warrior women.",
    "The penny whistle solo from 'My Heart Will Go On.'",
    "An oversized lollipop.",
    "Helplessly giggling at the mention of Hutus and Tutsis.",
    "Not wearing pants.",
    "Consensual sex.",
    "Her Majesty, Queen Elizabeth II.",
    "Funky fresh rhymes.",
    "The art of seduction.",
    "The Devil himself.",
    "Advice from a wise, old black man.",
    "Destroying the evidence.",
    "The light of a billion suns.",
    "Wet dreams.",
    "Synergistic management solutions.",
    "Growing a pair.",
    "Silence.",
    "An M16 assault rifle.",
    "Poopy diapers.",
    "A live studio audience.",
    "The Great Depression.",
    "A spastic nerd.",
    "Rush Limbaugh's soft, shitty body.",
    "Tickling Sean Hannity, even after he tells you to stop.",
    "Stalin.",
    "Brown people.",
    "Rehab.",
    "Capturing Newt Gingrich and forcing him to dance in a monkey suit.",
    "Battlefield amputations.",
    "An uppercut.",
    "Shiny objects.",
    "An ugly face.",
    "Menstrual rage.",
    "A bitch slap.",
    "One trillion dollars.",
    "Chunks of dead prostitute.",
    "The entire Mormon Tabernacle Choir.",
    "The female orgasm.",
    "Extremely tight pants.",
    "The Boy Scouts of America.",
    "Stormtroopers.",
    "Throwing a virgin into a volcano.",
]


def generate_rand_message():
    retmessage = ""

    q = questions[random.randint(0, len(questions))]
    q_split = q.split("_")

    if len(q_split) == 1:
        retmessage = q + " " + anwsers[random.randint(0,len(anwsers))]
    else:
        for i in range(0, len(q_split) - 1):
            retmessage += q_split[i] + anwsers[random.randint(0,len(anwsers))][:-1]
        retmessage += q_split[len(q_split) - 1]

    return retmessage

msg = generate_rand_message()
print(msg + " ")