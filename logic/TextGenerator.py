import tensorflow as tf

import os
import time


class TextGenerator:
    def __init__(self, fileData=None, epochsCount=20, optimizer = 'adam', temperature=0.5, sequenceLength=100, batchSize=64, generationType = 'NEW' ) -> None:
        self.textData = fileData
        self.epochsCount = epochsCount
        self.optimizer = optimizer
        self.temperature = temperature
        self.sequenceLength = sequenceLength
        self.batchSize = batchSize
        self.generationType = generationType


    def getUniqueCharacters(self):
        self.vocab = sorted(set(self.textData))

    def vectorizeText(self):
        example_texts = ['abcdefg', 'xyz']

        chars = tf.strings.unicode_split(example_texts, input_encoding='UTF-8')

        self.ids_from_chars = tf.keras.layers.StringLookup(
        vocabulary=list(self.vocab), mask_token=None)

        ids = self.ids_from_chars(chars)
        chars_from_ids = tf.keras.layers.StringLookup(vocabulary=self.ids_from_chars.get_vocabulary(), invert=True, mask_token=None)

        self.chars_from_ids = tf.keras.layers.StringLookup(vocabulary=self.ids_from_chars.get_vocabulary(), invert=True, mask_token=None)

        chars = chars_from_ids(ids)

        tf.strings.reduce_join(chars, axis=-1).numpy()

    def text_from_ids(self,ids):
        return tf.strings.reduce_join(self.chars_from_ids(ids), axis=-1)

    def prediction(self):
        all_ids = self.ids_from_chars(tf.strings.unicode_split(self.textData, 'UTF-8'))

        self.ids_dataset = tf.data.Dataset.from_tensor_slices(all_ids)

    def setSequences(self):
        seq_length = self.sequenceLength

        sequences = self.ids_dataset.batch(seq_length+1, drop_remainder=True)

        self.dataset = sequences.map(self.split_input_target)

    def split_input_target(self,sequence):
        input_text = sequence[:-1]
        target_text = sequence[1:]
        return input_text, target_text

    def createTrainingBatches(self):
        BATCH_SIZE = self.batchSize

        BUFFER_SIZE = 10000

        self.dataset = (self.dataset.shuffle(BUFFER_SIZE).batch(BATCH_SIZE, drop_remainder=True).prefetch(tf.data.experimental.AUTOTUNE))

    def buildModel(self):

        # The embedding dimension
        embedding_dim = 256

        # Number of RNN units
        rnn_units = 1024

        self.model = MyModel(vocab_size=len(self.ids_from_chars.get_vocabulary()),embedding_dim=embedding_dim,rnn_units=rnn_units)

    def getExampleBatchPredictions(self): 
        for input_example_batch, self.target_example_batch in self.dataset.take(1):
            self.example_batch_predictions = self.model(input_example_batch)

    def getSampledIndices(self):
        sampled_indices = tf.random.categorical(self.example_batch_predictions[0], num_samples=1)
        sampled_indices = tf.squeeze(sampled_indices, axis=-1).numpy()

    def trainModel(self):
        loss = self.lossFunction()
        self.model.compile(optimizer=self.optimizer, loss=loss)
    
    def lossFunction(self):
        loss = tf.losses.SparseCategoricalCrossentropy(from_logits=True)
        example_batch_loss = loss(self.target_example_batch, self.example_batch_predictions)
        self.mean_loss = example_batch_loss.numpy().mean()

        self.predictionShape = self.example_batch_predictions.shape;

        return loss

    def configureCheckpoints(self):
        checkpoint_dir = './training_checkpoints'
        checkpoint_prefix = os.path.join(checkpoint_dir, "ckpt_{epoch}")
        self.checkpoint_callback = tf.keras.callbacks.ModelCheckpoint(filepath=checkpoint_prefix, save_weights_only=True)

    def fitModel(self):
        history = self.model.fit(self.dataset, epochs=self.epochsCount, callbacks=[self.checkpoint_callback])

    def setupModel(self):
        self.getUniqueCharacters()
        self.vectorizeText()
        self.prediction()
        self.setSequences()
        self.createTrainingBatches()

        self.buildModel()
        self.getExampleBatchPredictions()
        self.getSampledIndices()
        self.trainModel()
        self.configureCheckpoints()
        self.fitModel()


    def generateText(self, input, predictCharcaterCount=1000):
        if self.generationType == 'LOAD':
            predictedText = self.generateTextLoadedModel(input, predictCharcaterCount)
        else:
            predictedText = self.generateTextNewModel(input, predictCharcaterCount)
        return predictedText
        
    def generateTextLoadedModel(self, input, predictCharcaterCount=1000):
        start = time.time()
        states = None
        next_char = tf.constant([input])
        result = [next_char]

        for n in range(predictCharcaterCount):
            next_char, states = self.one_step_reloaded.generate_one_step(next_char, states=states)
            result.append(next_char)

        result = tf.strings.join(result)
        end = time.time()

        self.runTime = end - start

        return result[0].numpy().decode('utf-8')
    
    def generateTextNewModel(self, input, predictCharcaterCount=1000):
        self.one_step_model = OneStep(self.model, self.chars_from_ids, self.ids_from_chars, temperature=self.temperature)

        start = time.time()
        states = None
        next_char = tf.constant([input])
        result = [next_char]

        for n in range(predictCharcaterCount):
            next_char, states = self.one_step_model.generate_one_step(next_char, states=states)
            result.append(next_char)

        result = tf.strings.join(result)
        end = time.time()

        self.runTime = end - start

        return result[0].numpy().decode('utf-8')
    

    def saveModel(self):
      tf.saved_model.save(self.one_step_model, 'new_model')
    
    def loadModel(self, path):
      self.one_step_reloaded = tf.saved_model.load(path)


