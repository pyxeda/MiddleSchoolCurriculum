'''Copyright (c) 2021 AIClub

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated 
documentation files (the "Software"), to deal in the Software without restriction, including without 
limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of 
the Software, and to permit persons to whom the Software is furnished to do so, subject to the following 
conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial
portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT 
LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO 
EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN 
AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE 
OR OTHER DEALINGS IN THE SOFTWARE.'''

# Import pre trained BertTokenizer and sequence classifier
from transformers import BertTokenizer, TFBertForSequenceClassification

# Import inputexample and inputfeatures
from transformers import InputExample, InputFeatures

# Import os module
import os

# The shutil module gives high-level operations on files and collections of files.
import shutil

# Import tensorflow module
import tensorflow as tf

# Import pandas
import pandas as pd

# Model by the Sequence Classifier
model = TFBertForSequenceClassification.from_pretrained("bert-base-uncased")

# Derive tokenizer with BERT Tokenizer.
tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")

# Get model summary
model.summary()

dataset = r'aclImdb_v1.tar.gz'

# Create  the main directory path
main_dir = os.path.join(os.path.dirname(dataset), 'aclImdb')

# Create the sub directory path ("/aclImdb/train")
train_dir = os.path.join(main_dir, 'train')

# Remove unsup folder
remove_dir = os.path.join(train_dir, 'unsup')
shutil.rmtree(remove_dir)

# Process entire data in a single batch
# Create a training dataset and a validation 
# Dataset from the "aclImdb/train" directory with a 80/20 split.
train = tf.keras.preprocessing.text_dataset_from_directory(
    'aclImdb/train', batch_size=30000, validation_split=0.2, 
    subset='training', seed=123)
test = tf.keras.preprocessing.text_dataset_from_directory(
    'aclImdb/train', batch_size=30000, validation_split=0.2, 
    subset='validation', seed=123)

# Convert train Dataset object to train pandas dataframe
for i in train.take(1):
  train_feat = i[0].numpy()
  train_lab = i[1].numpy()

train = pd.DataFrame([train_feat, train_lab]).T
train.columns = ['DATA_COLUMN', 'LABEL_COLUMN']
train['DATA_COLUMN'] = train['DATA_COLUMN'].str.decode("utf-8")

# Convert test Dataset object to test pandas dataframe
for j in test.take(1):
  test_feat = j[0].numpy()
  test_lab = j[1].numpy()

test = pd.DataFrame([test_feat, test_lab]).T
test.columns = ['DATA_COLUMN', 'LABEL_COLUMN']
test['DATA_COLUMN'] = test['DATA_COLUMN'].str.decode("utf-8")

# Get train and test datasets and convert each row into an InputExample object
def convert_data_to_examples(train, test, DATA_COLUMN, LABEL_COLUMN): 
  train_InputExamples = train.apply(lambda x: InputExample(guid=None,
                                                          text_a = x[DATA_COLUMN], 
                                                          text_b = None,
                                                          label = x[LABEL_COLUMN]), axis = 1)

  validation_InputExamples = test.apply(lambda x: InputExample(guid=None,
                                                          text_a = x[DATA_COLUMN], 
                                                          text_b = None,
                                                          label = x[LABEL_COLUMN]), axis = 1)
  
  return train_InputExamples, validation_InputExamples

# Tokenize the InputExample objects
# Create the required input format with the tokenized objects
# Create an input dataset that we can feed to the model
def convert_examples_to_tf_dataset(examples, tokenizer, max_length=128):
    # Keep input features that needs to converted later
    features = []

    for e in examples:
        input_dict = tokenizer.encode_plus(
            e.text_a,
            add_special_tokens=True,
            max_length=max_length,
            return_token_type_ids=True,
            return_attention_mask=True,
            pad_to_max_length=True,
            truncation=True
        )

        input_ids, token_type_ids, attention_mask = (input_dict["input_ids"],
            input_dict["token_type_ids"], input_dict['attention_mask'])

        features.append(
            InputFeatures(
                input_ids=input_ids, attention_mask=attention_mask, token_type_ids=token_type_ids, label=e.label
            )
        )

    def gen():
        for f in features:
            yield (
                {
                    "input_ids": f.input_ids,
                    "attention_mask": f.attention_mask,
                    "token_type_ids": f.token_type_ids,
                },
                f.label,
            )

    return tf.data.Dataset.from_generator(
        gen,
        ({"input_ids": tf.int32, "attention_mask": tf.int32, "token_type_ids": tf.int32}, tf.int64),
        (
            {
                "input_ids": tf.TensorShape([None]),
                "attention_mask": tf.TensorShape([None]),
                "token_type_ids": tf.TensorShape([None]),
            },
            tf.TensorShape([]),
        ),
    )

# Define data coloumn and label coloumn
DATA_COLUMN = 'DATA_COLUMN'
LABEL_COLUMN = 'LABEL_COLUMN'

# Call the above created functions with the following inputs
train_InputExamples, validation_InputExamples = convert_data_to_examples(train, test, DATA_COLUMN, LABEL_COLUMN)

train_data = convert_examples_to_tf_dataset(list(train_InputExamples), tokenizer)
train_data = train_data.shuffle(100).batch(32).repeat(2)

validation_data = convert_examples_to_tf_dataset(list(validation_InputExamples), tokenizer)
validation_data = validation_data.batch(32)

# Used Adam as the optimizer, 
# Used CategoricalCrossentropy as the loss function
# Used SparseCategoricalAccuracy as the accuracy metric
model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=3e-5, epsilon=1e-08, clipnorm=1.0), 
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True), 
              metrics=[tf.keras.metrics.SparseCategoricalAccuracy('accuracy')])

# Fit the training data
model.fit(train_data, epochs=2, validation_data=validation_data, steps_per_epoch=2)

# Define two sentences which will be used as an input
# First sentence is positive and the second one is negative
pred_sentences = ['This was an awesome movie. I watch it twice my time watching this beautiful movie if I have known it was this good',
                  'One of the worst movies of all time. I cannot believe I wasted two hours of my life for this movie']

# Tokenize the reviews with the pre trained bert tokenizer
tf_batch = tokenizer(pred_sentences, max_length=128, padding=True, truncation=True, return_tensors='tf')

# Give the tokenized reviews to the model
tf_outputs = model(tf_batch)

# Run a softmax layer to get the predictions
tf_predictions = tf.nn.softmax(tf_outputs[0], axis=-1)

# Define the lables
labels = ['Negative','Positive']

# Deternmine the prediction is negative or positive by using argmax function
label = tf.argmax(tf_predictions, axis=1)
label = label.numpy()

# Print the predicted results along with their input sentences
for i in range(len(pred_sentences)):
  print(pred_sentences[i], ": \n", labels[label[i]])