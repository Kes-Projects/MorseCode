
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


def encrypt(text):
    """Converts text to morse code"""
    encryption = " ".join(morse_code_dict[char] for char in text.upper())
    return encryption

def decrypt(morse_code):
    """Converts morse code back into text"""
    reverse_morse_code_dict = {value: key for key, value in morse_code_dict.items()}

    words = morse_code.split('   ')
    decrypted_text = []

    for word in words:
        letters = word.split(' ')
        decrypted_word = ''.join(reverse_morse_code_dict[letter] for letter in letters)
        decrypted_text.append(decrypted_word)

    return ' '.join(decrypted_text).lower()


