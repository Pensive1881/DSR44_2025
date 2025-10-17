# Review Questions - Practical Computer Vision with PyTorch and FiftyOne
* [View Playlist on YouTube](https://youtube.com/playlist?list=PLf-F6yXx9sp9YgRLzuegQWxA71XD13tVH&si=S_1oT8AHTVFIpuv5)

* [Practical Notebooks](https://github.com/andandandand/practical-computer-vision/tree/main/notebooks)

## Video 1 - Common Tasks in Computer Vision
* [Watch Video 1 on YouTube](https://youtu.be/VcF9i0Kcu30?si=FlC4NaSaMfM90lKb)

### **What is the primary goal of computer vision according to the presentation?**

a) To create digital images from textual descriptions.

b) To enable machines to physically interact with the world.

c) To give machines the ability to understand the content of digital images.

d) To optimize algorithms for image compression.


### **What is a key difference between discriminative and generative computer vision tasks, according to the video?**

a) Discriminative tasks create new images, while generative tasks analyze existing images.

b) Discriminative tasks assign labels or scores to images, while generative tasks create images from prompts.

c) Discriminative tasks require less training data compared to generative tasks.

d) Discriminative tasks are primarily used in scientific applications, while generative tasks are for industrial use.


### **Which of the following is a fundamental discriminative task in computer vision?**

a) Image generation from noise.

b) Creating synthetic training data.

c) Assigning global labels to entire images.

d) Learning probability distributions of images.


### **Which computer vision task provides the most detailed information about the location and shape of objects within an image?**

a) Image classification.

b) Object detection.

c) Instance segmentation.

d) Image captioning.


## Video 2 - Digital Image Representation with PIL and NumPy
* [Watch Video 2 on YouTube](https://youtu.be/zMKboz5jwEY?si=mqo57ztFXlnJbwqB)

### **What is the typical range of intensity values for each channel (grayscale or color) in a digital image commonly encountered from files like JPEG or PNG, and what data type is typically used to store these values?**

a) 0 to 1, float32

b) 0 to 1024, uint16

c) 0 to 255, uint8

d) -128 to 127, int8


### **According to the video, how does a computer fundamentally represent a grayscale digital image?**

a) As a collection of semantic shapes and objects.

b) As a vector graphic with defined lines and curves.

c) As a matrix (or a 2D array) of pixel intensity values.

d) As a compressed binary file that needs to be decoded to see the image.


### **What is the standard order of dimensions (height, width, channels) for representing a color image as a NumPy ndarray?**

a) Channels, Height, Width

b) Width, Height, Channels

c) Height, Width, Channels

d) Width, Height (no channel dimension)


### **What is the purpose of the Python Image Library (PIL/Pillow) as described in the course content?**

a) Primarily for performing complex numerical computations on image data like matrix multiplication.

b) Mainly for visualizing images using various plots and graphs directly within the library.

c) For opening, manipulating (resizing, converting), inspecting properties (mode, size), and saving image files in various formats (like JPEG or PNG).

d) For defining the underlying mathematical representation of image tensors used in deep learning.


### **Which Python library is primarily used for performing element-wise arithmetic operations and array manipulations on digital image data represented as multi-dimensional arrays?**

a) PIL (Python Image Library) / Pillow

b) Matplotlib

c) NumPy

d) scikit-image


### **What happens when we perform the operation <code>np_array = 255 - np_array</code> on a grayscale NumPy uint8 array representing an image?**

a) The array values are clipped, ensuring no value exceeds 255.

b) The array values are shifted downwards by 255, potentially becoming negative if not for uint8 properties.

c) The intensity values are inverted, creating the negative of the image (black becomes white, white becomes black).

d) The array is normalized to have values approximately between 0 and 1.


### **When indexing a NumPy array representing an RGB image (<code>rgb_image</code>) following the standard Height, Width, Channels convention, how would you access the intensity values for all three color channels of a single pixel at row index <code>r</code> and column index <code>c</code>?**

a) rgb_image[c, r, :]

b) rgb_image[r, c]

c) rgb_image[r, c, :]

d) rgb_image[:, :, [r, c]]


### **What is the significance of the "uint8" data type in the context of digital images?**

a) It represents high-precision floating-point numbers used primarily for intermediate calculations in image analysis.

b) It signifies an unsigned 8-bit integer, capable of storing whole numbers from 0 to 255, commonly used for representing pixel intensity values in standard image formats due to its memory efficiency.

c) It indicates that the image uses a 16-bit format (like uint16), allowing for a much wider range of intensity values (0 to 65535).

d) It directly specifies the color space (like RGB or Grayscale) used for representing the image's color information.


## Video 3 - PyTorch Image Tensors
* [Watch Video 3 on YouTube](https://youtu.be/DQlngcHaKd4?si=8j0gE6PuBchG8SkI)

### **What are the primary advantages of using PyTorch tensors over NumPy ndarrays for deep learning?**

a) NumPy ndarrays have better support for automatic gradient computation.

b) PyTorch tensors can leverage GPUs and TPUs for accelerated computation and offer automatic gradient computation.

c) NumPy ndarrays are inherently more memory efficient for large datasets.

d) PyTorch tensors are only compatible with CPU-based computation.


### **Why is it often necessary to move PyTorch tensors back to the CPU?**

a) GPU memory is always insufficient for any kind of complex operation.

b) Certain operations like visualization using libraries like Matplotlib are performed on the CPU.

c) All pre-processing steps must be done on the CPU before moving data to the GPU.

d) Moving tensors to the CPU always results in faster computation.


### **What is the primary purpose of setting <code>requires_grad=True</code> when creating a PyTorch tensor?**

a) To optimize memory usage for that tensor.

b) To indicate that PyTorch should track operations on this tensor to compute gradients for automatic differentiation.

c) To ensure that the tensor is always processed on the GPU.

d) To prevent the values of the tensor from being modified during training.


### **In PyTorch, what is the standard order of dimensions for a batch of image tensors, commonly expected by convolutional layers?**

a) Height, Width, Channels, Batch Size (H, W, C, N)

b) Channels, Height, Width, Batch Size (C, H, W, N)

c) Batch Size, Channels, Height, Width (N, C, H, W)

d) Width, Height, Channels, Batch Size (W, H, C, N)


### **What is the role of the <code>.backward()</code> method when called on a scalar tensor (like the loss) in PyTorch?**

a) To move the tensor calculation from the GPU back to the CPU.

b) To compute the gradients of that scalar tensor with respect to all leaf tensors in the computation graph that have requires_grad=True.

c) To save the current state of the computation graph to disk for later use.

d) To convert the PyTorch tensor into an equivalent NumPy array for compatibility with other libraries.


## Video 4 - Introduction to Neural Networks 
* [Watch Video 4 on YouTube](https://www.youtube.com/watch?v=QrblN6UM_cI)

### **What is the purpose of training a neural network?**

a) To increase the number of hidden layers.

b) To collect a large amount of data.

c) To adjust the network's weights to minimize error.

d) To select the best activation function.


### **Which of the following describes a loss function in the context of neural networks?**

a) A function that activates a neuron based on its input.

b) A measure of the error between the network's prediction and the true value.

c) A function that determines the learning rate of the network.

d) A layer in the neural network that is not the input or output layer.


### **What is the role of backpropagation in training neural networks?**

a) To perform the forward pass and generate predictions.

b) To calculate the gradient of the loss with respect to each weight.

c) To define the architecture of the neural network.

d) To divide the data into training, validation, and testing sets.


### **What is the primary purpose of using a validation set during the training process of a neural network?**

a) To directly train the model and allow the optimizer to adjust its weights based on this data.

b) To perform the final, definitive, and unbiased evaluation of the fully trained model's performance on completely unseen data.

c) To monitor the model's generalization performance on data it hasn't been trained on, helping to tune hyperparameters (like learning rate, model architecture) and decide when to stop training (early stopping) to prevent overfitting.

d) To introduce additional diverse examples (like augmented data) into the training process to improve robustness.


### **What is Stochastic Gradient Descent (SGD)?**

a) A technique for defining the architecture of a neural network by randomly connecting layers.

b) A specific type of non-linear activation function used primarily in recurrent neural networks.

c) An iterative optimization algorithm used to update the weights and biases of a neural network by taking steps in the opposite direction of the estimated gradient of the loss function, calculated on a small batch of data.

d) A loss function specifically designed to measure the difference between predicted and true probability distributions in classification tasks.


### **What is the Adam optimizer in the context of training neural networks?**

a) A specific type of loss function used for multi-class classification tasks.

