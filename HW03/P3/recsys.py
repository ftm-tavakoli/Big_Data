import numpy as np


class MatrixFactorization:
    def __init__(self, num_items, num_users, num_factors, learning_rate, regularization_rate, num_iterations):
        """
        Initialize the Matrix Factorization model.

        Args:
            num_items (int): Number of items.
            num_users (int): Number of users.
            num_factors (int): Number of latent factors.
            learning_rate (float): Learning rate for gradient descent.
            regularization_rate (float): Regularization rate for L2 regularization.
            num_iterations (int): Number of iterations for training.
        """
        self.num_items = num_items
        self.num_users = num_users
        self.num_factors = num_factors
        self.learning_rate = learning_rate
        self.regularization_rate = regularization_rate
        self.num_iterations = num_iterations

        # Initialize Q and P matrices with random values
        # Start your code

        # End your code

    def sigmoid(self, x):
        """
        Compute the sigmoid function.

        Args:
            x (float): Input value.

        Returns:
            float: Sigmoid value.
        """
        return 1 / (1 + np.exp(-x))

    def update_parameters(self, R):
        """
        Update the parameters Q and P using Stochastic Gradient Descent.

        Args:
            R (ndarray): Rating matrix.
        """
        # Start your code

        # End your code

    def train(self, R):
        """
        Train the Matrix Factorization model.

        Args:
            R (ndarray): Rating matrix.
        """
        self.update_parameters(R)

    def predict_rating(self, i, u):
        """
        Predict the rating for item i and user u.

        Args:
            i (int): Item index.
            u (int): User index.

        Returns:
            float: Predicted rating.
        """
        # Start your code

        # End your code

    def evaluate(self, users_list, groundTruth_list, topk=10):
        """
        Evaluate trained model for item i and user u

        Args:
            users_list (list): Users indexes list.
            groundTruth_list (list) : list of items in users test set
            topk (int): threshold for top item selection

        Returns:
            float: sum(Intersection between topk predicted items and user profile in test set / user profile size in test set) / len(users_list)
        """
        # Start your code

        # End your code


num_items = None
num_users = None
num_factors = None
learning_rate = None
regularization_rate = None
num_iterations = None

R = None  # rating matrix

model = MatrixFactorization(num_items, num_users, num_factors, learning_rate, regularization_rate,
                            num_iterations)
model.train(R)

# Test prediction for item 0 and user 0
item_index = 0
user_index = 0
prediction = model.predict_rating(item_index, user_index)
print(f"Predicted rating for item {item_index} and user {user_index}: {prediction}")

# Evaluate model for users in test set
user_indexes = None
groudTruths = None
result = model.evaluate(user_indexes, groudTruths)
print(f"Accuracy for model: {result}")
