from stats import count_words , get_book_text , display_counter, list_dict
import sys

def main():
    try:
        if sys.argv[1] is not None:
            book_path = sys.argv[1]
            freq_count,num_words = get_book_text(book_path)
            print("============ BOOKBOT ============")
            print(f"Analyzing book found at {book_path}...")
            list_dict(freq_count,num_words)
    except:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

if __name__ == "__main__":
    main()