b) An adaptive learning rate optimization algorithm, often considered an improvement over basic Stochastic Gradient Descent (SGD), that uses estimates of first and second moments of gradients.

c) A non-linear activation function known for preventing the vanishing gradient problem.

d) A standard technique for evaluating the performance and generalization ability of a trained neural network.


### **What is the relationship between the batch size used in training and the estimation of the gradient in Stochastic Gradient Descent (SGD) and its variants?**

a) A larger batch size results in a gradient estimate that is more noisy and less representative of the true gradient over the entire dataset.

b) The batch size directly determines the learning rate used for the parameter updates in SGD.

c) The batch size specifies the number of training samples used to compute the loss and its gradient in a single iteration; this gradient estimate guides the parameter update for that step.

d) Using a smaller batch size always leads to more stable and faster convergence compared to using a larger batch size.


## Video 5 - Multilayer Perceptron for Image-based Regression
* [Watch Video 5 on YouTube](https://www.youtube.com/watch?v=cr4NMVKJzaw)

### **What are the three key components of a basic multilayer perceptron architecture illustrated in the initial example? (Assume that all layers are fully connected)**

a) Input layer, convolutional layer, output layer

b) Input layer, pooling layer, output layer

c) Input layer, hidden layer, output layer

d) Input layer, recurrent layer, output layer


### **Why is it important to include a nonlinearity, such as ReLU, between layers in a neural network?**

a) To reduce the number of parameters

b) To speed up the forward pass

c) To avoid wasting computation by introducing complex mappings between inputs and outputs

d) To ensure the network can only learn linear relationships


### **In the context of neural network training, what does the learning rate control?**

a) The complexity of the model architecture

b) The size of the adjustments made to the weights during updates

c) The type of loss function used

d) The number of hidden layers in the network


### **Why is choosing an appropriate learning rate a critical hyperparameter during neural network training?**

a) It directly determines the total number of epochs the training will run for.

b) It dictates which specific activation functions (ReLU, sigmoid, etc.) must be used in each layer.

c) It controls the step size taken during parameter updates; too large a rate can cause instability or divergence, while too small a rate can lead to very slow convergence or getting stuck in poor local minima.

d) It automatically adjusts the size of the input data batches based on available memory.


### **What happens to the dimensions of an image tensor with shape <code>(3, 1282, 1920)</code> (Channels, Height, Width) after being flattened for input into a fully connected network?**

a) It remains a 3D tensor but with permuted dimensions, like (1920, 1282, 3).

b) It becomes a 2D tensor (matrix) with shape (3, 1282 * 1920).

c) It becomes a 1D vector with a total size equal to the product of its dimensions (3 * 1282 * 1920 elements).

d) Its dimensions are averaged to produce a single scalar value.


### **Which of the following PyTorch modules is specifically designed to implement a standard fully connected (affine) transformation layer in a neural network?**

a) torch.matmul()

b) torch.relu()

c) torch.nn.Linear(in_features, out_features)

d) torch.sigmoid()


### **By stacking multiple layers consisting of linear transformations followed by non-linear activation functions, what kind of decision boundaries can a neural network learn to approximate?**

a) Only simple, straight, linear boundaries separating classes.

b) Only boundaries that are convex in shape.

c) Highly complex, non-linear, potentially non-convex, and intricate decision boundaries required for sophisticated tasks.

d) Boundaries that are strictly limited to being hyperplanes in the feature space.


## Video 6 - Matrix Multiplication and Activation Functions
* [Watch Video 6 on YouTube](https://youtu.be/w83lLCZiMng?si=TIMQhudVRh-OrrAk)

### **What is an important aspect to consider regarding the dimensions of matrices during multiplication in neural networks?**

a) The sum of the dimensions must be equal.

b) The number of columns in the first matrix must match the number of rows in the second matrix.

c) The matrices must have the same shape.

d) The determinant of both matrices must be non-zero.


### **Which of the following is a common and effective debugging tip for identifying tensor dimension errors in PyTorch?**

a) Using a very small learning rate.

b) Randomly permuting the input data.

c) Printing the shape of tensors before operations using tensor.shape or torch.size().

d) Increasing the batch size.


### **What is the output of the ReLU activation function for a negative input value?**

a) The negative input value itself.

b) Zero.

c) The absolute value of the input.

d) One.


### **In a standard fully connected (linear) layer of a neural network, the dimensions of the weight matrix directly determine:**

a) Which activation function (e.g., ReLU, Sigmoid) will be used after the layer.

b) The specific learning rate that will be applied to update the weights of that layer.

c) The transformation mapping between the number of input features coming into the layer and the number of output features produced by the layer.

d) The type of loss function (e.g., Cross Entropy, MSE) that will be used to evaluate the network's output.


### **In PyTorch's <code>nn.Linear(in_features, out_features, bias=True)</code> layer, what functional advantage does including the bias term (when <code>bias=True</code>) provide?**

a) It significantly speeds up the matrix multiplication computation.

b) It allows the layer to perform dimensionality reduction more effectively.

c) It adds an offset to the output, allowing the linear transformation (hyperplane) to shift, providing more flexibility beyond just rotation/scaling through the origin.

d) It automatically normalizes the input features before the matrix multiplication.


### **What is the most likely consequence if the number of input features in a data batch provided to a PyTorch <code>nn.Linear</code> layer does not match the <code>in_features</code> argument specified when the layer was defined?**

a) The program will continue to run, but the output predictions will be numerically incorrect or meaningless.

b) PyTorch will automatically try to reshape the input tensor to match the layer's expected in_features.

c) A runtime error (typically a RuntimeError related to shape mismatch) will occur during the forward pass when the matrix multiplication is attempted.

d) The weight matrix of the linear layer will be re-initialized randomly to accommodate the new input size.


### **What is the primary purpose of applying non-linear activation functions (like ReLU, Sigmoid, Tanh) after the linear transformations (matrix multiplications) in neural network layers?**

a) To reduce the dimensionality of the feature space at each layer.

b) To ensure that the network's overall computation remains strictly linear, simplifying analysis.

c) To introduce non-linearities into the model, enabling it to learn complex patterns and decision boundaries that cannot be captured by purely linear transformations.

d) To significantly speed up the computation of the forward pass compared to just using linear layers.


## Video 7 - Building a Feedforward Network for Classification in PyTorch
* [Watch Video 7 on YouTube](https://youtu.be/x4umXrs9MuA?si=xtBMpZ6ibJ-vKlBb)

### **What is the purpose of the cross entropy loss function when used for image classification?**

a) To measure the accuracy of the network's predictions directly

b) To measure how well the predicted probabilities match the true labels

c) To optimize the learning rate of the Adam optimizer

d) To add non-linearity to the neural network


### **When the true label for an image is "cat" (encoded as [1.0, 0.0, 0.0]) and the network predicts probabilities [0.99, 0.01, 0.0], the cross entropy loss will be:**

a) Very high

b) Very low

c) Undefined

d) Equal to 1


### **What is name of the output of the final linear layer of a network (without going into a softmax or sigmoid activation function)?**

a) Probabilities

b) Logits

c) Features

d) Activations


### **Why is cross-entropy loss generally preferred over accuracy as the objective function for training classification models using gradient descent?**

a) Cross-entropy loss values are always bounded between 0 and 1, making them easier to interpret.

b) Accuracy provides a smoother and more granular signal for gradient updates compared to cross-entropy.

c) Cross-entropy loss is a differentiable function with respect to model outputs (probabilities or logits), allowing for the computation of gradients needed for backpropagation and weight updates, whereas accuracy is not differentiable.

d) Accuracy directly optimizes the model for the most common and desired business evaluation metric.


### **What is the common term for the raw, unnormalized output scores produced by the final linear layer of a neural network, before any activation function (like Softmax or Sigmoid) is applied?**

a) Probabilities

b) Logarithms

c) Logits

d) Gradients


## Video 8 - Metrics for Classification and Experiment Tracking
* [Watch Video 8 on YouTube](https://youtu.be/e1RrEafgUjQ?si=1yipMUYkjjKLXS3c)

### **Which of the following describes a false negative in a classification problem?**

a) The model predicts a positive class, and the ground truth is also a positive class.

b) The model predicts a negative class, and the ground truth is also a negative class.

c) The model predicts a negative class, but the ground truth is a positive class.

d) The model predicts a positive class, but the ground truth is a negative class.


### **What is the default threshold commonly used in machine learning libraries to binarize the output probability of a classifier into positive or negative predictions?**

a) 0.1

b) 0.5

c) 0.9

d) 0.99


### **How does increasing the threshold for a positive prediction typically affect precision and recall?**

a) Both precision and recall increase.

