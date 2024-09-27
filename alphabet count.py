from collections import Counter
import string
import matplotlib.pyplot as plt

def letterCount(paragraf):
    paragraf = paragraf.lower()
    onlyLetter = [char for char in paragraf if char in string.ascii_lowercase]
    countLetter = Counter(onlyLetter)
    return countLetter, len(onlyLetter)

def plot_freq(countLetter, letterTotal):
    letters = sorted(countLetter.keys())
    freq = [countLetter[letter] for letter in letters]
    percentages = [(count/letterTotal) * 100 for count in freq]

    bars = plt.bar(letters, freq, color='skyblue')
    plt.xlabel('Letters')
    plt.ylabel('Frequency')
    plt.title('Letter Frequency in a Paragraph')
    
    for bar, percentage in zip(bars, percentages):
        valueY = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, valueY, f'{percentage:.2f}%', va='bottom', ha='center', fontsize=8, color='black')
    
    plt.show()


paragraf = input("Enter a paragraph: ")
letter_freq, letterTotal= letterCount(paragraf)

plot_freq(letter_freq, letterTotal)

for letter, count in letter_freq.items():
    print(f"{letter}: {count}")