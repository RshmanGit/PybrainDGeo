import dataMan
import tensorflow as tf

# data work
dataMan.load_all_data()
data = dataMan.get_data()
mean_key = dataMan.get_mean_key()
var_key = dataMan.get_var_key()
norm_data = dataMan.get_norm_data()
n_samples = len(data['nox'])

# algorithm structure
learning_rate = 0.001
training_epochs = 15
batch_size = 100
display_step = 1

n_input = 3
n_hidden_1 = 9
n_hidden_2 = 7
n_hidden_3 = 5
n_output = 4

# inputs
x = tf.placeholder("float", [None, n_input])
y = tf.placeholder("float", [None, n_output])


# model design
def multilayer_perceptron(x, weights, biases):
    in_layer = tf.add(tf.matmul(x, weights['h1']), biases['b1'])
    in_layer = tf.nn.sigmoid(in_layer)

    hid_layer_1 = tf.add(tf.matmul(in_layer, weights['h2']), biases['b2'])
    hid_layer_2 = tf.add(tf.matmul(hid_layer_1, weights['h3']), biases['b3'])

    out_layer = tf.add(tf.matmul(hid_layer_2, weights['h4']), biases['b4'])
    out_layer = tf.nn.sigmoid(out_layer)
    return out_layer


weights = {
    'h1': tf.Variable(tf.random_normal([n_input, n_hidden_1])),
    'h2': tf.Variable(tf.random_normal([n_hidden_1, n_hidden_2])),
    'h3': tf.Variable(tf.random_normal([n_hidden_2, n_hidden_3])),
    'h4': tf.Variable(tf.random_normal([n_hidden_3, n_output]))
}

biases = {
    'b1': tf.Variable(tf.random_normal([n_hidden_1])),
    'b2': tf.Variable(tf.random_normal([n_hidden_2])),
    'b3': tf.Variable(tf.random_normal([n_hidden_3])),
    'b4': tf.Variable(tf.random_normal([n_output]))
}

# construct model
pred = multilayer_perceptron(x, weights, biases)

# define loss and optimizer
cost = tf.reduce_sum(tf.pow(pred - y, 2))/(2*n_samples)
# gradient descent
optimizer = tf.train.GradientDescentOptimizer(learning_rate).minimize(cost)

init = tf.global_variables_initializer()

#with tf.Session() as sess:
#    sess.run(init)

#    for epoch in range(training_epochs):
#        for (x, y) in zip():
#            pass