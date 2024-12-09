def input_data():
    return input("Введите текст: ")

def generate_data():
    import random
    words = ["example", "text", "generation", "random", "words", "vowels", "consonants"]
    return " ".join(random.choices(words, k=random.randint(5, 15)))

def process_data(data):
    words = re.findall(r'\b\w+\b', data)  # Извлечение слов
    vowels = "aeiouyAEIOUY"
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"

    total_vowels = sum(1 for char in data if char in vowels)
    result = []
    for word in words:
        num_vowels = sum(1 for char in word if char in vowels)
        num_consonants = sum(1 for char in word if char in consonants)
        result.append((word, num_vowels, num_consonants, total_vowels))
    return result

def display_result(result):
    print("\nРезультат обработки текста:")
    for word, vowels_count, consonants_count, total_vowels in result:
        print(f"Слово: {word}, Гласные: {vowels_count}, Согласные: {consonants_count}, Всего гласных в тексте: {total_vowels}")