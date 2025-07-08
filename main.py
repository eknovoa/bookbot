from stats import get_num_words, get_times_each_char, sort_dict
import sys

def get_book_text(filepath):
  with open(filepath) as f:
    return f.read()

def main():
  if len(sys.argv) != 2:
    print('Usage: python3 main.py <path_to_book>')
    sys.exit(1)
  

  contents = get_book_text(sys.argv[1])
  
  result = get_times_each_char(contents)
  
  print("============ BOOKBOT ============")
  print("Analyzing book found at books/frankenstein.txt...")
  print("----------- Word Count ----------")
  words = get_num_words(contents)
  print(f'Found {words} total words')
  print("--------- Character Count -------")

  sorted_result = sort_dict(result)
  for key,value in sorted_result.items():
    if key.isalpha():
      print(f'{key}: {value}')
  print("============= END ===============")

main()