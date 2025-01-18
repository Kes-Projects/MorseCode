from tkinter import *

morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
    ',': '--..--', '.': '.-.-.-', '?': '..--..', "'": '.----.',
    '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-',
    '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-',
    '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.',
    '$': '...-..-', '@': '.--.-.', ' ': '/'
}

def reset():
    """Resets all user input and text displayed"""
    text_bar.delete("1.0", END)
    display_text.config(state=NORMAL)
    display_text.delete("1.0", END)
    display_text.config(state=DISABLED)

def encrypt():
    """Converts text to morse code"""
    text = text_bar.get("1.0", END).strip()
    text_bar.delete("1.0", END)

    if text:
        if any(char in text for char in ['.', '-']):
            display_text.config(state=NORMAL)
            display_text.delete("1.0", 'end')
            display_text.insert('1.0', "Text is already in Morse code.")
            display_text.tag_add("center", "1.0", "end")
            display_text.config(state=DISABLED)
        else:
            encrypted_text = " ".join(morse_code_dict[char] for char in text.upper() if char in morse_code_dict)
            display_text.config(state=NORMAL)
            display_text.delete("1.0", END)
            display_text.insert(END, encrypted_text)
            display_text.tag_add("center", "1.0", "end")
            display_text.config(state=DISABLED)

    else:
        display_text.config(state=NORMAL)
        display_text.delete("1.0", END)
        display_text.insert(END, "Please enter text to encode")
        display_text.tag_add("center", "1.0", "end")
        display_text.config(state=DISABLED)

def decrypt():
    """Converts morse code back into text"""
    morse_code = text_bar.get("1.0", END).strip()
    text_bar.delete("1.0", END)
    if morse_code:
        reverse_morse_code_dict = {value: key for key, value in morse_code_dict.items()}
        words = morse_code.split('   ')
        decrypted_text = []

        try:
            for word in words:
                letters = word.split(' ')
                decrypted_word = ''.join(reverse_morse_code_dict[letter] for letter in letters)
                decrypted_text.append(decrypted_word)
                print(decrypted_text)
            display_text.config(state=NORMAL)
            display_text.delete("1.0", END)
            display_text.tag_add("center", "1.0", "end")
            display_text.insert(END, ' '.join(decrypted_text).lower())
            display_text.config(state=DISABLED)
        except KeyError:
            display_text.config(state=NORMAL)
            display_text.delete("1.0", END)
            display_text.insert(END, "Invalid morse code")
            display_text.tag_add("center", "1.0", "end")
            display_text.config(state=DISABLED)
    else:
        display_text.config(state=NORMAL)
        display_text.delete("1.0", END)
        display_text.insert(END, "Please input a Morse Code to decode")
        display_text.tag_add("center", "1.0", "end")
        display_text.config(state=DISABLED)




BACKGROUND_COLOR = "#ADD8E6"

# Create the main window
window = Tk()
window.title("Morse Code Converter")
window.config(pady=30, padx=30, background=BACKGROUND_COLOR)

# Create a canvas for the background image and title
canvas = Canvas(width=800, height=526, highlightthickness=0, background=BACKGROUND_COLOR)
screen_image = PhotoImage(file="./images/Screen.png")
screen = canvas.create_image(400, 263, image=screen_image)

# Create a text to display user text input to decode or encode
display_text = Text(window,
                    width=80,
                    height=15,
                    font=("Arial", 20, 'bold'),
                    wrap="word")
display_text.grid(column=0, row=0, columnspan=3, pady=20)
display_text.config(state=DISABLED)
display_text.tag_config("center", justify="center")



# Create a text input bar
text_bar = Text(width=60, height=5, font=("Ariel", 15, 'normal'))
text_bar.grid(column=0, row=1, columnspan=3, pady=20)
text_bar.focus()

# Create buttons and align them
encode_button = Button(width=10,
                       height=2,
                       text="ENCODE",
                       font=("Ariel", 14, "bold"),
                       highlightthickness=0,
                       command=encrypt)
encode_button.grid(column=0, row=2, padx=10, pady=10, sticky="ew")

exit_button = Button(width=10,
                      height=2,
                      text="RESET",
                      font=("Ariel", 14, "bold"),
                      highlightthickness=0,
                      command=reset)
exit_button.grid(column=1, row=2, padx=10, pady=10, sticky="ew")

decode_button = Button(width=10,
                       height=2,
                       text="DECODE",
                       font=("Ariel", 14, "bold"),
                       highlightthickness=0,
                       command=decrypt)
decode_button.grid(column=2, row=2, padx=10, pady=10, sticky="ew")

#Configure column weights for proportional resizing
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)
window.grid_columnconfigure(2, weight=1)


window.mainloop()