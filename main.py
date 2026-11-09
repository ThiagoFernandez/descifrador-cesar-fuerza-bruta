import argparse

def create_parser():
    p = argparse.ArgumentParser(description="cesar decypher")
    p.add_argument("-t", "--text", type=str, required=True ,help="text to decypher")
    args = p.parse_args()
    return args

def get_possibilities(text: str) -> dict[int, str]:
    possibilities = {} # key=shift, value=decrypted text
    words = text.split()
    for shift in range(1, 26):
        possible_text = "" # one line for each shift
        for i in range(len(words)): 
            decrypted_word = ""  # one word for each one in words
            for char in words[i]: # iterate the word
                if char.isalpha():
                    shifted = ord(char) - shift 
                    if char.islower():
                        if shifted < ord('a'):
                            shifted += 26 #fix the shift
                    elif char.isupper():
                        if shifted < ord('A'):
                            shifted += 26 #fix the shift
                    decrypted_word += chr(shifted)
                else:
                    decrypted_word += char # added the char to the word
            possible_text+=decrypted_word # added the word to the line
            possible_text+=" " # added a space between words
        possibilities[shift]=possible_text # added the line
    return possibilities

def read_results(results)->None:
    for k,v in results.items():
        print(f"shift: {k} | text: {v}")

def main():
    args = create_parser()
    text = args.text
    results = get_possibilities(text)
    read_results(results)

if __name__ == "__main__":
    main()