import os, sys, time, datetime, random
import torch
from torch.autograd import Variable
from torchvision.models import detection
from PIL import Image
import numpy as np
import pdb
import cv2

def detect(input_image_path, labels_path=None): 
	with open('coco.txt') as f:
		classes = [line.rstrip() for line in f]
	colors = np.random.uniform(0, 255, size=(len(classes), 3))
	model = detection.fasterrcnn_resnet50_fpn(pretrained=True)
	model.eval()
	image = cv2.imread(input_image_path)
	orig = image.copy()
	image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
	image = image.transpose((2, 0, 1))
	image = np.expand_dims(image, axis=0)
	image = image / 255.0
	image = torch.FloatTensor(image)
	detections = model(image)[0]
	for i in range(0, len(detections["boxes"])):
		confidence = detections["scores"][i]
		idx = int(detections["labels"][i])-1
		box = detections["boxes"][i].detach().cpu().numpy()
		(startX, startY, endX, endY) = box.astype("int")
		label = "{}: {:.2f}%".format(classes[idx], confidence * 100)
		cv2.rectangle(orig, (startX, startY), (endX, endY),
			colors[idx], 2)
		y = startY - 15 if startY - 15 > 15 else startY + 15
		cv2.putText(orig, label, (startX, y),
			cv2.FONT_HERSHEY_SIMPLEX, 0.5, colors[idx], 2)
	return orig
	#cv2.imwrite(output_image_path, orig)

#detect("/home/vikram/bisque_module_testing/Modules/EdgeDetection/src/Intersection-Counts.jpg", "b.jpg")

