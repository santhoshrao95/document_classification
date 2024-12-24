import numpy as np
import ast

def get_random_sample(df, class_name=None):
    if class_name:
        filtered_df = df[df["target_col"] == class_name]
        if len(filtered_df) == 0:
            print(f"No samples found for class {class_name}")
            return None
        random_idx = np.random.randint(0, len(filtered_df))
        random_sample = filtered_df.iloc[random_idx]
    else:
        random_idx = np.random.randint(0, len(df))
        random_sample = df.iloc[random_idx]

    print("Random Document Sample:")
    print("-" * 50)
    print("\nText Content:")
    print("-" * 50)
    print(random_sample["text"])
    print("-" * 50)
    print(f"Label: {random_sample['target_col']}")

    return random_sample["text"], random_sample["target_col"]


def ast_df(df):
    try:
        for column in df.columns:
            df[column] = df[column].apply(ast.literal_eval)
    except (ValueError, SyntaxError) as e:
        print(f"Note: ast.literal_eval not needed or failed: {str(e)}")
