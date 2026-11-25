"""
Experiment 06: Object Detection using Pre-Trained Deep Learning Architecture
Name   : S. Maruthu Pandi
Reg No : 192511162
Course : CSA1717 - Artificial Intelligence
College: Saveetha School of Engineering
"""

import torch
import torchvision
from torchvision.models.detection import fasterrcnn_resnet50_fpn, FasterRCNN_ResNet50_FPN_Weights

# Load pre-trained Faster R-CNN model
weights = FasterRCNN_ResNet50_FPN_Weights.DEFAULT
model = fasterrcnn_resnet50_fpn(weights=weights)
model.eval()
categories = weights.meta["categories"]

# Create dummy RGB tensor representing an image (3x224x224)
dummy_image = [torch.rand(3, 224, 224)]
with torch.no_grad():
    predictions = model(dummy_image)

print("=== Pre-Trained Faster R-CNN Object Detection ===")
print(f"Model Loaded: FasterRCNN_ResNet50_FPN (COCO {len(categories)} classes)")
print("Sample COCO Classes:", categories[1:6])
print("Inference Tensor Shape:", dummy_image[0].shape)
print("Detection Pipeline Status: Ready for Bounding Box Inference")
