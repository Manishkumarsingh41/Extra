img = imread('Flower.jpeg'); % Load image from file
imshow(img); % Display the image
size(img)      % Returns dimensions: height, width, channels
class(img)     % Returns data type (e.g., 'uint8')
imfinfo('Flower.jpeg')

pixel = uint8([120, 200, 80]);
disp(pixel);  % Output: 120   200    80
class(pixel)  % Output: 'uint8'

Red = img(:,:,1);
Green = img(:,:,2);

figure;imshow(Red); title('Red components');
figure;imshow(Green);title('Green components');  % Shows green intensity

inverted_img = 255 - img;       % Invert each R, G, B channel
figure;imshow(inverted_img);title('Inverted Image');  % Show inverted image

rotated_img = imrotate(img, 180);
figure;imshow(rotated_img);title('Rotated Image');  % Show rotated image

crop_img = imcrop(img, [1000 1000 500 800]);
figure;imshow(crop_img);title('Cropped Image');  % Show cropped image

