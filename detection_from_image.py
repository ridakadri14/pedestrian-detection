# Running:
# $ python run-custom-cascade.py

# Import OpenCV
import cv2

# Image file
IMAGE_FILE = './crop_000001.png' # Change this to be your image

# Cascade file
CASCADE_FILE = './haarcascade_fullbody.xml'

# Cascade item name
CASCADE_ITEM = 'Front Face'

# Load image file
image = cv2.imread(IMAGE_FILE)

# Convert the image to gray
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Load your cascade file
cascade = cv2.CascadeClassifier(CASCADE_FILE)

# Detect cascade items and put rectangles around them
rectangles = cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=10,
			minSize=(75, 75))

print ("in")

for (i, (x, y, w, h)) in enumerate(rectangles):
	# Surround cascade with rectangle
    print(i)
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
    cv2.putText(image, CASCADE_ITEM + " #{}".format(i + 1), (x, y - 10),cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0, 0, 255), 2)

# Display the cascade to the user
cv2.imshow(CASCADE_ITEM + "s", image)

cv2.waitKey(0)