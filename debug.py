from src.pipeline.predict_pipeline import CustomData, PredictPipeline
import pandas as pd

data=CustomData(
    gender="male",
    race_ethnicity="group B",
    parental_level_of_education="associate's degree",
    lunch="standard",
    test_preparation_course="none",
    reading_score=65.0,
    writing_score=50.0
)

pred_df = data.get_data_as_data_frame()
print(pred_df)

try:
    predict_pipeline = PredictPipeline()
    results = predict_pipeline.predict(pred_df)
    print("Results:", results)
except Exception as e:
    import traceback
    traceback.print_exc()
