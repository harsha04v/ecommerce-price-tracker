import kagglehub

# Download latest version
path = kagglehub.dataset_download("PromptCloudHQ/flipkart-products")

print("Path to dataset files:", path)