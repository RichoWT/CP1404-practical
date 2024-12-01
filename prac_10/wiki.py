import wikipedia

page_title = input("Enter page title: ")
while page_title != '':
    try:
        wikipedia.search(page_title)
        page = wikipedia.page(page_title)
        print(page.title)
        print(wikipedia.summary(page.title, 5))
        print(page.url)
    except wikipedia.exceptions.PageError:
        print(f'page id "{page_title}" does not match any page. Try another id!')
    except wikipedia.exceptions.DisambiguationError as e:
        print("We need a more specific title. Try one of the following, or a new search!")
        print("(BeautifulSoup warning)")
        suggestions = wikipedia.search(page_title)
        print(suggestions)
    page_title = input("Enter page title: ")
print("thanks")