

class onbutton():
    def __init__(self):
        pass

    def click(self, entry, entry2):
        print('Button clicked: ' + entry + ' ' + entry2)

    def searching_results(self,object,label):
        for item in object:
            label['text'] = '\n'.join(item)

