import itertools

# Defining the books and subjects
math_books = ['Math1', 'Math2', 'Math3', 'Math4', 'Math5']
english_books = ['English1', 'English2', 'English3']
urdu_books = ['Urdu1', 'Urdu2']

subjects = ['Math', 'English', 'Urdu']

# Step 1: Arrange the subjects (Math, English, Urdu)
subject_arrangements = itertools.permutations(subjects)

# Step 2: Arrange the books within each subject
math_book_arrangements = itertools.permutations(math_books)
english_book_arrangements = itertools.permutations(english_books)
urdu_book_arrangements = itertools.permutations(urdu_books)

# Step 3: Combine the arrangements
arrangement_count = 0
for subject_order in subject_arrangements:
    for math_order in itertools.permutations(math_books):
        for english_order in itertools.permutations(english_books):
            for urdu_order in itertools.permutations(urdu_books):
                # Merge the arrangements based on subject order
                arrangement = []
                for subject in subject_order:
                    if subject == 'Math':
                        arrangement.extend(math_order)
                    elif subject == 'English':
                        arrangement.extend(english_order)
                    elif subject == 'Urdu':
                        arrangement.extend(urdu_order)
                
                # Print the arrangement
                arrangement_count += 1
                print(f"Arrangement {arrangement_count}: {arrangement}")

# Let the user know how many arrangements were generated
print(f"Total arrangements: {arrangement_count}")
