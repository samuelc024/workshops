# evaluate_competition.py
import pandas as pd
import Final as final

if __name__ == "__main__":
    print("Generando predicciones para la competencia...")
    submission = final.predict_test_set()
    print("Submission file creado: submission.csv")