import random

def is_valid_word(word, word_list):
  """Checks if a word is valid (all lowercase letters and exists in the word list)."""
  return word.isalpha() and word.islower() and word in word_list

def main():
  # Set the desired word length and number of words to form
  word_length = 6
  num_words = 5

  # Load a word list (replace "words.txt" with your own file path if desired)
  try:
    with open("words.txt", "r") as file:
      word_list = set(line.strip().lower() for line in file)
  except FileNotFoundError:
    print("Error: Word list file 'words.txt' not found. Please create or provide the correct path.")
    return

  # Ensure word list contains words of the desired length
  valid_words = [word for word in word_list if len(word) == word_length]
  if len(valid_words) < 1:
    print("Error: Word list does not contain enough words of desired length", word_length)
    return

  # Start the game
  print("Welcome to Mystery Word Chain!")
  print(f"Try to form a chain of {num_words} words, each starting with the last letter of the previous.")
  print(f"Words must be {word_length} letters long.")

  # Generate the first random word
  current_word = random.choice(valid_words)
  print(f"Starting word: {current_word}")

  # Track formed words and user input
  formed_words = [current_word]
  for _ in range(num_words - 1):
    while True:
      new_word = input("Enter a word starting with " + current_word[-1] + ": ").lower()
      if is_valid_word(new_word, word_list) and len(new_word) == word_length and new_word not in formed_words:
        formed_words.append(new_word)
        current_word = new_word
        break
      else:
        print("Invalid word. Please try again.")

  # Display the results
  if len(formed_words) == num_words:
    print("Congratulations! You formed a chain of", num_words, "words:")
    for word in formed_words:
      print(word)
  else:
    print("You got stuck! The chain ended at", len(formed_words), "words.")
    print("Formed words:", ", ".join(formed_words))

if __name__ == "__main__":
  main()
