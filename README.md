# Santhosh Rao M - MLE-2 Assignment

[LinkedIn](#) | [GitHub](#)

## Code that you wrote to solve the problem
[GitHub Repository Link](#)

## Inference pipeline function or hosted app link
I have developed a FastAPI app. The inference can be done through the following link: [API Endpoint](#).
You can use the `inference_nb.ipynb` notebook to pass the input URL and see the output. 
You can also deploy the app locally to get the inference.

## How long did it take to solve the problem?
8-10 hours of development time and around 4-6 hours of I/O time.

## Explain your solution
1. **Downloading and saving the PDFs**
2. **Text extraction using PyPDF2**
3. **Exploratory Data Analysis (EDA)**
4. **Model building**: Tried Logistic Regression and Random Forest with TF-IDF vectorizer
5. **Evaluation and model selection**
6. **Inference**
7. **Building a FastAPI app**
8. **Deploying it on a free-tier cloud**

## Which model did you use and why?
I used a Random Forest classifier as it provided the highest F1-Score.

## Any shortcomings and how can we improve the performance?
1. **Cross-validation**: I should have used a cross-validation set for training instead of relying solely on the test dataset.
2. **Failed downloads and extractions**: Many downloads and extractions failed. Spending more time on extracting properly downloaded PDFs would help.
3. **Feature extraction**: Current feature extraction only captures text from PDFs without differentiating between elements like headings, tables, images, emails, phone numbers, etc. Extracting these features separately could improve the model.
4. **Context capturing**: The TF-IDF vectorizer captures word-level importance but not context. Using BERT-based embeddings and pre-trained models along with proper text extraction could significantly enhance performance. For instance, documents related to lighting describe lights in detail, and BERT with sequence classification would identify these descriptions more effectively.

## Report the model's performance on the test data using an appropriate metric quantitatively
- **Train Dataset size**: 1279
- **Data loss**: 2570-1279=1291 due to download and extraction failures. 
- **Test Dataset size**: 217
- **Data loss**: 400-217=183 due to download and extraction failures.

### Test Classification Report:
```
             precision    recall  f1-score   support

       cable       0.94      1.00      0.97        64
       fuses       1.00      1.00      1.00        39
    lighting       0.98      1.00      0.99        65
      others       1.00      0.90      0.95        49

    accuracy                           0.98       217
   macro avg       0.98      0.97      0.98       217
weighted avg       0.98      0.98      0.98       217
```

## Explain why you chose this particular metric
**Chosen metric**: F1-Score

The choice of metric depends on the business context:
- **Precision**: If misclassification has significant consequences, precision should be prioritized.
- **Recall**: If missing product information is undesirable, recall should be prioritized.
- **F1-Score**: If a balance between precision and recall is needed, F1-score is preferred.

In this case, I assumed the need for a balance and therefore preferred F1-score as the primary metric.
