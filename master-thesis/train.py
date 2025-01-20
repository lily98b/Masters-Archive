
import os
import torch
import torch.nn as nn
import numpy as np
import torch.nn.functional as F 
from tqdm import tqdm
import torch_optimizer as otpim
from model import GoClass
from data_loader import train_dataloader, test_dataloader
from sklearn import metrics


"""
metrics to evaluate the model
"""

def true_positive(labels, predictions):
    tp = []
    tot_p = []
    for label, prediction in zip(labels, predictions):
        for i,j in zip(label.tolist(), round_numbers(prediction.to("cpu").detach().tolist())):
            if j ==1:
              tot_p.append(1)
            if i == 1 and j == 1:
                tp.append(1)
    if tot_p == []:
      return 0
    else:
      return sum(tp)/sum(tot_p)

def true_negative(labels, predictions): 
  tn = []
  tot_n = []
  for label, prediction in zip(labels, predictions):
    for i,j in zip(label.tolist(), round_numbers(prediction.to("cpu").detach().tolist())):
      if j ==0:
        tot_n.append(1)
      if i == 0 and j == 0:
        tn.append(1)
  return sum(tn)/sum(tot_n)

def false_negative(labels, predictions):
  fn = []
  tot_n = []
  for label, prediction in zip(labels, predictions):
    for i,j in zip(label.tolist(), round_numbers(prediction.to("cpu").detach().tolist())):
      if j ==0:
        tot_n.append(1)
      if i == 1 and j == 0:
        fn.append(1)
  return sum(fn)/sum(tot_n)

def false_positive(labels, predictions):
  fp = []
  tot_p = []
  for label, prediction in zip(labels, predictions):
    for i,j in zip(label.tolist(), round_numbers(prediction.to("cpu").detach().tolist())):
      if j ==1:
        tot_p.append(1)
      if i == 0 and j == 1:
        fp.append(1)
  return sum(fp)/sum(tot_p)


def round_numbers(number):
  return [round(i) for i in number]


#accuracy for exact match ratio
def acc_exact(labels, predictions):
    accuracy = []
    for label, prediction in zip(labels, predictions):
        if label.tolist() == round_numbers(prediction.to("cpu").detach().tolist()):
            accuracy.append(1)
        else:
            accuracy.append(0)
    return sum(accuracy)/len(accuracy)

#label-based accuracy
def acc_label(labels, predictions):
    accuracy = []
    for label, prediction in zip(labels, predictions):
        element_acc = []
        for i,j in zip(label.tolist(), round_numbers(prediction.to("cpu").detach().tolist())):
            if i == j:
                element_acc.append(1)
            else:
                element_acc.append(0)
        accuracy.append(sum(element_acc)/len(element_acc))
    return sum(accuracy)/len(accuracy)




#multilabel metric, F1
"""
The F1 score can be interpreted as a harmonic mean of the precision and recall,
where an F1 score reaches its best value at 1 and worst score at 0.
"""
def F1_score(labels, predictions):
    f_one_score = metrics.f1_score(labels, predictions, average='sample')
    return f_one_score


def round_numbers(number):
  return [round(i) for i in number]


#accuracy for exact match ratio
def acc_exact(labels, predictions):
    accuracy = []
    for label, prediction in zip(labels, predictions):
        if label.tolist() == round_numbers(prediction.to("cpu").detach().tolist()):
            accuracy.append(1)
        else:
            accuracy.append(0)
    return sum(accuracy)/len(accuracy)

#multilabel metric, rercall or sensitivity
def recall(labels, predictions):
    recall = metrics.recall_score(labels, predictions, average='sample')
    return recall
#multilabel metric, precision
def precision(labels, predicitons):
    precision = metrics.precision_score(labels, predictions, average='sample')
    return precision

#Area under the curve









def train(model, device, trainloader, optimizer, lr):
    """
    args
    model = The model object must be instantiated here
    device = choosing between cpu or gpu for training
    optimizer = choosing the optimizer type
    lr = learning rate
    gamma = learning rate decay multipier
    """
    loss_total = 0
    acc_total=0
    tp_total=0
    acc_ind_total=0
    model.train()
    model.to(device)
    loss = nn.BCELoss() #loss function between the non-linear transformation of the logit output and the target.
    scheduler = torch.optim.lr_scheduler.StepLR(optimizer, gamma=0.8, step_size=2)    #adjusting learning rate at each epoch
    for count, (protein, label) in enumerate(trainloader):
        optimizer.zero_grad()
        protein, label = protein.to(device), label.to(device)
        output = model(protein)
        l = loss(output, label.float())
        l.backward()
        optimizer.step()
        loss_total += l.item()
        acc = acc_exact(label.float(), output)
        acc_ind = acc_label(label.float(), output)
        tp = true_positive(label.float(), output)
        acc_total += acc
        tp_total += tp
        acc_ind_total += acc_ind
    acc = acc_total/count
    tp = tp_total/count
    acc_ind = acc_ind_total/count
    scheduler.step() #adjustment of lr at each epoch
    return tp, acc, acc_ind, loss_total




epochs = 100
model = GoClass(input_dim=1280, output_dim=17, dropout=0.2)
device = torch.device("cuda" if torch.cuda.is_available else "cpu")  #devices to put the model and the data on the device
lr = 0.001
optimizer = otpim.RAdam(model.parameters(), lr=0.001)
for epoch in tqdm(range(epochs)):
    tp, acc, acc_ind, loss_total= train(model, device, train_dataloader, optimizer = optimizer, lr = lr)
    print(tp, acc, acc_ind, loss_total)