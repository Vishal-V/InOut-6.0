# What's up, doc?

We use the power of AI to provide users with a primary medical diagnosis from any symptoms they may be experiencing. Our project provides a basic cure that patients can use to reduce discomfort. The conversations are almost human-like, and can be implemented for multiple languages.

### Why do we need it?

In developing countries, especially India, it can be seen that the number of doctors in rural areas are very small. Additionally, residents do not have much medical knowledge, and rely either on a doctor's direct advice or on remedies passed down, to interpret any medical symptoms they experience. This leads to overcrowded clinics, or wrongly diagnosed diseases.

Modern advancements in AI in the fields of Natural Language Processing, Natural Language Understanding, Knowledge representation and knowledge extraction can be used for providing a simple, preliminary and accurate diagnosis of a patient's symptoms. Simple remedies can be suggested for minor ailments. Such remedies are extracted form a large corpus of medical data, what is used to train the model.

We use the BERT architecture, which has proven exceptionally good at aforementioned tasks. Additionally, it can be used with multiple languages, if medical datasets are available in those languages.


### Challenges we faced

- The first challenge was preparing data for training. We selected two reputed medical databases for this purpose.

- Next, training requires a lot of compute power, which we cannot carry around in out laptops. We used Google Colab, which provides high-end GPUs for training neural networks.

- We had to reduce the latency of predictions. For this, we had to optimize several parts of our entire pipelie.

- Wrappers had to be created so that the inputs and outputs to and from the model were interpretable by humans.


#### Notes

- The entire pipeline is too big to be set up and run quickly on a local system. A one-time environment setup is required. We have provided a IPython notebook where we demonstrate the working of the system.
