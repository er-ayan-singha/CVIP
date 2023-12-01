from tkinter import *
import random
from tkinter import messagebox
import pyttsx3
import tkinter as tk
import pygame

class SpeedTester:
    def __init__(self):
        # Text-to-speech engine setup
        self.engine = pyttsx3.init()

        # Set the rate of speech
        rate = self.engine.getProperty('rate')
        self.engine.setProperty('rate', rate - 50)

        # Setup
        self.root = Tk()
        self.root.title('Typing Speed Tester @ LIICTER')

        self.root.geometry('1400x800')  # Increased height to accommodate the self.root

        self.root.option_add("*Label.Font", "consolas 30")
        self.root.option_add("*Button.Font", "consolas 30")
        self.root.config(bg="black")

        # Add a global variable to track if the game is stopped
        self.gameStopped = False

        # Other initializations
        self.writeAble = None
        self.secondsPassed = 0
        self.nameLabelLeft = None
        self.nameLabelRight = None
        self.currentAlphabetLabel = None
        self.secondsLeft = None
        self.showcaseResults = None

        # Call the handlingLabels method to set up the initial UI
        self.handlingLabels()

        pygame.mixer.init()
        self.typing_sound = pygame.mixer.Sound('key_press.wav')
           # Place each key individually using .place()
        self.buttons = {}
        self.buttons['Q'] = tk.Button(self.root, text='Q',  bg="black", fg="white", font=("Tekton Pro Ext",15))
        self.buttons['Q'].place(x=10, y=550)

        self.buttons['W'] = tk.Button(self.root, text='W', bg="black", fg="white", font=("Tekton Pro Ext",15))
        self.buttons['W'].place(x=60, y=550)

        self.buttons['E'] = tk.Button(self.root, text='E', bg="black", fg="white", font=("Tekton Pro Ext",15))
        self.buttons['E'].place(x=110, y=550)

        self.buttons['R'] = tk.Button(self.root, text='R',  bg="black", fg="white",font=("Tekton Pro Ext",15))
        self.buttons['R'].place(x=160, y=550)

        self.buttons['T'] = tk.Button(self.root, text='T',  bg="black", fg="white",font=("Tekton Pro Ext",15))
        self.buttons['T'].place(x=210, y=550)

        self.buttons['Y'] = tk.Button(self.root, text='Y', bg="black", fg="white", font=("Tekton Pro Ext",15))
        self.buttons['Y'].place(x=260, y=550)

        self.buttons['U'] = tk.Button(self.root, text='U', bg="black", fg="white", font=("Tekton Pro Ext",15))
        self.buttons['U'].place(x=310, y=550)

        self.buttons['I'] = tk.Button(self.root, text='I', bg="black", fg="white", font=("Tekton Pro Ext",15))
        self.buttons['I'].place(x=360, y=550)

        self.buttons['O'] = tk.Button(self.root, text='O', bg="black", fg="white", font=("Tekton Pro Ext",15))
        self.buttons['O'].place(x=410, y=550)

        self.buttons['P'] = tk.Button(self.root, text='P',  bg="black", fg="white",font=("Tekton Pro Ext",15))
        self.buttons['P'].place(x=460, y=550)

        self.buttons['A'] = tk.Button(self.root, text='A', bg="black", fg="white", font=("Tekton Pro Ext",15))
        self.buttons['A'].place(x=35, y=600)

        buttons_s= tk.Button(self.root, text='S', bg="black", fg="white",font=("Tekton Pro Ext",15))
        buttons_s.place(x=85, y=600)

        self.buttons['D'] = tk.Button(self.root, text='D', bg="black", fg="white", font=("Tekton Pro Ext",15))
        self.buttons['D'].place(x=135, y=600)

        self.buttons['F'] = tk.Button(self.root, text='F', bg="black", fg="white", font=("Tekton Pro Ext",15))
        self.buttons['F'].place(x=185, y=600)

        self.buttons['G'] = tk.Button(self.root, text='G', bg="black", fg="white", font=("Tekton Pro Ext",15))
        self.buttons['G'].place(x=235, y=600)

        self.buttons['H'] = tk.Button(self.root, text='H', bg="black", fg="white", font=("Tekton Pro Ext",15))
        self.buttons['H'].place(x=285, y=600)

        self.buttons['J'] = tk.Button(self.root, text='J', bg="black", fg="white", font=("Tekton Pro Ext",15))
        self.buttons['J'].place(x=335, y=600)

        self.buttons['K'] = tk.Button(self.root, text='K', bg="black", fg="white", font=("Tekton Pro Ext",15))
        self.buttons['K'].place(x=385, y=600)

        self.buttons['L'] = tk.Button(self.root, text='L',  bg="black", fg="white",font=("Tekton Pro Ext",15))
        self.buttons['L'].place(x=435, y=600)

        self.buttons['Z'] = tk.Button(self.root, text='Z', bg="black", fg="white", font=("Tekton Pro Ext",15))
        self.buttons['Z'].place(x=60, y=650)

        self.buttons['X'] = tk.Button(self.root, text='X',  bg="black", fg="white",font=("Tekton Pro Ext",15))
        self.buttons['X'].place(x=110, y=650)

        self.buttons['C'] = tk.Button(self.root, text='C', bg="black", fg="white", font=("Tekton Pro Ext",15))
        self.buttons['C'].place(x=160, y=650)

        self.buttons['V'] = tk.Button(self.root, text='V',  bg="black", fg="white",font=("Tekton Pro Ext",15))
        self.buttons['V'].place(x=210, y=650)

        self.buttons['B'] = tk.Button(self.root, text='B',  bg="black", fg="white",font=("Tekton Pro Ext",15))
        self.buttons['B'].place(x=260, y=650)

        self.buttons['N'] = tk.Button(self.root, text='N', bg="black", fg="white", font=("Tekton Pro Ext",15))
        self.buttons['N'].place(x=310, y=650)

        self.buttons['M'] = tk.Button(self.root, text='M', bg="black", fg="white", font=("Tekton Pro Ext",15))
        self.buttons['M'].place(x=360, y=650)

        # Numeric keys
        self.buttons['1'] = tk.Button(self.root, text='1',  bg="black", fg="white",font=("Tekton Pro Ext",15))
        self.buttons['1'].place(x=10, y=700)

        self.buttons['2'] = tk.Button(self.root, text='2',  bg="black", fg="white",font=("Tekton Pro Ext",15))
        self.buttons['2'].place(x=60, y=700)

        self.buttons['3'] = tk.Button(self.root, text='3',  bg="black", fg="white",font=("Tekton Pro Ext",15))
        self.buttons['3'].place(x=110, y=700)

        self.buttons['4'] = tk.Button(self.root, text='4',  bg="black", fg="white",font=("Tekton Pro Ext",15))
        self.buttons['4'].place(x=160, y=700)

        self.buttons['5'] = tk.Button(self.root, text='5',  bg="black", fg="white",font=("Tekton Pro Ext",15))
        self.buttons['5'].place(x=210, y=700)

        self.buttons['6'] = tk.Button(self.root, text='6',  bg="black", fg="white",font=("Tekton Pro Ext",15))
        self.buttons['6'].place(x=260, y=700)

        self.buttons['7'] = tk.Button(self.root, text='7',  bg="black", fg="white",font=("Tekton Pro Ext",15))
        self.buttons['7'].place(x=310, y=700)

        self.buttons['8'] = tk.Button(self.root, text='8',  bg="black", fg="white",font=("Tekton Pro Ext",15))
        self.buttons['8'].place(x=360, y=700)

        self.buttons['9'] = tk.Button(self.root, text='9',  bg="black", fg="white",font=("Tekton Pro Ext",15))
        self.buttons['9'].place(x=410, y=700)

        self.buttons['0'] = tk.Button(self.root, text='0', bg="black", fg="white", font=("Tekton Pro Ext",15))
        self.buttons['0'].place(x=460, y=700)
        
        

        # Start the Tkinter main loop
        self.root.mainloop()
    def play_typing_sound(self):
        # Play the typing sound
        pygame.mixer.Sound.play(self.typing_sound)


    def handlingLabels(self):
        # Text List
        random_selection = ['Python a highlevel programming language has gained immense popularity for its simplicity readability and versatility Created by Guido van Rossum and first released in nineteen ninetyone Python prioritizes code readability making it an ideal language for beginners and experienced developers alike Pythons syntax designed to be clear and concise minimizes the need for boilerplate code fostering a clean and expressive coding style With a dynamic typing system and automatic memory management Python promotes rapid development and allows developers to focus on problemsolving rather than dealing with lowlevel details',
                            'One of Pythons key strengths lies in its extensive standard library offering a wide range of modules and packages that facilitate various tasks from web development and data analysis to artificial intelligence and scientific computing The languages robust community support and the availability of thirdparty libraries such as NumPy Pandas and TensorFlow contribute to its adaptability across diverse domains Pythons versatility extends beyond traditional software development it is frequently used in scripting automation and even as a language for introductory computer science courses Its crossplatform compatibility ensures that Python code can run seamlessly on different operating systems enhancing its appeal for developers working in various environments',
                            'Pythons success in the modern tech landscape can be attributed to its role in emerging technologies As the language of choice for machine learning and artificial intelligence applications Python has become an integral part of the data science ecosystem Frameworks like Django and Flask have solidified Pythons position in web development enabling the creation of scalable and maintainable web applications The languages support for integration with other languages such as C and C enhances its capabilities making it a preferred choice for projects with performancecritical components Overall Pythons combination of readability versatility and community support has positioned it as a powerhouse in the software development world with a continuously growing user base and a bright future ahead',
                            'Digital marketing is a dynamic and multifaceted field that leverages online channels to promote products services or brands It encompasses a wide range of strategies including search engine optimization SEO social media marketing email marketing content marketing and more One of the key advantages of digital marketing is its ability to reach a global audience breaking down geographical barriers and enabling businesses to connect with potential customers across the world In the digital landscape data plays a crucial role allowing marketers to analyze consumer behavior preferences and trends This datadriven approach enables targeted and personalized campaigns ensuring that businesses can tailor their messages to specific demographics thereby increasing the effectiveness of their marketing efforts',
                            'Social media marketing is an integral component of digital marketing harnessing the power of platforms like Facebook Instagram Twitter and LinkedIn to engage with audiences These platforms provide a unique opportunity for brands to build a community share valuable content and establish a direct line of communication with their customers Through strategic content creation and engagement strategies businesses can enhance brand awareness and foster customer loyalty Additionally paid advertising on social media platforms allows for precise targeting ensuring that ads are shown to the most relevant audiences based on demographics interests and online behavior As social media continues to evolve staying updated on platform algorithms and trends is crucial for digital marketers to adapt their strategies and maintain a competitive edge',
                            'Email marketing remains a stalwart in the digital marketing arsenal providing a direct and costeffective way to communicate with potential and existing customers By crafting compelling and personalized email campaigns businesses can nurture leads drive conversions and build longterm relationships Automation tools further streamline the email marketing process allowing for the creation of targeted campaigns triggered by specific customer actions or milestones However the success of email marketing hinges on delivering valuable content and maintaining a balance between promotional and informative messages As privacy concerns grow respecting user preferences and adhering to regulations such as GDPR is paramount to building trust and ensuring the sustainability of email marketing strategies In essence digital marketing continues to ',
                            'Passion serves as the driving force behind a fulfilling and purposeful life When one sets passion as a life goal they embark on a journey that transcends mere existence shaping their actions decisions and aspirations It is the magnetic pull that propels individuals towards a life infused with enthusiasm and commitment Rather than succumbing to the mundane routine of daily existence pursuing passion ignites a vibrant flame within fostering resilience and perseverance The pursuit of passion becomes a compass guiding individuals through the labyrinth of choices and challenges steering them towards a life that resonates with personal authenticity',
                            'Embracing passion as a life goal transforms the ordinary into the extraordinary It prompts individuals to explore their innermost desires and interests giving rise to a sense of purpose that extends beyond societal expectations The alignment of ones goals with their passions creates a harmonious synergy wherein each endeavor becomes a meaningful step towards selfdiscovery and fulfillment This alignment fosters a deep connection between the individual and their pursuits cultivating a profound sense of joy and accomplishment In this context life becomes a canvas upon which the colors of passion are blended creating a masterpiece of experiences that reflect the true essence of ones aspirations',
                            'Setting passion as a life goal is a commitment to continuous growth and selfimprovement It transcends the confines of conventional success metrics urging individuals to measure their achievements against the yardstick of personal fulfillment The pursuit of passion is a dynamic process that encourages adaptability and resilience in the face of obstacles Challenges are viewed not as deterrents but as opportunities for growth learning and refining ones craft This mindset shift enables individuals to navigate the complexities of life with a sense of purpose transforming setbacks into stepping stones toward the realization of their deepest passions Ultimately embracing passion as a life goal is a transformative choice that enriches every facet of existence infusing each moment with meaning and significance',
                            'In the intricate world of coding the mind of a programmer is a fascinating nexus of genius and creativity Unlike conventional problemsolving coding requires a unique blend of analytical thinking and imaginative prowess The genius coder navigates through complex algorithms and intricate lines of code with an innate understanding of logic and structure Their mind is a finely tuned instrument capable of deciphering intricate problems and crafting elegant solutions Its a cognitive symphony where each line of code is a note carefully composed to create a harmonious and functional wholeCreativity plays a pivotal role in the coding persons mental landscape Contrary to the stereotypical image of a programmer as a logical automaton the creative coder thrives on innovation and outofthebox',
                            'The genius coders mind is akin to a constantly evolving puzzle They revel in the challenge of solving problems that seem insurmountable to others Every bug is a mystery waiting to be unraveled and every optimization is an opportunity for improvement Their mental landscape is a dynamic realm where algorithms dance and data structures interlace in a choreography of efficiency The genius coder doesnt merely see lines of code they perceive patterns anticipate potential pitfalls and architect solutions that stand the test of time'
                                        
           ]        # Choosing one of the texts randomly with the choice function
        text = random.choice(random_selection).lower()

        splitPoint = 0

        self.nameLabelLeft = Label(self.root, text=text[0:splitPoint],bg='black', fg='white',font=("Empty Trash",70))
        self.nameLabelLeft.place(relx=0.5, rely=0.5, anchor=E)
        #self.nameLabelLeft.place(x=100,y=350)

        self.nameLabelRight = Label(self.root, text=text[splitPoint:],bg='black', fg='white',font=("Times New Roman",40))
        self.nameLabelRight.place(relx=0.5, rely=0.5, anchor=W)
        #self.nameLabelRight.place(x=100,y=250)

        self.currentAlphabetLabel = Label(self.root, text=text[splitPoint], bg='black',fg='white',font=("Tekton Pro Ext",70))
        #self.currentAlphabetLabel.place(relx=0.5, rely=0.6, anchor=N)
        self.currentAlphabetLabel.place(x=1200,y=550)

        headingLabel = Label(self.root, text=f'Typing  Speed  Tester', bg='black',fg='white', font=("Cooper Black",50))
        #headingLabel.place(relx=0.5, rely=0.2, anchor=S)
        headingLabel.place(x=310,y=50)
        self.secondsLeft = Label(self.root, text=f'0 Seconds',bg='black', fg='white',font=("Forte",40))
        #self.secondsLeft.place(relx=0.5, rely=0.4, anchor=S)
        self.secondsLeft.place(x=520,y=150)

        self.writeAble = True
        self.root.bind('<Key>', self.handleKeyPress)
        

        self.secondsPassed = 0

        self.root.after(1000, self.timeAddition)  # Removed the time limit

    def stopGame(self):
        if not self.gameStopped:  # Check if the game is already stopped
            self.writeAble = False
            self.gameStopped = True  # Set the flag to indicate the game is stopped

            # Calculating the amount of words
            amountWords = len(self.nameLabelLeft.cget('text').split(' '))

            # Display result in a messagebox
            result_message = f'Your typing speed is : {amountWords} Words per minute'
            messagebox.showinfo("Typing Speed Test Result", result_message)

            # Speak the result
            self.engine.say(result_message)
            self.engine.runAndWait()

            # Destroy widgets
            self.secondsLeft.destroy()
            self.currentAlphabetLabel.destroy()
            self.nameLabelRight.destroy()
            self.nameLabelLeft.destroy()

            # Display a button to restart the game
            result_label = Label(self.root, text=result_message, fg='black')
            result_label.place(relx=0.5, rely=0.4, anchor=CENTER)

            self.showcaseResults = Button(self.root, text='Quit', command=self.destroyGame)
            self.showcaseResults.place(relx=0.5, rely=0.6, anchor=CENTER)

    def destroyGame(self):
        # Destroy result widgets
        #self.showcaseResults.destroy()
        #self.handlingLabels()
        self.root.destroy()

    def timeAddition(self):
        if self.writeAble and not self.gameStopped:  # Check if the game is still running
            self.secondsPassed += 1
            self.secondsLeft.configure(text=f'{self.secondsPassed} Seconds')

            if self.secondsPassed >= 60:
                self.stopGame()
            else:
                self.root.after(1000, self.timeAddition)  # Recursive call for the next second

    def handleKeyPress(self, event):
        pressed_key = event.char.upper()
        if pressed_key in self.buttons:
            self.buttons[pressed_key].config(bg="white", fg="black")
        
        try:
            if event.char.lower() == self.nameLabelRight.cget('text')[0].lower():
                self.nameLabelRight.configure(text=self.nameLabelRight.cget('text')[1:])
                self.nameLabelLeft.configure(text=self.nameLabelLeft.cget('text') + event.char.lower())
                self.currentAlphabetLabel.configure(text=self.nameLabelRight.cget('text')[0])

              
                # Add sound on key press
                self.play_typing_sound()
        except tkinter.TclError:
            pass

        # Bind key press event
        self.root.bind("<KeyRelease>", self.key_release)
        self.root.bind('<Key>', self.handleKeyPress)
    def key_press(self,event):
        pressed_key = event.char.lower()
        if pressed_key in self.buttons:
            self.buttons[pressed_key].config(bg="white", fg="black")
        return

    def key_release(self,event):
        released_key = event.char.upper()
        if released_key in self.buttons:
            self.buttons[released_key].config(bg="black", fg="white")
        return

 
   


# Instantiate the SpeedTester class to run the program
SpeedTester()




