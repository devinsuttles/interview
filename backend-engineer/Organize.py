class MyException (Exception):
    """Exciption class to implement exception raise testing
    """
    pass

class Organize:
    def __init__(self):
        """Class constructor
        """
        self.dictionary = {}

    def insert(self, text):
        """Insert method that takes the given text looks for number value
        to use for the key of the dictionary 
        Args:
            text (str): short string
        """
        if text:
            num = ''.join(filter(lambda c: c.isdigit(), text))
            word = ''.join(filter(lambda c: not c.isdigit(), text)).strip(' ')
            if num != '':
                num = int(num)
            else: 
                num = 0
            if num in self.dictionary:
                arr = self.dictionary[int(num)]
                arr.append(word)
                self.dictionary[num] = arr
            else:
                arr = [word]
                self.dictionary[num] = arr
        elif not text or text == '':
            raise MyException("Insert must not be None or Empty String")

    def search(self, num):
        """Search function that looks up the list of words

        Args:
            num (int): key value of the look up table

        Returns:
            list:string: returns an array of strings
        """
        if num in self.dictionary:
            return self.dictionary[num]
        return None

    def sort_shortWords(self, num):
        """Will sort the given values at different intervals

        Args:
            num (int): key value provided for lookup on dictionary
        """
        if num in self.dictionary:
            arr = self.dictionary[num]

            new_arr = sorted(arr, key = str.lower)
            self.dictionary[num] = new_arr

    def txt_fileGenerator(self):
        """Function that helps generate file of string of words sorted by numerics than alphabetically
        """
        output_file = open('output.txt', 'w')

        keys_inOrder = list(self.dictionary.keys())
        keys_inOrder.sort()
        for num in keys_inOrder:
            self.sort_shortWords(num)
            result = ''

            arr = self.dictionary[num]
            for i in range(0, len(arr)):
                result += arr[i]
                if i != len(arr)-1:
                    result += ', '
            output_file.writelines(str(num)+' '+result.strip()+'\n')
        output_file.close()