b) Precision increases, and recall decreases.

c) Precision decreases, and recall increases.

d) Both precision and recall decrease.


### **What is the role of the test set in the machine learning workflow, particularly in evaluating a trained neural network?**

a) To fine-tune the weights of the network one last time after validation is complete.

b) To guide the decision of when to stop the training process based on performance saturation.

c) To provide a final, unbiased estimate of the model's generalization performance on completely new, unseen data after all training and hyperparameter tuning is finished.

d) To optimize critical hyperparameters like the learning rate, batch size, or network architecture during development.


### **Which of the following is a primary reason why accuracy might be a misleading evaluation metric for a classifier, especially when dealing with imbalanced datasets?**

a) Calculating accuracy requires complex mathematical operations involving derivatives.

b) Accuracy inherently incorporates the model's confidence probabilities for each prediction.

c) A naive classifier that always predicts the majority class can achieve a high accuracy score, even if it completely fails to identify minority class instances.

d) Accuracy is a smooth, differentiable function, making it unsuitable for certain optimization techniques.


### **What does the F1 score represent in classification evaluation?**

a) The proportion of actual positive instances that were correctly identified (Recall or True Positive Rate).

b) The proportion of predicted positive instances that were actually correct (Precision).

c) The harmonic mean of Precision and Recall, providing a single metric that balances both aspects.

d) The overall percentage of correct predictions across all classes (Accuracy).


### **What is the primary purpose of checkpointing models during the training process?**

a) To create visualizations of the model's internal layer activations.

b) To save the state (weights, optimizer state, epoch number, etc.) of the model periodically, especially when it achieves the best performance so far on a validation metric, allowing training to be resumed or the best model to be retrieved later.

c) To generate intermediate predictions on the training data to monitor progress.

d) To significantly speed up the overall training process by skipping redundant computations.


### **What information does a confusion matrix visually represent for a classification model?**

a) The evolution of the training and validation loss values over epochs.

b) The probability scores predicted by the model for each class for a set of samples.

c) A table summarizing the performance by showing the counts of true positive, true negative, false positive, and false negative predictions across different actual and predicted classes.

d) The detailed architecture of the neural network, including layers and connections.


### **For which type of classification datasets are evaluation metrics like precision, recall, and F1 score generally considered more informative or crucial than overall accuracy?**

a) Datasets with a very large number of input features (high dimensionality).

b) Datasets where all classes are represented roughly equally (balanced datasets).

c) Datasets exhibiting class imbalance, where some classes have significantly fewer samples than others.

d) Datasets used for regression tasks rather than classification.


## Video 9 - PyTorch Datasets and DataLoaders
* [Watch Video 9 on YouTube](https://youtu.be/d2TdTiTLBb0?si=ZVm3QZ96JinlRKuJ)

### **When doing computer vision tasks, what is the primary purpose of a PyTorch Dataset object?**

a) To load data in batches for model training.

b) To define the transformations applied to the data.

c) To store and provide access to individual samples of data (images and labels).

d) To move data to the GPU for faster processing.


### **Why is it important to shuffle the training data when using a DataLoader?**

a) To speed up data loading.

b) To reduce memory consumption.

c) To prevent the model from learning sequence-specific patterns and to ensure stochasticity in gradient descent.

d) To ensure that the validation and test sets are processed in the correct order.


### **Which of the following methods is essential for a custom PyTorch Dataset class?**

a) forward()

b) backward()

c) __init__(), __len__(), and __getitem__()

d) __iter__() and __next__()


### **In typical PyTorch data loading and processing for neural networks, what does the first dimension (dimension 0) of an input tensor usually represent?**

a) The number of output features the next layer should produce.

b) The size (number of elements) of each individual sample or feature vector in the input.

c) The batch size, indicating the number of independent data samples being processed together in parallel.

d) The total number of layers present in the neural network architecture.


## Video 10 - Fundamentals of Convolutions in Computer Vision
* [Watch Video 10 on YouTube](https://youtu.be/M-YWxCUvmnI?si=dlKGY8L95qwnNT1W)

### **What is the primary purpose of a convolution kernel in image processing?**

a) To increase the image resolution

b) To compress the image data

c) To extract features from the image

d) To change the color balance of the image


### **What determines the extent of neighboring pixels that influence a single output pixel in a convolution operation?**

a) The stride of the convolution

b) The padding applied to the image

c) The size of the convolution kernel

d) The activation function used after the convolution


### **In modern neural networks for computer vision, how are the weights of convolution kernels typically determined?**

a) They are set to fixed values based on mathematical formulas (e.g., Sobel filters).

b) They are initialized to zero and remain constant.

c) They are learned from the data through a training process (backpropagation).

d) They are manually selected by experienced engineers.


### **What is a key motivation for resizing input images (e.g., from 1920x1282 down to 224x224) before feeding them into a neural network, especially one with fully connected layers?**

a) To increase the number of color channels available for processing.

b) To significantly improve the visual quality and resolution of the input image.

c) To drastically reduce the number of input features (pixels * channels), making the model computationally feasible by reducing the number of parameters (especially in the first fully connected layer) and memory requirements.

d) To fundamentally change the aspect ratio of the image to match the network's requirements.


### **What is the conventional format for representing a batch of image tensors in PyTorch, typically expected by layers like <code>nn.Conv2d</code>?**

a) [Channels, Height, Width, Batch Size] (C, H, W, N)

b) [Height, Width, Channels, Batch Size] (H, W, C, N)

c) [Height, Width, Batch Size, Channels] (H, W, N, C)

d) [Batch Size, Channels, Height, Width] (N, C, H, W)


### **What does the 'stride' parameter control in a convolutional layer operation?**

a) The dimensions (height and width) of the convolution kernel (filter).

b) The numerical values (weights) contained within the convolution kernel.

c) The step size, in pixels, that the convolution kernel moves across the input feature map both horizontally and vertically between computations.

d) The type and amount of padding (e.g., 'same', 'valid', or specific pixel count) applied to the borders of the input feature map.


### **What is a primary reason for adding padding (e.g., zero-padding) around the borders of an input feature map before applying a convolution operation?**

a) To significantly reduce the computational cost and memory usage of the convolution.

b) To increase the number of learnable parameters (features) extracted by the convolution filters.

c) To control the spatial dimensions of the output feature map, often used to preserve the original height and width when using a stride of 1, and to allow the kernel to process border pixels more effectively.

d) To directly introduce non-linearity into the convolution operation itself, before the activation function.


## Video 11 - Pooling in Neural Networks
* [Watch Video 11 on YouTube](https://youtu.be/M-YWxCUvmnI?si=dlKGY8L95qwnNT1W)

### **What is the primary operation performed by Max Pooling?**

a) Calculating the average value in a window.

b) Selecting the highest value in a window.

c) Computing the sum of all values in a window.

d) Applying a non-linear activation function.


### **What is the effect of a Max Pool 2D layer with a stride of 2 on the spatial dimensions (height and width) of a feature map?**

a) It doubles the spatial dimensions.

b) It keeps the spatial dimensions the same.

c) It reduces the spatial dimensions by half (approximately, depending on kernel size and padding).

d) It triples the spatial dimensions.


### **What is the main purpose of Global Pooling operations like Global Max Pooling or Global Average Pooling?**

a) To increase the spatial dimensions of feature maps.

b) To apply a sliding window to extract local features.

c) To convert feature maps of varying spatial sizes into fixed-length vectors.

d) To introduce non-linearity into the network.


### **How does Mean Pooling (Average Pooling) typically differ from Max Pooling in its effect on the resulting feature map?**

a) Mean Pooling tends to preserve sharp edges and the most salient features better, while Max Pooling creates smoother, blurrier outputs.

b) Max Pooling is better at retaining background information and texture details, while Mean Pooling focuses only on the strongest activation.

c) Mean Pooling computes the average value within the pooling window, generally resulting in a smoother, downsampled feature map that retains more information about the overall region, while Max Pooling selects the maximum value, preserving the strongest activation (feature presence).

d) Max Pooling considers all values within the window by taking their maximum, while Mean Pooling randomly samples one value from the window.


### **How does replacing a final flattening operation followed by fully connected layers with a Global Pooling layer (like Global Average Pooling or Global Max Pooling) potentially benefit a Convolutional Neural Network?**

a) It significantly increases the total number of trainable parameters in the network, allowing for more complex decision boundaries.

b) It guarantees an improvement in the model's classification accuracy on all types of datasets.

c) It drastically reduces the number of parameters (especially compared to flattening high-resolution feature maps), enforces better correspondence between feature maps and categories, and can act as a structural regularizer helping to prevent overfitting. It also allows the network to handle variable input sizes more easily.

