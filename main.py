def countText(file_content):
  words = file_content.split()
  return len(words)

def countChar(text):
  dict = {}

  for char in text:
    if char.isalpha():
      if char.lower() in dict:
        dict[char.lower()] += 1
      else:
        dict[char.lower()] = 1
  return dict

def main():
  with open("books/frankenstein.txt") as f:
    file_contents = f.read()
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{countText(file_contents)} words found in the document")

    for key,val in countChar(file_contents).items():
      print(f"The '{key}' character was found {val} times")
    
    print("--- End report ---")

main()