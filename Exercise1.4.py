import pandas as pd

# 1. Ladda filen
file_path = 'Exercise_4_Advanced_Student_Scores.txt'
# Antag att filen har kolumner: "Student" och "Score"
data = pd.read_csv(file_path)  

# 2. Funktion för att gruppera studenter baserat på deras resultat
def categorize_students(score):
    if score > 85:
        return 'A'
    elif 70 <= score <= 85:
        return 'B'
    else:
        return 'C'

data['Category'] = data['Score'].apply(categorize_students)

# 3. Generera sammanfattningsrapport
summary = []
categories = ['A', 'B', 'C']

for category in categories:
    category_data = data[data['Category'] == category]
    total_students = len(category_data)
    average_score = category_data['Score'].mean() if total_students > 0 else 0
    student_names = ', '.join(category_data['Name'].tolist())
    
    summary.append({
        'Category': category,
        'Total Students': total_students,
        'Average Score': round(average_score, 2),
        'Students': student_names
    })

summary_df = pd.DataFrame(summary)

# Visa rapporten i konsolen
print("Sammanfattningsrapport:")
print(summary_df)

# 4. Exportera rapporten till en CSV-fil
output_file = 'Student_Scores_Report.csv'
summary_df.to_csv(output_file, index=False)
print(f"Rapporten har exporterats till {output_file}")