d) It substantially increases the computational cost and memory requirements during both training and inference.


## Video 12 - Upsampling and Channel Mixing with Convolutions
* [Watch Video 12 on YouTube](https://youtu.be/AV2wgR_YPpM)

### **Which operation is known for potentially introducing checkerboard artifacts during image upsampling?**

a) Bilinear interpolation

b) 1x1 convolution

c) Transpose convolution (Deconvolution / Up-convolution)

d) Max pooling


### **What is the primary purpose of a 1x1 convolution?**

a) To increase the spatial resolution of an image.

b) To reduce the number of channels in a feature map.

c) To mix information across channels and potentially change the number of channels.

d) To introduce non-linearity into a network.


### **What is bilinear interpolation used for in the context of deep learning and image processing, according to the video?**

a) To compress feature maps into a lower-dimensional representation.

b) To resize feature maps (upsampling or downsampling) by estimating new pixel values based on a weighted average of the four nearest neighbors.

c) To perform channel-wise attention on feature maps.

d) To identify edges and corners in an image.


### **What are hypercolumns in the context of deep learning for computer vision, and how are 1x1 convolutions often used with them?**

a) Hypercolumns are sparsely connected, highly efficient neural network layers; 1x1 convolutions are used primarily to prune unnecessary connections within these layers.

b) Hypercolumns refer to a specific type of advanced activation function used in generative models; 1x1 convolutions help normalize their output range.

c) Hypercolumns are feature vectors created by stacking or concatenating the activation maps from multiple layers of a CNN at the same spatial (x, y) location; 1x1 convolutions are then often used to process and combine these multi-level features effectively.

d) Hypercolumns are simply very high-resolution input images used for fine-grained tasks; 1x1 convolutions are mainly used as an initial step to downsample these images.


### **What is a commonly cited benefit of using a sequence of bilinear upsampling followed by channel mixing with convolutions (e.g., 1x1 or 3x3 conv) for increasing spatial resolution in generative models or segmentation networks, compared to using transpose convolutions?**

a) This sequence is always significantly faster and requires less memory than a single transpose convolution layer.

b) It allows the network to learn much more complex and non-linear upsampling patterns from the data.

c) It tends to produce smoother results and helps reduce or eliminate the checkerboard artifacts that can sometimes appear when using transpose convolutions due to uneven overlap.

d) It inherently performs feature selection during the upsampling process, discarding irrelevant channels automatically.


## Video 13 - Normalizing Input Values and Inference with Pretrained Models
* [Watch Video 13 on YouTube](https://youtu.be/0Lz1uDpgVCw)

### **What is the mathematical operation involved in standard input scaling (normalization)?**

a) Multiplying the data by a scaling factor.

b) Subtracting the median and dividing by the interquartile range.

c) Subtracting the mean and dividing by the standard deviation.

d) Taking the logarithm of the data.


### **According to the video, what is a key reason for performing input normalization?**

a) To reduce the size of the input data.

b) To visualize the data in a more interpretable way.

c) To accelerate the training of deep learning models, potentially through smoother gradient updates and a more well-behaved loss landscape.

d) To introduce non-linearity into the model.


### **When using a pretrained model that was trained on the ImageNet dataset, why is it important to normalize the input data using the specific ImageNet mean and standard deviation statistics?**

a) To change the data into the specific image file format (e.g., PNG, JPEG) required by the model architecture.

b) To ensure that the input data has a mean of zero and a standard deviation of one for each feature, regardless of the original training data statistics.

c) To ensure the input data distribution matches the distribution the model saw during its original training, maintaining compatibility.

d) To increase the variance of the input data, making features more distinct.


### **What is the primary purpose of scaling pixel values of an image tensor from the integer range [0, 255] to the floating-point range [0.0, 1.0] before feeding them into a deep learning model?**

a) To significantly change the data type from integer to floating-point, which is inherently required by all PyTorch operations.

b) To reduce the memory footprint of the image tensor, as floats between 0 and 1 use less memory than integers between 0 and 255.

c) To improve numerical stability during training computations (like gradient calculations, activation functions) and potentially help optimization algorithms converge more effectively.

d) To automatically convert the image from RGB to grayscale format as part of the normalization.


### **What was a significant consequence or outcome related to the AlexNet network's success in the 2012 ImageNet Large Scale Visual Recognition Challenge (ILSVRC)?**

a) The ImageNet dataset itself was first created and released to the public in 2012 specifically for this challenge.

b) The problem of overfitting in deep neural networks was conclusively solved by the techniques used in AlexNet.

c) AlexNet achieved a dramatically lower error rate compared to previous state-of-the-art methods, demonstrating the power of deep convolutional neural networks with GPU acceleration for complex image classification tasks and sparking renewed interest in deep learning.

d) The practice of input data normalization (subtracting mean, dividing by standard deviation) was first introduced and established by the AlexNet paper.


### **When calculating statistics (mean and standard deviation) for input normalization to be applied during the training of a neural network, from which data split should these statistics be derived?**

a) Only from the validation set to ensure the model generalizes well.

b) Only from the test set to match the final evaluation conditions.

c) Only from the training set.

d) From a combination of all available data (training, validation, and test sets) to get the most accurate overall statistics.


## Video 14 - Binary Cross Entropy Loss
* [Watch Video 14 on YouTube](https://youtu.be/pM1lHyauY3Q)

### **Which loss function is best suited for a single-label image classification problem with multiple classes (e.g., classifying digits 0-9, where each image is only one digit)?**

a) Binary Cross Entropy Loss (BCE Loss)

b) Binary Cross Entropy with Logits Loss (BCEWithLogitsLoss)

c) Categorical Cross Entropy Loss (CrossEntropyLoss in PyTorch)

d) Mean Squared Error Loss (MSE Loss)


### **You are training a multi-label image classifier (each image may belong to any number of classes simultaneously, e.g., an image containing both a "cat" and a "dog"). Which activation–loss pairing is the correct choice?**

a) Softmax activation + Categorical Cross Entropy Loss

b) Sigmoid activation + Categorical Cross Entropy Loss

c) Softmax activation + Binary Cross Entropy Loss

d) Sigmoid activation + Binary Cross Entropy Loss (or BCEWithLogitsLoss)


### **What is the primary role of the natural logarithm function within the cross entropy loss formula?**

a) To normalize the probability distribution so that probabilities sum to 1.

b) To convert the raw output scores (logits) into probabilities.

c) To heavily penalize confident wrong predictions and lightly penalize confident correct predictions, driving the model towards certainty.

d) To ensure that the calculated loss values are always non-negative.


### **Why is using <code>nn.CrossEntropyLoss</code> directly with raw logits (the output of the final linear layer before softmax) generally recommended in PyTorch instead of applying <code>softmax</code> first and then using <code>nn.NLLLoss</code>?**

a) Because nn.CrossEntropyLoss is computationally much simpler and faster.

b) To provide loss values that are more easily interpretable as probabilities by humans.

c) For improved numerical stability, as nn.CrossEntropyLoss internally combines log_softmax and nn.NLLLoss in a way that avoids potential floating-point precision issues with calculating softmax and then log separately.

d) Because nn.CrossEntropyLoss inherently requires the target labels to be provided in a one-hot encoded format.


### **Which activation function is typically applied to the output layer (logits) of a neural network designed for a single-label multi-class classification task (e.g., classifying an image as one of 10 digits)?**

a) Sigmoid

b) ReLU (Rectified Linear Unit)

c) Softmax

d) Tanh (Hyperbolic Tangent)


### **In PyTorch, if you have already applied a <code>torch.sigmoid</code> activation function to the output of your neural network for a binary or multi-label classification problem, which loss function should you typically use?**

a) torch.nn.CrossEntropyLoss

b) torch.nn.BCEWithLogitsLoss

c) torch.nn.BCELoss

d) torch.nn.MSELoss


### **What is the common term for the raw, unnormalized output scores produced by the final linear layer of a neural network, before any activation function (like Softmax or Sigmoid) is applied?**

a) Probabilities

b) Logarithms

c) Logits

d) Gradients


### **For a multi-label image classification problem, where a single image can simultaneously belong to multiple classes (e.g., an image containing both a "cat" and a "dog"), which activation function should typically be used in the output layer?**

a) Softmax

b) ReLU

c) Sigmoid

d) Tanh


### **In the context of training classification models, what is the primary purpose of encoding the ground truth class labels into a probability distribution format (e.g., one-hot encoding for single-label, multi-hot encoding for multi-label)?**

a) To significantly accelerate the forward pass computation during training.

