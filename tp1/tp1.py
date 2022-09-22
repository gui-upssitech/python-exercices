from pprint import pprint
import re



def main(pre_treated: bool, num_results: int = 10, type_delimiter: str = "", n: int = 1):
    # Step 1 : load file
    path = "alice-pre.txt" if pre_treated else "alice.txt" 
    file_contents = get_file_contents(path)

    # Step 2 : convert file to word list
    if pre_treated:
        # This method allows to specify a word type to filter with in addition to removing whitespace
        word_list = replace_with_root_word(file_contents, type_delimiter)
    else:
        word_list = ngram(remove_whitespace(file_contents), n)

    # Step 3 : convert to dictionnary with words as keys and number of occurences as values
    word_count = count_word_occurences(word_list)

    # Step 4 : sort dict by value and return n highest entries
    n_highest = get_n_highest(word_count, num_results)
    pprint(n_highest)
        

def ngram(word_list: list[str], n: int):
    new_list = []
    for i in range(n-1, len(word_list) + 1):
        new_list.append(" ".join(word_list[i-n:i]))
    
    return new_list

    
def get_n_highest(word_dict: dict[str, int], n: int) -> list[tuple[str, int]]:
    # convert dict to tuple list and sort by num occurences 
    sorted_items = sorted(word_dict.items(), key=lambda item: item[1])
    
    # retirieve the n highest entries
    n_highest = []
    for i in range(n):
        n_highest.append(sorted_items[-(i+1)])

    return n_highest



def count_word_occurences(word_list: list[str]) -> dict[str, int]:
    dic = {}

    for word in word_list:
        if word not in dic:
            dic[word] = 0
        dic[word] += 1

    return dic



def replace_with_root_word(text: str, type_delimiter: str = "") -> list[str]:
    new_list = []

    # for each line
    for line in text.split("\n"):
        # split the line into its 3 components : word word_type word_root
        split = re.sub(r"\s+", " ", line.strip()).split(" ")

        # remove broken entries (less than 3 things) and punctuation
        if len(split) != 3 or re.match(r"\W+", split[0]):
            continue

        # added option to filter the words by word type
        if type_delimiter != "" and split[1] != type_delimiter:
            continue

        # add word root to list (or original word if no word root is present)
        word = split[2] if split[2] != "<unknown>" else split[0]
        new_list.append(word)
    
    return new_list



def remove_whitespace(text: str) -> list[str]:
    # this method uses a regex to convert a succession on non word characters into a single space char
    # the text is then converted to a list by splitting by space

    rnw_content = re.sub(r"\W+", " ", text.strip())
    return rnw_content.split(" ")



def get_file_contents(path: str) -> str:
    content = ""

    with open(path, "r") as f:
        content = f.read()

    return content



if __name__ == "__main__":
    # main(False, n=3)
    main(True, type_delimiter="VB", num_results=20)