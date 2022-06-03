# FlashCards
A GUI usking Tkinter that aids in the learning of languages through flash cards. 


Welcome to the FlashCards GUI! 

![image](https://user-images.githubusercontent.com/69131452/171783656-3ea085c7-3c31-402a-8ca3-2e4a61979a7a.png)
![image](https://user-images.githubusercontent.com/69131452/171783687-b26d57de-39ce-4de9-9666-43ef61309468.png)

This is a GUI made entirely from Python 3 using the Tkinter library. It takes records (english-french word pairs) from a csv file, and saves the progress (words that user got wrong) in a different csv file. 

# How Does It Work 
Once the user runs the GUI, a flashcard showing a french word will show. User then has 3 seconds to guess the English translation for it. If the user gets it correct, they can press the correct button - that word will then be removed from the database so it does not show up again. If the user gets it wrong, the word will remain in the database until it is randomly chosen again. 