b) To provide a target probability distribution that the model's predicted probability distribution (output of softmax/sigmoid) can be directly compared against using a suitable loss function like cross-entropy.

c) To create easily interpretable visualizations of the class distribution within the training dataset.

d) To reduce the dimensionality of the input data fed into the neural network.


## Video 15 - Skip Connections
* [Watch Video 15 on YouTube](https://youtu.be/Hi2C-7gN4PU)

### **What is identified as a significant problem in deep neural network training that skip connections help to resolve?**

a) Overfitting of training data

b) Increased computational complexity

c) The vanishing gradient problem

d) Slower convergence rates


### **The vanishing gradient problem is fundamentally caused by what limitation in computers, according to the video's explanation?**

a) The speed of processing floating-point numbers.

b) The limited precision available to represent extremely small numbers, leading to numerical underflow when we do repeated multiplication by values &lt; 1 (e.g. derivatives of activation functions times weights).

c) The way certain activation functions (like sigmoid/tanh) squash values into a small range.

d) The discrete nature of digital computations versus continuous mathematical functions.


### **According to the video, what effect do skip connections have on the loss landscape during training?**

a) They make the loss landscape more rugged and harder to optimize.

b) They smooth the loss landscape, making optimization easier by providing shorter paths for gradients.

c) They have no significant impact on the shape of the loss landscape, only on gradient values.

d) They sharpen the loss landscape, leading to faster convergence but potentially into suboptimal minima.


### **In the standard ResNet (Residual Network) architecture, how are skip connections typically implemented within a residual block?**

a) By concatenating the input feature map x with the feature map F(x) produced by the convolutional layers along the channel dimension.

b) By performing element-wise addition between the input feature map x and the output F(x) of the block's convolutional layers (i.e., output = F(x) + x).

c) By applying a learned multiplicative gate (like in LSTMs) to the input x before adding it to F(x).

d) By replacing some of the convolutional layers within the block with simple identity mappings (pass-through layers).


### **What is the primary role of the long skip connections (connecting encoder blocks to corresponding decoder blocks) in the U-Net architecture, particularly for tasks like image segmentation?**

a) To solely mitigate the vanishing gradient problem during the training of the deep encoder part of the network.

b) To exclusively transfer high-level semantic information learned in the bottleneck layer to the final layers of the decoder.

c) To combine high-resolution spatial features from the encoder path with the semantically rich but spatially coarse up-sampled features from the decoder path, enabling precise localization in the output segmentation map.

d) To significantly reduce the computational complexity and number of parameters required in the decoder path.


### **What are the two main methods discussed in the course materials for implementing skip connections in neural network architectures?**

a) Using Batch Normalization layers alongside Dropout layers.

b) Applying ReLU activation functions followed by Max Pooling operations.

c) Element-wise addition of feature maps (as in ResNet) and concatenation of feature maps along the channel dimension (as in U-Net and DenseNet).

d) Replacing standard convolution operations with pooling operations.


### **What is the functional significance of the "identity path" provided by the skip connection in a ResNet block, especially concerning gradient flow during training?**

a) It primarily serves to introduce additional non-linearity into the skip connection path itself.

b) Its main purpose is to perform dimensionality reduction on the input before it's added to the block's output.

c) It provides a direct, uninterrupted pathway for the gradient to flow backward through the network, bypassing the potentially gradient-diminishing operations in the main convolutional path of the block, thus alleviating the vanishing gradient problem.

d) It significantly increases the effective receptive field of the convolutional layers within that specific block.


## Video 16 - Image Data Augmentation
* [Watch Video 16 on YouTube](https://youtu.be/Z6HymBkKoR4)

### **What is the primary purpose of data augmentation in computer vision tasks?**

a) To reduce the size of the training dataset for faster training.

b) To artificially expand the training dataset and improve model robustness and generalization by exposing it to more variations.

c) To simplify the training process by making all images look uniform.

d) To improve the resolution and quality of the original training images.


### **What does the translation (shifting) transformation help a model learn?**

a) That the object's size can vary within the image.

b) That the object's orientation (angle) can change.

c) That the object's classification is independent of its specific location within the image frame.

d) That the object can appear with different textures or surface patterns.


### **Why might vertical flipping be used cautiously or avoided for certain types of images like traffic signs or text?**

a) Because vertical flipping always distorts the image significantly, making it unrecognizable.

b) Because vertical flipping increases the computational cost of training substantially.

c) Because some objects have a canonical "up" direction, and flipping them vertically creates unrealistic or confusing examples (e.g., upside-down text is usually not encountered).

d) Because vertically flipping an image always changes the correct label associated with the image.


### **What is a key benefit of applying random data augmentation transformations (like flips, rotations, crops) differently during each training epoch?**

a) It significantly speeds up the training process by reducing the amount of data loaded per epoch.

b) It ensures that the model sees the exact same augmented version of each image multiple times, reinforcing learning.

c) It effectively increases the diversity of the training data seen by the model, forcing it to learn invariances (e.g., to position, orientation) and thus improve its ability to generalize to unseen data.

d) It reduces the overall computational cost and memory required for training compared to training without augmentation.


### **Why should data augmentation typically NOT be applied to the validation set during the training and evaluation loop?**

a) Because augmenting the validation set significantly increases the overall training time.

b) Because validation is only necessary once at the very end of the entire training process.

c) Because applying random augmentations to the validation set would introduce randomness into the evaluation metric, making it unreliable and non-deterministic for comparing models or deciding when to stop training.

d) Because augmenting validation data is the primary cause of model overfitting to the training set.


### **When incorporating data augmentation into a typical deep learning data loading pipeline (e.g., using PyTorch Datasets and DataLoaders), at which stage should the augmentation transformations be applied?**

a) Before splitting the original dataset into training, validation, and test sets, applied uniformly to all data.

b) Applied equally to all three datasets (training, validation, and test) after the split.

c) Applied only to the training set, typically within the Dataset.__getitem__ method or via the transforms argument of the Dataset/DataLoader, *after* the initial train/validation/test split has been made.

d) Applied only to the validation and test sets to make the evaluation more challenging and realistic.


## Video 17 - Regularization with Dropout and Batch Normalization
* [Watch Video 17 on YouTube](https://youtu.be/3kGE1vCmxag)

### **According to the video, what do both Dropout and Batch Normalization achieve in the context of neural networks?**

a) They both primarily focus on directly optimizing the value of the loss function during the forward pass.

b) They both act as regularization techniques, introducing noise or variability during training to prevent overfitting and improve generalization.

c) They both modify the input data directly before it enters the first layer of the network.

d) They both completely eliminate the possibility of the network overfitting the training data.


### **What happens to the activations of a neural network layer when Dropout is applied during training with a rate (probability) of <code>p=0.5</code>?**

a) All activations corresponding to negative input values are set to zero.

b) All activations are multiplied by a scaling factor of 0.5.

c) On average, 50% of the activation values are randomly selected and set to zero for that forward pass.

d) The mean of the activations across the batch is shifted by a value of 0.5.


### **What is the main operation performed by Batch Normalization during training?**

a) Randomly removing (setting to zero) entire connections between neurons in adjacent layers.

b) Normalizing the initial input data before it enters the network using global dataset statistics.

c) Normalizing the activations within a mini-batch (subtracting batch mean, dividing by batch standard deviation) and then applying learnable scaling and shifting parameters (gamma and beta).

d) Introducing non-linearity into the network by applying a function like ReLU or sigmoid.


### **During which phase of the model lifecycle (training or evaluation) is the Dropout mechanism typically active and randomly setting activations to zero?**

a) Only during the evaluation phase (model.eval()) to test robustness.

b) Only during the inference phase after the model has been fully deployed.

c) Only during the training phase (model.train()) to act as a regularizer.

d) During both training and evaluation phases, behaving identically in both.


### **What is the primary purpose of using Dropout as a regularization technique in neural networks?**

a) To significantly accelerate the convergence speed of the training process.

b) To perform automatic dimensionality reduction on the input data before it enters the network.

c) To prevent neurons from becoming overly reliant on the activations of a few specific other neurons, forcing the network to learn more distributed and robust representations, thus improving generalization and reducing overfitting.

d) To normalize the activations within each mini-batch to stabilize training dynamics, similar to Batch Normalization.


### **During model evaluation (<code>model.eval()</code>), how does the behavior of a Batch Normalization layer differ from its behavior during training (<code>model.train()</code>)?**

a) Batch Normalization is completely turned off and acts as an identity layer during evaluation.

b) The layer continues to calculate the mean and variance from the current input batch and uses these batch statistics for normalization, just like during training.

