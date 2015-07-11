from sys import argv


class WordsTweeted:
  def __init__(self, input_filename, output_filename):
    self.input_filename = input_filename
    self.output_filename = output_filename
    self.words = {}

  def read_file(self):
    input_file = open(self.input_filename)
    return input_file.read()

  def write_occurences(self):
    content = self.read_file()
    self.count_occurences(content)
    self.wrtie_to_file()

  def count_occurences(self, content):
    for word in content.split():
      if word in self.words:
        self.words[word] += 1
      else:
        self.words[word] = 1

  def wrtie_to_file(self):
    output_file = open(self.output_filename, 'w')
    for word in sorted(self.words):
      output_file.write("{}    {}".format(word, self.words[word]))
      output_file.write("\n")
    output_file.close()


script, input_filename, output_filename = argv

words_tweeted = WordsTweeted(input_filename, output_filename)
words_tweeted.write_occurences()