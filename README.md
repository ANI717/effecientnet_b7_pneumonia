<p align="center">
  <h1 align="center">Pneumonia Detection in Chest X-ray Image with EfficientNet-B7</h1>
</p>

Google has published both a very exciting paper and source code for a newly designed CNN called EfficientNet, that set new records for both accuracy and computational efficiency over most popular CNNs on ImageNet dataset. Among them, EfficientNet-B7 (which achieved highest accuracy over ImageNet dataset) is used here to solve a classsification problem, detection of Pneumonia in Chest X-ray Images. Without any augmentation, 100% precision can be achieved. <br />

## Database
Kermany D., Goldbaum M., Cai W. Large dataset of labeled optical coherence tomography (OCT) and chest X-Ray images 2018, 172, 1122–1131. Cell. 2018;172:1122–1131. doi: 10.1016/j.cell.2018.02.010.
https://data.mendeley.com/datasets/rscbjbr9sj/3 <br />
```
Unzip ZhangLabData.zip
Copy it to "./data/" directory
```
Training Dataset:
```
Total Images: 5233
Normal Healthy Person: 1349
Pnumonia Patients: 3884
```
Testing Dataset:
```
Total Images: 624
Normal Healthy Person: 234
Pnumonia Patients: 390
```
Validation Dataset is created from Training Dataset for calibrating Hyperparameters.

## Codebase
Driver Program
```
train.py = runs training session
test.py = runs testing session
folder_to_csv.py = lists files in a folder
merge_csv.py = merges contents in CSV files
augmentation.py = creates augmented dataset
```
Setting File
```
settings.json = contains hyperparameters
```
Utility Classes
```
_datagen.py = data generator for deep learning session
_train_test.py = runs deep learning session
```
EfficientNet by Luke Melas-Kyriazi
https://github.com/lukemelas/EfficientNet-PyTorch
```
./efficientNet/
```

## Result
Plain Data (No Augmentation)
```
Accuracy = 87.98%
Precision = 100%
Recall = 83.87%
F1 Score = 91.23
```
