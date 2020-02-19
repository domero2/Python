

class onbutton():
    def __init__(self):
        pass

    def click(self, entry, entry2):
        print('Button clicked: ' + entry + ' ' + entry2)

    def searching_results(self,object,text):
        for item in object:
            #label['text'] = '\n'.join(item) if you want use label agianst text
            text.insert(1.0,'\n'.join(item))

    def clear_content(self,text, command):
        text.delete(1.0, command)
