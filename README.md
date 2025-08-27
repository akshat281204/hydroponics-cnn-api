# Spinach Disease Classifier

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-orange?logo=tensorflow)
![Gradio](https://img.shields.io/badge/Gradio-3.x-purple?logo=gradio)
![License](https://img.shields.io/badge/License-MIT-green)

This repository hosts a web-based application that utilizes a Convolutional Neural Network (CNN) to classify the health status of spinach leaves. Users can upload an image of a spinach leaf, and the application will predict whether it exhibits signs of 'Leaf Spot', 'Mite Damage', or is 'Healthy'. The interactive user interface is built with Gradio, making it easy to use for rapid assessment.

## Table of Contents

-   [Features](#features)
-   [Project Structure](#project-structure)
-   [Dependencies](#dependencies)
-   [Installation](#installation)
-   [Usage](#usage)
-   [API Documentation (Gradio Interface)](#api-documentation-gradio-interface)
-   [Model Details](#model-details)
-   [Contributing](#contributing)
-   [License](#license)

## Features

*   **Spinach Disease Classification:** Accurately identifies three distinct categories: 'Leaf Spot', 'Healthy', and 'Mite Damage'.
*   **User-Friendly Interface:** An intuitive web interface built with Gradio allows for simple image uploads and clear display of prediction results.
*   **Deep Learning Powered:** Employs a pre-trained Convolutional Neural Network (CNN) (`spinach_disease_classifier.h5`) for robust image analysis and classification.
*   **Real-time Predictions:** Provides immediate classification outcomes upon image submission.
*   **Confidence Scores:** Displays the probability score for each potential class, offering insights into the model's certainty.

## Project Structure

```
hydroponics-cnn-api/
├── .gitattributes
├── .gitignore
├── app.py
├── models/
│   └── spinach_disease_classifier.h5
└── requirements.txt
```

*   `app.py`: The main application file containing the Gradio interface setup and the core logic for loading the model, preprocessing images, and making predictions.
*   `models/`: This directory stores the pre-trained deep learning model.
    *   `spinach_disease_classifier.h5`: The Keras model file containing the CNN trained to classify spinach leaf diseases.
*   `requirements.txt`: Lists all Python package dependencies required to run the application.
*   `.gitignore`: Specifies files and directories that Git should ignore.
*   `.gitattributes`: Defines attributes for pathnames in the repository.

## Dependencies

The project relies on the following Python libraries:

*   **TensorFlow:** The primary framework for building and running the deep learning model.
*   **Gradio:** Used to create the interactive web interface for the application.
*   **Pillow (PIL):** For image manipulation and preprocessing.
*   **NumPy:** For numerical operations, especially array manipulation of image data.

All required packages are listed in `requirements.txt`.

## Installation

To get this project up and running on your local machine, follow these steps:

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/akshat281204/hydroponics-cnn-api.git
    cd hydroponics-cnn-api
    ```

2.  **Create and activate a virtual environment (recommended):**

    ```bash
    python -m venv venv
    ```

    *   **On Windows:**
        ```bash
        .\venv\Scripts\activate
        ```
    *   **On macOS/Linux:**
        ```bash
        source venv/bin/activate
        ```

3.  **Install the required Python packages:**

    ```bash
    pip install -r requirements.txt
    ```

## Usage

Once the installation is complete, you can launch the application:

1.  **Ensure your virtual environment is activated.**
2.  **Run the `app.py` script:**

    ```bash
    python app.py
    ```

3.  **Access the web interface:**
    The application will start a Gradio server. Open your web browser and navigate to the local URL provided in the console output (usually `http://127.0.0.1:7860`).

4.  **Upload an image:**
    On the Gradio interface, click on the "Upload Spinach Leaf Image" area to select an image file of a spinach leaf from your computer.

5.  **View predictions:**
    The model will process the image, and the "Prediction" output will display the predicted class (e.g., 'Healthy', 'Leaf Spot', 'Mite Damage') along with confidence scores for all three classes.

## API Documentation (Gradio Interface)

This project provides a user-friendly web interface via Gradio, serving as its primary API.

*   **Endpoint:** The application runs locally, typically accessible at `http://127.0.0.1:7860`.
*   **Title:** Spinach Disease Classifier
*   **Description:** Upload an image of a spinach leaf to classify its health status.

### Input

*   **Field:** "Upload Spinach Leaf Image"
*   **Type:** `gr.Image(type="pil")` - Accepts image files (e.g., JPEG, PNG). The image is converted to a PIL Image object internally, resized to 224x224 pixels, and normalized before prediction.

### Output

*   **Field:** "Prediction"
*   **Type:** `gr.Label(num_top_classes=3)` - Displays the classification result as a dictionary mapping class names to their confidence scores.
    *   **Class Names:**
        *   `Leaf Spot`
        *   `Healthy`
        *   `Mite Damage`
    *   **Example Output:**
        ```json
        {
          "Healthy": 0.985,
          "Leaf Spot": 0.010,
          "Mite Damage": 0.005
        }
        ```
        The output highlights the most probable class, and lists confidence scores for all defined classes.

## Model Details

*   **Model Name:** `spinach_disease_classifier.h5`
*   **Type:** Convolutional Neural Network (CNN)
*   **Framework:** TensorFlow/Keras
*   **Input Image Dimensions:** 224x224 pixels, 3 color channels (RGB)
*   **Output Classes:**
    *   `Leaf Spot`
    *   `Healthy`
    *   `Mite Damage`
*   **Preprocessing:** Images are resized to 224x224, converted to RGB, normalized to a 0-1 range, and expanded to batch dimensions before being fed to the model.

## Contributing

Contributions are welcome! If you have suggestions for improvements, new features, or bug fixes, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
