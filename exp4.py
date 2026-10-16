def min_edit_distance(str1, str2):
    m = len(str1)
    n = len(str2)

    # Create DP table
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    # Initialize table
    for i in range(m + 1):
        dp[i][0] = i

    for j in range(n + 1):
        dp[0][j] = j

    # Fill DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                cost = 0
            else:
                cost = 1

            dp[i][j] = min(
                dp[i - 1][j] + 1,         # Deletion
                dp[i][j - 1] + 1,         # Insertion
                dp[i - 1][j - 1] + cost   # Substitution
            )

    return dp[m][n]


dictionary = [
    "apple", "banana", "orange", "computer", "science",
    "python", "programming", "student", "language", "algorithm"
]


def spell_correct(word, dictionary):
    min_distance = float('inf')
    suggestion = word

    for correct_word in dictionary:
        distance = min_edit_distance(word.lower(), correct_word.lower())

        if distance < min_distance:
            min_distance = distance
            suggestion = correct_word

    return suggestion, min_distance


sample_text = "aple bananna scince langauge pyhton"

print("Original Text:")
print(sample_text)

print("\nCorrected Text:")

corrected_words = []

for word in sample_text.split():
    corrected_word, distance = spell_correct(word, dictionary)
    corrected_words.append(corrected_word)
    print(f"{word:10} -> {corrected_word:12} (Edit Distance = {distance})")

print("\nFinal Corrected Sentence:")
print(" ".join(corrected_words))
