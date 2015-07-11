from sys import argv

class MedianUnique:
  def __init__(self, input_filename, output_filename):
    self.input_filename = input_filename
    self.output_filename = output_filename
    self.data = []

  def read_file(self):
    input_file = open(self.input_filename)
    return input_file.readlines()

  def calculate_median(self, data):
    data = sorted(data)
    if len(data) < 1:
      return None
    if len(data) %2 == 1:
      return data[((len(data)+1)/2)-1]
    else:
      return (sum(data[(len(data)/2)-1:(len(data)/2)+1]))/2.0
  

  def wrtie_to_file(self, content_array):
    output_file = open(self.output_filename, 'w')
    for content in content_array:
      words = content.split()
      self.data.append(len(set(words)))
      output_file.write("{}".format(self.calculate_median(self.data)))
      output_file.write('\n')
    output_file.close()

  def write_median(self):
    content_array = self.read_file()
    self.wrtie_to_file(content_array)


script, input_filename, output_filename = argv

median_unique = MedianUnique(input_filename, output_filename)
median_unique.write_median()