c) Instead of using the current batch's statistics, the layer uses the running estimates of the mean and variance (accumulated across batches during training) to normalize the activations.

d) The learnable affine parameters (gamma for scaling, beta for shifting) are disabled and set to 1 and 0 respectively during evaluation.


### **When is it essential to switch a PyTorch model containing layers like Dropout or Batch Normalization to evaluation mode using <code>model.eval()</code>?**

a) Only when saving the final trained model checkpoint to disk.

b) Only immediately after initializing the model, before starting the first training epoch.

c) Whenever performing inference (making predictions on new data) or evaluating the model's performance on a validation or test dataset.

d) It is generally optional and rarely makes a significant difference to the output.


### **What are the learnable affine transformation parameters introduced and optimized within a Batch Normalization layer?**

a) The running mean and running standard deviation accumulated during training.

b) The dropout probability p used in Dropout layers.

c) Gamma (γ), a scaling factor, and Beta (β), a shifting factor, applied after the initial normalization step.

d) The weights and biases associated with the preceding convolutional or linear layer.


## Video 18 - Transfer Learning and Fine-tuning
* [Watch Video 18 on YouTube](https://youtu.be/_JOYVFW96xY)

### **What is a primary benefit of using transfer learning for deep learning practitioners?**

a) It always guarantees higher accuracy compared to training a model from scratch on the target dataset.

b) It leverages knowledge learned from a large source dataset, often allowing good performance on a target task with significantly less labeled target data and/or faster training convergence.

c) It completely eliminates the need for any data augmentation on the target dataset.

d) It automatically selects the most optimal neural network architecture for the target task.


### **What is the ImageNet 1K dataset primarily known for in the context of deep learning?**

a) Its extremely small size and suitability for quick testing of simple classification models.

b) Its primary focus on natural language processing tasks like text generation.

c) Being a large-scale benchmark dataset for image classification, containing over a million images across 1000 diverse object categories, often used for pre-training vision models.

d) Having a constantly updated public test set that allows researchers to directly compare model performance year-round.


### **What is the core idea behind transfer learning?**

a) Training a very large, complex model exclusively on a very small target dataset.

b) Re-using knowledge (features, weights) learned by a model trained on one task (source task) as a starting point for training a model on a different but related task (target task).

c) Initializing all the weights of a neural network completely randomly before starting training on the target task.

d) Training multiple different models on the same target data and then averaging their predictions to get a final result.


### **When adapting a ResNet50 pre-trained on ImageNet for a new classification task with 10 classes, what is a common and essential modification to the network architecture?**

a) Removing several of the initial convolutional layers (the "backbone").

b) Changing the activation function (e.g., from ReLU to Sigmoid) in all layers.

c) Replacing or modifying the final fully connected layer (the "classifier head") to have 10 output units instead of the original 1000.

d) Adding extra batch normalization layers before every single convolutional layer in the network.


### **In the context of transfer learning using models pre-trained on ImageNet, what kind of visual features are typically captured by the initial (early) convolutional layers of the network?**

a) Highly complex and object-specific features like complete faces, car models, or specific dog breeds.

b) Features that are exclusively relevant only to the specific target dataset the model will eventually be fine-tuned on.

c) General, low-level visual primitives such as edges, corners, color blobs, textures, and simple gradients, which are common across many types of natural images.

d) Abstract semantic concepts and relationships between objects within the image scene.


### **Why might a sophisticated ResNet50 model, pre-trained extensively on the diverse ImageNet dataset, still perform poorly when directly applied (without fine-tuning) to classifying images of rotten fruits (apples, bananas, oranges)?**

a) Because ImageNet primarily contains very low-resolution images (e.g., 32x32) that don't match the rotten fruit images.

b) Because ResNet50 has too many layers (is too deep), making it inherently unsuitable for a seemingly simple task like fruit classification.

c) Because the ImageNet dataset, while diverse, likely contains very few or no examples of fruits in a state of decay or rot. The model hasn't learned the specific visual features associated with rottenness.

d) Because the learning rate used during the original ImageNet pre-training was likely too high, preventing the model from learning subtle features.


## Video 19 - Interpretability with Class Activation Mapping
* [Watch Video 19 on YouTube](https://youtu.be/Gs1brxEsG3c)

### **What is the primary purpose of Class Activation Mapping (CAM) and its variants like Grad-CAM?**

a) To significantly improve the final classification accuracy of Convolutional Neural Networks (CNNs).

b) To provide visual explanations ("interpretability") for CNN predictions by highlighting the image regions most influential for a particular class decision.

c) To drastically reduce the computational cost and memory usage of CNNs during inference.

d) To accelerate the training process of CNNs, especially on very large datasets.


### **What specific architectural component or operation is essential for the original Class Activation Mapping (CAM) technique to work directly (without modification)?**

a) Max Pooling layers used throughout the network.

b) Average Pooling layers used instead of Max Pooling.

c) A Global Average Pooling (GAP) layer applied to the final convolutional feature maps, followed by a fully connected layer for classification.

d) Stochastic Pooling layers for regularization.


### **What is a key advantage of Gradient-weighted Class Activation Mapping (Grad-CAM) over the original CAM technique?**

a) Grad-CAM is significantly faster and requires less memory to compute than the original CAM.

b) Grad-CAM requires modifying the CNN architecture to include a Global Average Pooling (GAP) layer before the final classifier.

c) Grad-CAM is more general and can be applied to a wider range of CNN architectures without requiring specific layers like GAP; it can visualize activations from various convolutional layers.

d) Grad-CAM does not require calculating gradients, making it simpler to implement.


### **What does overlaying the Class Activation Map (CAM) heatmap onto the original input image primarily help to visualize?**

a) The precise mathematical flow of data and gradients through each layer of the neural network.

b) The magnitude of the gradients calculated during backpropagation for each pixel in the image.

c) The spatial regions or areas within the input image that the neural network found most important or influential in making its prediction for a specific target class.

d) The theoretical receptive field boundaries for the neurons located in the final convolutional layer of the network.


### **In the context of implementing Class Activation Mapping (CAM) or its variants in PyTorch, what is the purpose of using a "hook"?**

a) To directly modify the learned weights of specific layers in the neural network during the forward or backward pass.

b) To register a function that intercepts the forward or backward pass at a specific layer, allowing access to intermediate outputs (activations) or gradients without altering the network's definition.

c) To automatically implement the Global Average Pooling (GAP) operation required for the original CAM technique.

d) To visualize the computational graph and the flow of gradients during the backpropagation process.


### **When interpreting a classifier trained on potentially "dirty" or biased data using CAM, what potential issue might the visualization reveal?**

a) The CAM heatmap might consistently highlight irrelevant background regions or artifacts that happen to be spuriously correlated with the target class in the biased training data, rather than focusing on the actual object features.

b) The CAM heatmap might fail to produce any activation whatsoever, indicating the model hasn't learned anything.

c) The CAM visualization might consistently highlight the exact same small region in every image, regardless of the predicted class.

d) The resolution of the CAM heatmap might become too low to provide any meaningful spatial insights due to the dirty data.


## Video 20 - Image Embeddings
* [Watch Video 20 on YouTube](https://youtu.be/2JvSIbM3NHM)

### **What is the primary purpose of image embedding algorithms?**

a) To significantly compress image file sizes for efficient storage and transmission.

b) To transform raw pixel data into lower-dimensional, dense vector representations (embeddings) where visually or semantically similar images have nearby vectors in the embedding space.

c) To artificially enhance the resolution and visual quality of low-resolution images.

d) To directly classify images into a predefined set of categories with high accuracy.


### **Which metric is commonly used to measure the similarity between two embedding vectors based on the angle between them, effectively ignoring their magnitudes?**

a) Euclidean distance (L2 distance)

b) Cosine similarity

c) Mean Squared Error (MSE)

d) Cross-entropy loss


### **What is a key advantage of using image embeddings extracted from a layer of a pre-trained model (like ResNet trained on ImageNet)?**

a) These embeddings are guaranteed to provide the absolute best possible performance for any downstream task without further modification.

b) They are computationally extremely cheap to obtain, requiring almost no processing power.

c) They encapsulate rich, hierarchical visual features learned from a large and diverse dataset (ImageNet), making them effective general-purpose representations for various vision tasks (like similarity search, clustering, or as input to smaller models).

d) They are specifically designed and optimized for only one very narrow task, such as detecting a single type of object.


### **How do neural networks, particularly CNNs, typically produce image embeddings (vector representations)?**

a) By directly using the one-hot encoded class label predicted for the image as the embedding.

b) By applying a fixed mathematical transformation (like PCA or Fourier Transform) directly to the raw pixel values.

