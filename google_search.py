import webbrowser
import wikipedia

def search(command):
    
    term = command.replace("search", "")
    term = term.replace("google", "")

    webbrowser.open_new(f"https://google.com/search?q={term}")
    result = wikipedia.summary(term, sentences=3)
    ret = f"Here is what I found for {term} on Google {result}"
    return ret