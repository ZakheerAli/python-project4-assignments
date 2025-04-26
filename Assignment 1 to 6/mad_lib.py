def main():
    noun = input("Enter a noun (person/place/thing): ")
    verb = input("Enter a verb (e.g., run, eat, jump): ")
    adjective = input("Enter an adjective (e.g., funny, loud, small): ")
    adverb = input("Enter an adverb (e.g., quickly, slowly, loudly): ")

    story = f"One day, a {adjective} {noun} decided to {verb} {adverb}. It was the weirdest thing anyone had ever seen!"

    print("\nYour Mad Libs story:")
    print(story)

if __name__ == "__main__":
    main()