c) By processing the image through multiple layers of learned transformations (convolutions, non-linearities, pooling) that extract increasingly abstract features, and then taking the activations from one of the later layers (often before the final classification layer) as the embedding vector.

d) By looking up the image in a large, predefined dictionary that maps every possible image to a unique embedding vector.


### **Which of the following methods were discussed as ways to generate image embeddings using neural networks?**

a) Method 1: Flattening the raw image pixels and feeding them directly into one or more fully connected (linear) layers.

b) Method 2: Using several convolutional layers to extract spatial features first, then flattening the resulting feature map and feeding it into fully connected layers.

c) Method 3: Using convolutional layers followed by a Global Pooling layer (e.g., Global Average Pooling) to reduce the feature map to a fixed-size vector without flattening.

d) All of the above methods (a, b, and c) are valid approaches discussed.


### **What is the objective of using triplet loss for training image embedding models?**

a) To significantly improve the speed and efficiency of generating embeddings during inference.

b) To train the network such that the embedding vector for an "anchor" image is closer to the embedding of a "positive" sample (similar image) than it is to the embedding of a "negative" sample (dissimilar image), by at least a predefined margin.

c) To compress the dimensionality of the resulting embedding vectors as much as possible while preserving all information.

d) To directly train the network to classify images into predefined categories using the learned embeddings.


### **What does a high cosine similarity score (e.g., close to +1.0) between the embedding vectors of two images typically indicate?**

a) The two images are likely visually very different or semantically unrelated.

b) The Euclidean distance between the two embedding vectors in the vector space is also guaranteed to be very large.

c) The embedding vectors point in very similar directions in the vector space, suggesting that the images are likely to be visually or semantically similar according to the learned representation.

d) The magnitudes (lengths) of the two embedding vectors are necessarily very different from each other.


## Video 21 - Vision Transformers (ViT)
* [Watch Video 21 on YouTube](https://youtu.be/GCPQVVsoEvs)

### **What is the purpose of the initial linear projection applied to the flattened image patches in a Vision Transformer (ViT)?**

a) To significantly reduce the dimensionality of the flattened patches for computational efficiency.

b) To transform or project the flattened, high-dimensional patches into lower-dimensional vector embeddings (patch embeddings).

c) To explicitly add positional information, indicating where each patch came from in the original image.

d) To normalize the pixel values within each patch to have zero mean and unit variance.


### **What are the three key inputs generated from the sequence of embeddings (patch embeddings + class token + positional embeddings) that are fed into the Multi-Head Self-Attention mechanism within a Transformer encoder block?**

a) The original image patches before flattening.

b) Flattened raw pixel vectors for each patch.

c) Query (Q), Key (K), and Value (V) matrices derived from the input embeddings.

d) Convolutional feature maps extracted by a CNN backbone.


### **What is typically the first step in processing an input image within a standard Vision Transformer (ViT) architecture?**

a) Applying a series of large-kernel convolutional filters across the entire input image.

b) Splitting the input image into a grid of smaller, non-overlapping (or sometimes overlapping) fixed-size patches.

c) Performing a global non-linear activation function (like ReLU) on all pixel values simultaneously.

d) Computing the 2D Fourier Transform of the input image to work in the frequency domain.


### **In a Vision Transformer (ViT), after the image patches are flattened and projected into embeddings, what crucial piece of information must be added to these patch embeddings before they are processed by the Transformer Encoder layers?**

a) The predicted class label for the entire image.

b) Pixel-level semantic segmentation masks corresponding to each patch.

c) Positional information (Positional Embeddings), indicating the original spatial location (position) of each patch within the image grid.

d) Detailed color histograms calculated individually for each image patch.


### **What is often cited as a significant drawback or challenge of Vision Transformers (ViTs) compared to traditional Convolutional Neural Networks (CNNs), especially when training from scratch?**

a) Their inherent inability to model long-range dependencies between distant parts of an image.

b) Their generally poor performance when trained on very large datasets (like ImageNet or JFT-300M).

c) Their higher demand for computational resources (compute power, memory) and significantly larger amounts of training data to achieve strong performance, partly due to their lack of strong inductive biases like locality.

d) A complete lack of interpretability, making it impossible to understand which parts of the image influenced the prediction.


### **What does the term "locality bias" refer to in the context of Convolutional Neural Networks (CNNs)?**

a) The tendency of CNNs to focus primarily on the central region of an input image, ignoring the borders.

b) The inductive bias built into the convolution operation, assuming that spatially nearby pixels are more strongly correlated and that meaningful features can be extracted by processing local neighborhoods with shared filters.

c) The significantly increased computational cost associated with processing very high-resolution images using standard convolutional filters.

d) The inherent limitation of early CNN layers in capturing global context or relationships between distant parts of the image.


### **What does "translational equivariance" (or approximate equivariance) mean for Convolutional Neural Networks (CNNs)?**

a) The network's predictions remain consistent even if the lighting conditions or colors in the input image change significantly.

b) If an object in the input image is shifted (translated) horizontally or vertically, the representation of that object in the feature maps produced by convolutional layers will also shift by a corresponding amount.

c) The network can recognize an object successfully regardless of its size or scale within the image.

d) The network's ability to generalize its learned knowledge effectively to completely new datasets it has never seen before.


## Video 22 - CLIP - Contrastive Language-Image Pretraining
* [Watch Video 22 on YouTube](https://youtu.be/Rvy1SrgQlDk)

### **What is the primary goal of Contrastive Language-Image Pretraining (CLIP)?**

a) To generate highly realistic, novel images directly from complex text descriptions.

b) To train highly accurate image classification models using only large labeled image datasets, ignoring language.

c) To learn a shared multimodal embedding space where representations of semantically similar images and text descriptions are close together, enabling zero-shot transfer.

d) To primarily improve the performance of natural language processing tasks (like translation or summarization) by incorporating visual context.


### **What key capability, enabling classification on unseen categories without task-specific training, arises directly from CLIP's learned shared embedding space for text and images?**

a) Real-time, high-frame-rate video processing and action recognition.

b) Zero-shot classification based on natural language prompts.

c) Generation of photorealistic images with extremely high resolution (e.g., 4K).

d) Detailed understanding and reconstruction of complex 3D scenes from 2D images.


### **How does CLIP's contrastive training process encourage the alignment of corresponding text and image embeddings?**

a) By using completely separate loss functions and optimizers for the text encoder and the image encoder.

b) By attempting to minimize the Euclidean distance between the embeddings of all text-image pairs in a batch.

c) By using a symmetric contrastive loss (like InfoNCE) that maximizes the cosine similarity between embeddings of true (image, text) pairs while minimizing similarity for incorrect pairs within a batch.

d) By employing a Generative Adversarial Network (GAN) framework where one network generates embeddings and another tries to discriminate between real and fake pairs.


### **What is a significant advantage of CLIP's zero-shot classification capability compared to traditional supervised classification?**

a) It consistently achieves significantly higher accuracy than models specifically fine-tuned on the target dataset.

b) It allows a pre-trained CLIP model to classify images into novel categories defined by text prompts, without needing any labeled image examples or retraining specifically for those new categories.

c) It enables the model to directly predict precise bounding boxes or segmentation masks for objects described in the text prompts.

d) It drastically reduces the computational resources required to train the initial CLIP model compared to standard supervised models.


### **According to the original OpenAI paper and common observations, in which types of tasks might a specialized model, fine-tuned specifically for that task, potentially outperform zero-shot CLIP?**

a) General, broad-category image classification across diverse domains (like classifying everyday objects).

b) Performing semantic image search based on natural language queries across large, varied image datasets.

c) Highly specialized, fine-grained tasks such as counting specific objects in complex scenes (e.g., CLEVR), recognizing handwritten digits (e.g., MNIST), or performing classification within very specific technical domains (e.g., medical imaging subtypes).

d) Classifying images based on abstract or compositional textual descriptions that require nuanced understanding.


## Video 23 - Approaches to Object Detection
* [Watch Video 23 on YouTube](https://youtu.be/13geNm84sns)

### **What are the typical components combined in the loss function for training an object detector?**

a) Only a regression loss measuring the accuracy of the predicted bounding box coordinates.

b) Only a classification loss measuring the accuracy of the predicted object class label.

c) Both a regression loss (for bounding box localization) and a classification loss (for object category).

d) A loss function based solely on the total number of objects detected in the image.


### **What is the fundamental idea behind using anchor boxes in many object detection models (like Faster R-CNN, SSD, YOLOv2/v3)?**

a) Anchor boxes represent the final, precise bounding box predictions output directly by the model.

