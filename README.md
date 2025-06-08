# Azure Function: Queens Solver

This Azure Function processes an uploaded image containing a color-constrained N-Queens puzzle and returns the solution as a PNG image. It also uploads the original, processed, and solution images to Azure Blob Storage.

---

## Overview

- Accepts an HTTP POST request with a puzzle image.
- Processes the image to extract game constraints.
- Solves the color-constrained N-Queens puzzle.
- Saves the images (original, processed, and solution) to Azure Blob Storage.
- Returns a PNG of the solution.

---

## Features

- HTTP-Triggered Azure Function
- Image processing and color extraction
- N-Queens puzzle solver with additional constraints
- Integration with Azure Blob Storage
- Provides solution image as PNG

---

## Technologies Used

- Azure Functions
- Python
- Azure Blob Storage

---

## Deployment

1. Install Azure Functions Core Tools.
2. Set the Azure Blob Storage connection string in your application settings.
3. Deploy using Azure CLI or Visual Studio Code.
4. For deployment best practices, consult the [Azure Functions documentation](https://docs.microsoft.com/azure/azure-functions/).

---

## Getting Started

1. Clone the repository.
2. Install required dependencies:
    pip install -r requirements.txt
3. Run the function locally with:
    func start
4. Test by sending a POST request with the image file to the function endpoint.

---

## Usage

Send a POST request to your Azure Function endpoint with the image file. The function will:
- Process the image.
- Solve the color-constrained N-Queens puzzle.
- Upload relevant images to Azure Blob Storage.
- Return the solution image in PNG format.

---


