def load_questions(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:  # Specifierar utf-8 kodning
            questions = []
            for line in file:
                parts = line.strip().split(';')
                questions.append({
                    'question': parts[0],
                    'options': parts[1:-1],
                    'correct_answer': int(parts[-1])
                })
            return questions
    except FileNotFoundError:
        print(f"Fil {filename} hittades inte, skapar en tom fil.")
        with open(filename, 'w', encoding='utf-8') as file:  # Även här specifierar vi utf-8
            pass  # Skapa en tom fil
        return []


def run_quiz(questions):
    if not questions:
        print("Inga frågor att visa. Lägg till frågor i filen och kör programmet igen.")
        return

    score = 0
    total = len(questions)
    for q in questions:
        print(q['question'])
        for i, option in enumerate(q['options'], 1):
            print(f"{i}. {option}")
        try:
            answer = int(input("Ditt svar: "))
            if answer == q['correct_answer']:
                score += 1
                print("Rätt svar!\n")
            else:
                print(f"Fel, rätt svar var {q['options'][q['correct_answer']-1]}\n")
        except ValueError:
            print("Ogiltigt svar, vänligen ange ett nummer.\n")

    print(f"Du fick {score} av {total} rätt.")

def main():
    filename = 'quiz.txt'
    questions = load_questions(filename)
    run_quiz(questions)

if __name__ == "__main__":
    main()