b) Anchor boxes are used to perform pixel-level segmentation of the objects within the boxes.

c) Anchor boxes are a set of predefined reference boxes with various sizes (scales) and aspect ratios, centered at different locations on the feature map, which the model refines to predict final bounding boxes.

d) Anchor boxes are learnable vector embeddings that represent general object features or queries.


### **Which of the following object detection models represents an anchor-free approach, often utilizing learned object queries or point-based predictions instead of refining predefined anchor boxes?**

a) Faster R-CNN

b) RetinaNet

c) YOLOv3

d) DETR (Detection Transformer)


### **What is a key conceptual difference between single-shot detectors (e.g., SSD, YOLO, RetinaNet) and two-stage detectors (e.g., Faster R-CNN)?**

a) Two-stage detectors are generally significantly faster during inference than single-shot detectors.

b) Two-stage detectors explicitly perform a region proposal step first to identify candidate object regions (Regions of Interest - RoIs), and then classify and refine boxes for these proposals in a second stage. Single-shot detectors predict boxes and classes directly from feature maps in one go.

c) Single-shot detectors primarily use anchor boxes, whereas two-stage detectors never use anchor boxes.

d) Single-shot detectors typically achieve higher accuracy, especially on small objects, compared to two-stage detectors.


### **What type of label information is primarily required for the object detection task in computer vision?**

a) Textual descriptions of the image content.

b) Pixel-level masks delineating object boundaries.

c) Bounding boxes indicating the location of objects of interest alongside the class label for each box.

d) Global labels identifying the presence of certain object categories.


### **Object detection fundamentally accomplishes which two primary tasks for each object of interest in an image?**

a) Image-level classification only (identifying categories present).

b) Pixel-level segmentation only (delineating object shapes).

c) Classification (identifying the object's category) and Localization (determining its position and extent, typically via a bounding box).

d) Localization only (finding object positions without identifying them).


### **Which of the following models is provided as a prominent example of a two-stage object detector?**

a) YOLO (You Only Look Once)

b) RetinaNet

c) Faster R-CNN

d) DETR (Detection Transformer)


### **What is the primary advantage or key capability highlighted for the Grounding DINO model in the context of object detection?**

a) Achieving significantly higher detection accuracy on standard benchmarks compared to all previous fine-tuned models.

b) Offering much faster inference speed suitable for real-time applications on edge devices.

c) Enabling open-set or language-guided detection, where objects can be detected based on arbitrary text descriptions or prompts, not just predefined categories.

d) Demonstrating superior performance specifically in handling heavily occluded objects compared to anchor-based methods.


## Video 24 - Deep Learning Approaches to Image Segmentation
* [Watch Video 24 on YouTube](https://youtu.be/NtHU9GVccJw)

### **What is the primary goal of semantic segmentation?**

a) To assign a class label to every pixel in the image, grouping pixels belonging to the same object category together.

b) To detect and draw bounding boxes around individual objects and assign a class label to each box.

c) To separate and provide a unique mask for each individual object instance, even if they belong to the same class.

d) To generate class-agnostic (unlabeled) masks for salient objects specified by user prompts.


### **Which type of segmentation distinguishes between different instances of the same object class (e.g., labeling car #1 differently from car #2)?**

a) Semantic segmentation

b) Instance segmentation

c) Panoptic segmentation

d) Class-agnostic segmentation


### **Panoptic segmentation aims to provide a unified segmentation map by combining which two types of segmentation?**

a) Semantic segmentation and class-agnostic segmentation.

b) Instance segmentation and class-agnostic segmentation.

c) Semantic segmentation and instance segmentation.

d) Object detection and semantic segmentation.


### **What does it mean for the Segment Anything Model (SAM) to be "prompt-driven"?**

a) It automatically segments every single object and region in an image without requiring any user input or guidance.

b) It requires the user to provide specific class labels (like "cat" or "dog") as prompts to generate the corresponding masks.

c) It relies on user-provided input prompts—such as points on an object, a bounding box around an object, or potentially text—to specify *what* should be segmented.

d) It is trained entirely using only text prompts paired with images, without any mask annotations.


### **What type of loss function is typically minimized during the training of a semantic segmentation model by comparing the predicted pixel-level class probabilities with the ground truth segmentation mask?**

a) Mean Squared Error (MSE) Loss

b) Pixel-wise Cross Entropy Loss

c) Focal Loss (though a variant of Cross Entropy, Cross Entropy is the base)

d) Triplet Loss


### **Which specific model architecture is described as being a versatile, transformer-based approach capable of performing instance, semantic, and panoptic segmentation within a unified framework?**

a) Mask R-CNN

b) U-Net

c) Mask2Former

d) Segment Anything Model (SAM)


### **The U-Net architecture was originally developed and gained prominence primarily for which specific image segmentation task?**

a) Instance segmentation in natural images.

b) Panoptic segmentation of outdoor driving scenes.

c) Semantic segmentation of biomedical images.

d) Class-agnostic segmentation guided by text prompts.


### **What is a key distinguishing characteristic of the Segment Anything Model (SAM)?**

a) It directly outputs semantic class labels along with the segmentation masks it generates.

b) It is specifically optimized for performing instance segmentation on a small, predefined set of common object categories.

c) It is designed to generate class-agnostic segmentation masks based on various forms of input prompts (points, boxes, text), allowing it to segment potentially any object or region specified by the user.

d) It requires extensive fine-tuning with large amounts of labeled data for each specific object class it needs to segment.


## Video 25 - Image Generation with Diffusion Models
* [Watch Video 25 on YouTube](https://youtu.be/NtHU9GVccJw)

### **What is the primary goal of the forward diffusion process in diffusion models?**

a) To generate high-quality, realistic images starting from random noise.

b) To systematically and gradually add noise (typically Gaussian) to an input image over a sequence of steps, eventually transforming it into pure noise.

c) To take a noisy image and remove the noise in a single step to recover the original clean image.

d) To predict the original clean image directly from a noisy image using a learned function.


### **What is the role of the 'noise schedule' (often defined by βₜ values) in the forward diffusion process?**

a) It determines the specific architecture (e.g., U-Net) of the neural network used for the reverse denoising process.

b) It defines the amount (variance) of noise that is added at each specific time step t during the forward diffusion process, controlling how quickly the image degrades into noise.

c) It specifies the method used to generate the initial random noise vector z from which the image generation (reverse process) starts.

d) It dictates the type of loss function (e.g., L1, L2) used to train the neural network in the reverse process.


### **What is the main task of the neural network trained for the reverse diffusion process?**

a) To add precisely controlled noise to an initially clean image according to the noise schedule.

b) Given a noisy image xₜ at time step t, to predict the noise component ε that was added to get xₜ from xₜ₋₁ (or related quantities like the original image x₀).

c) To directly generate a high-quality image from a random noise vector in a single forward pass, similar to a GAN generator.

d) To encode text prompts or other conditioning information into vector embeddings suitable for guiding image generation.


### **What is a key characteristic of the image generation process in diffusion models?**

a) They generate images instantaneously in a single forward pass, similar to a Generative Adversarial Network (GAN) generator.

b) They directly translate text prompts into pixel values using a large transformer model without any intermediate noise steps.

c) They operate iteratively, starting from pure random noise and gradually denoising it over a sequence of steps, guided by a learned model, to produce a coherent image.

d) They rely on an adversarial training paradigm where a generator model tries to fool a discriminator model that distinguishes real images from generated ones.


### **What is the "reparameterization trick" used for, as mentioned in the video in the context of the forward diffusion process?**

a) It's a technique primarily used to significantly speed up the training convergence of the reverse diffusion (denoising) model.

b) It's a method for generating more diverse and realistic noise patterns during the forward diffusion process itself.

c) It's a mathematical technique that allows gradients to be backpropagated through the random noise sampling step in the forward process formulation, making it possible to train models (like VAEs, though mentioned here in the diffusion context conceptually) that involve sampling from a distribution.

d) It's a strategy used to compress the image into a compact latent space representation before initiating the noise addition process.


### **What is the typical role of CLIP (Contrastive Language-Image Pretraining) models when used to guide image generation with diffusion models (like in Stable Diffusion or DALL-E 2)?**

a) CLIP models are used to execute the forward diffusion process, adding noise to the initial image samples.

b) The CLIP image encoder itself serves as the primary U-Net architecture for the reverse diffusion (denoising) network.

c) Text embeddings generated by the CLIP text encoder provide conditioning information to the denoising network (e.g., U-Net), guiding the iterative denoising process to generate an image that matches the semantic content of the input text prompt.

d) CLIP models are used to generate the initial random noise tensor from which the image generation process begins.
