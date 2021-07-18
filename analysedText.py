# From Course 2 Week 3 Objects & Classes Lab Exercise

class analysedText(object):
    
    def __init__ (self, text):
        self.wordoccurrences = {}
        self.fmtText = ""
        self.words = []
        self.allowedchars = "abcdefghijklmnopqrstuvwxyz "    # allowed characters
        
        # first, make text parameter lowercase
        text = text.lower()
        
        # for each text character, is it an allowed character? if so, add to fmtText string
        for c in text:
            if c in self.allowedchars:
                self.fmtText = self.fmtText + c

        # split the string and store in a list
        self.words = self.fmtText.split()
        
        # for each word in the list, track the occurrences with a dictionary
        for w in self.words:
            if w not in self.wordoccurrences:
                self.wordoccurrences[w] = 0
            self.wordoccurrences[w] = self.wordoccurrences[w] + 1
    
    def freqAll(self):        
        # return our dictionary object
        return self.wordoccurrences
            
    
    def freqOf(self,word):
        # using the word parameter as a key, return the occurrence of that word
        return(self.wordoccurrences[word])

