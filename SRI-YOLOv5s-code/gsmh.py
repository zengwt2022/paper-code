import cv2


def gaussian_blur(input_image_path, output_image_path, ksize=(5, 5)):
    # 读取图像
    image = cv2.imread(input_image_path)

    # 对图像进行高斯模糊
    blurred_image = cv2.GaussianBlur(image, ksize, 0)

    # 保存模糊后的图像
    cv2.imwrite(output_image_path, blurred_image)


# 使用
input_path = "D:\\code\\SRGAN-main\\frame0_1.jpg"
output_path = "D:\\code\\SRGAN-main\\frame0_1_1.jpg"
gaussian_blur(input_path, output_path)
