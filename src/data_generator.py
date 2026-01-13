import pandas as pd
import numpy as np

data = {
    'years_experience': np.random.randint(1, 20, 1000),
    'programming_language': np.random.choice(['Python', 'Java', 'C++'], 1000),
    'education_level': np.random.choice(['Bachelor', 'Master', 'PhD'], 1000)
}

df = pd.DataFrame(data)


base_salary = 30000
df['salary'] = base_salary + (df['years_experience'] * 5000)

df['salary'] += df['programming_language'].map({'Python': 10000, 'Java': 8000, 'C++': 12000})
df['salary'] += df['education_level'].map({'Bachelor': 0, 'Master': 5000, 'PhD': 10000})

df['salary'] += np.random.normal(0, 2000, 1000)

df.to_csv('/Users/busekoseoglu/Desktop/PROJELER/tech_talk_model_deployment/data/raw_data.csv', index=False)
