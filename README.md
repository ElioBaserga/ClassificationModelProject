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

## Data Augmentation
| Augmentation                     | Description |
|-----------------------------------|-------------|
| `RandomPerspective(distortion_scale=0.5, p=0.5)`          | Applies a random perspective transformation to the image with a probability of 0.5. |
| `GaussianBlur(kernel_size=3, sigma=(0.1, 2.0))`          | Applies a blur to the image |
| `RandomHorizontalFlip()`          | Randomly flips the image horizontally with a probability of 0.5. |
| `RandomRotation(30)`              | Rotates the image randomly within a range of ±30 degrees. |
| `ColorJitter(brightness=0.2, contrast=0.2, saturation=0.2, hue=0.2)` | Randomly alters brightness, contrast, saturation, and hue within the specified limits. |
| `RandomResizedCrop(224)`          | Randomly crops and resizes the image to 224×224 pixels. |
| `RandomAffine(degrees=30, translate=(0.1, 0.1))` | Applies a random affine transformation, with rotation within ±30 degrees and translation up to 10% of the image dimensions. |

## Model Training

### Data Splitting Method (Train/Validation/Test)
A total of 3825 images from 36 fruits and vegetables were used for training, validation, and testing, split approximately as follows:  
80% for training, 10% for validation, and 10% for testing.

| Split      | Number of Rows |
|------------|---------------:|
| Train      | 3115          |
| Validation | 351           |
| Test       | 359           |

## Training

| Epoch | Training Loss | Validation Loss | Accuracy |
|-------|---------------|-----------------|----------|
| 1     | 1.6402        | 0.4357          | 90.03%   |
| 2     | 0.9837        | 0.3048          | 91.74%   |
| 3     | 0.8899        | 0.2703          | 91.74%   |
| 4     | 0.8108        | 0.2568          | 91.74%   |
| 5     | 0.7973        | 0.2520          | 91.74%   |

### TensorBoard

Details of training can be found at [Huggingface TensorBoard](https://huggingface.co/ElioBaserga/fruits-and-vegetables-vit/tensorboard)

| Model/Method                                                         | TensorBoard Link                                      |
|----------------------------------------------------------------------|------------------------------------------------------|
| Transfer Learning with `google/vit-base-patch16-224` (without data augmentation) | runs/May14_22-52-45_ip-10-192-12-66                    |
| Transfer Learning with `google/vit-base-patch16-224` (with data augmentation)  | runs/May15_06-55-05_ip-10-192-12-251                    |

## Results
| Model/Method                                                         | Accuracy | Precision | Recall |
|----------------------------------------------------------------------|----------|-----------|--------|
| Transfer Learning with `google/vit-base-patch16-224` (without data augmentation) | 95.26%      | -         | -      |
| Transfer Learning with `google/vit-base-patch16-224` (with data augmentation)  | 91.64%      | -         | -      |
| Zero-shot Image Classification with `openai/clip-vit-large-patch14` | %      | %    | %    |
