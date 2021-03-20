from imageai.Detection import ObjectDetection
detector = ObjectDetection()
model_path = "./object_detection/models/yolo.h5"
input_path = "./object_detection/input/test5.jpg"
output_path = "./object_detection/output/newimage.jpg"
#detector.setModelTypeAsTinyYOLOv3()
detector.setModelTypeAsYOLOv3()
#detector.setModelTypeAsRetinaNet()
detector.setModelPath(model_path)
detector.loadModel()
detection = detector.detectCustomObjectsFromImage(input_image = input_path, output_image_path = output_path)
for i in detection:
    print (i["name"], " : ", i["percentage_probability"])


'''
either doesn't detect clothes or detects it as person??  (tried all pre trained models in the imageai library
 
so will have to make our own model?
'''