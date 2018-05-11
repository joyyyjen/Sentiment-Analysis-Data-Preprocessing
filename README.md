# sentiment_analysis_prepro

Term Project for LING 406
Sentiment Analysis Text Preprossed
- This program do text preprossed and output text file for further sentiment analysis application

It's a python program. (Idealy python3)
- using library os, punctuation from string, stopwords from nltk.corpus, word_tokenize from nltk.tokenize, and pos_tag from nltk

### 1. How to run?
- If you are using Mac, open Terminal
  1. If you are considering first step text preprocessing , run ./prepro1.py
  2. If you are considering doing POS taggingg, run, ./prePOS.py
- Note: both script used the defalut dataset.

### 2. Double check the python path in your environment
- mine is in /usr/local/bin/python3
- After executed, if you received this error: "No such file or directory"
- try changing the first line #!/usr/local/bin/python3 to #!/usr/bin/python3 

### 3. How does it work?
- Both program reads the text directory "txt_sentoken_def" and modified the textfile
- After executed prepro1.py,a new directory called "txt_sentoken" will be created
- After executed prePOS.py, a new directory called "txt_sentoken2" will be created
- It will print file ID it currently on when the sript is running 