class MyModel(tf.keras.Model):
    def __init__(self, vocab_size, embedding_dim, rnn_units):
        super().__init__(self)
        self.embedding = tf.keras.layers.Embedding(vocab_size, embedding_dim)
        self.gru = tf.keras.layers.GRU(rnn_units,
                                   return_sequences=True,
                                   return_state=True)
        self.dense = tf.keras.layers.Dense(vocab_size)

    def call(self, inputs, states=None, return_state=False, training=False):
        x = inputs
        x = self.embedding(x, training=training)
        if states is None:
            states = self.gru.get_initial_state(x)
        x, states = self.gru(x, initial_state=states, training=training)
        x = self.dense(x, training=training)

        if return_state:
           return x, states
        else:
           return x

class OneStep(tf.keras.Model):
    def __init__(self, model, chars_from_ids, ids_from_chars, temperature=0.5):
        super().__init__()
        self.temperature = temperature
        self.model = model
        self.chars_from_ids = chars_from_ids
        self.ids_from_chars = ids_from_chars

        # Create a mask to prevent "[UNK]" from being generated.
        skip_ids = self.ids_from_chars(['[UNK]'])[:, None]
        sparse_mask = tf.SparseTensor(
            # Put a -inf at each bad index.
            values=[-float('inf')]*len(skip_ids),
            indices=skip_ids,
            # Match the shape to the vocabulary
            dense_shape=[len(ids_from_chars.get_vocabulary())])
        self.prediction_mask = tf.sparse.to_dense(sparse_mask)

    @tf.function
    def generate_one_step(self, inputs, states=None):
        # Convert strings to token IDs.
        input_chars = tf.strings.unicode_split(inputs, 'UTF-8')
        input_ids = self.ids_from_chars(input_chars).to_tensor()

        # Run the model.
        # predicted_logits.shape is [batch, char, next_char_logits]
        predicted_logits, states = self.model(inputs=input_ids, states=states,
                                            return_state=True)
        # Only use the last prediction.
        predicted_logits = predicted_logits[:, -1, :]
        predicted_logits = predicted_logits/self.temperature
        # Apply the prediction mask: prevent "[UNK]" from being generated.
        predicted_logits = predicted_logits + self.prediction_mask

        # Sample the output logits to generate token IDs.
        predicted_ids = tf.random.categorical(predicted_logits, num_samples=1)
        predicted_ids = tf.squeeze(predicted_ids, axis=-1)

        # Convert from token ids to characters
        predicted_chars = self.chars_from_ids(predicted_ids)

        # Return the characters and model state.
        return predicted_chars, states