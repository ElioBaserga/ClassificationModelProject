# Fruits and Vegetable Classifier

## Project Description
This project classifies different fruits and vegetables.

### Name & URL
| Name          | URL |
|---------------|-----|
| Huggingface   | [Huggingface Space]() |
| Model Page    | [Huggingface Model Page](https://huggingface.co/ElioBaserga/fruits-and-vegetables-vit) |
| Code          | [GitHub Repository](https://github.com/ElioBaserga/ClassificationModelProject) |

## Labels
The different fruits and vegetables are:  
`['apple', 'banana', 'beetroot', 'bell pepper', 'cabbage', 'capsicum', 'carrot', 'cauliflower', 'chilli pepper', 'corn', 'cucumber', 'eggplant', 'garlic', 'ginger', 'grapes', 'jalepeno', 'kiwi', 'lemon', 'lettuce', 'mango', 'onion', 'orange', 'paprika', 'pear', 'peas', 'pineapple', 'pomegranate', 'potato', 'raddish', 'soy beans', 'spinach', 'sweetcorn', 'sweetpotato', 'tomato', 'turnip', 'watermelon']`

## Data Source
| Data Source | Description |
|-------------|-------------|
| [Fruits and Vegetables](https://www.kaggle.com/datasets/kritikseth/fruit-and-vegetable-image-recognition/data) | Original dataset from Kaggle containing 36 different fruits and vegetables in total. |

## Model Training

### Data Splitting Method (Train/Validation/Test)
A total of 3825 images from 36 fruits and vegetables were used for training, validation, and testing, split approximately as follows:  
80% for training, 10% for validation, and 10% for testing.

| Split      | Number of Rows |
|------------|---------------:|
| Train      | 3115          |
| Validation | 351           |
| Test       | 359           |

### TensorBoard

Details of training can be found at [Huggingface TensorBoard](https://huggingface.co/ElioBaserga/fruits-and-vegetables-vit/tensorboard)

| Model/Method                                                         | TensorBoard Link                                      |
|----------------------------------------------------------------------|------------------------------------------------------|
| Transfer Learning with `google/vit-base-patch16-224` (without data augmentation) | runs/May14_22-52-45_ip-10-192-12-66                    |
| Transfer Learning with `google/vit-base-patch16-224` (with data augmentation)  | -                    |

## Results
| Model/Method                                                         | Accuracy | Precision | Recall |
|----------------------------------------------------------------------|----------|-----------|--------|
| Transfer Learning with `google/vit-base-patch16-224` (without data augmentation) | 95.26%      | -         | -      |
| Transfer Learning with `google/vit-base-patch16-224` (with data augmentation)  | %      | -         | -      |
| Zero-shot Image Classification with `openai/clip-vit-large-patch14` | %      | %    | %    |
