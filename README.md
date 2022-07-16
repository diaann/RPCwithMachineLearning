# RPC with Machine Learning

Remote Procedure Call (RPC) is a distributed computing technique in which a computer program calls a procedure to execute in a different address space than its own. The procedure may be on the same system or a different system connected on a network. RPC uses the client-server model. The requesting program is a client, and the service-providing program is the server.

In this project we use machine learning to predict whether heart disease or not. The dataset used is from kaggle.com. There are 3 algorithms that we use, namely Naive Bayes, SVM, and the last one is KNN.

### How to use

1. install the libraries that will be used.
2. go to the directory where the server and client files are stored.
3. at the command prompt, run the following command

```
server_heart_disease.py
```

4. after "server is ready" appears, open a new command prompt and run the following command

```
client_heart_disease.py
```

5. later, several questions will appear. answer the question, then at the end a prediction will appear whether heart disease or not.
