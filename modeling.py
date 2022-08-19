#!/usr/bin/env python
# coding: utf-8

# In[7]:


from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression

import warnings
warnings.filterwarnings("ignore")

# Decision Tree functions
def decision_tree_train(X_train, y_train, selected_features, target, d = 10, m=1, print_results = True):
  
    clf = DecisionTreeClassifier(max_depth=d, min_samples_leaf = m, random_state=123)
    clf = clf.fit(X_train, y_train)
    accuracy = clf.score(X_train, y_train)
    y_pred = clf.predict(X_train)
    class_report = classification_report(y_train, y_pred,output_dict=True)
    
    tn, fp, fn, tp = confusion_matrix(y_train, y_pred).ravel()
        
    fp_rate = fp/(fp+tn)
    fn_rate = fn/(fn+tp)
    tp_rate = tp/(tp+fn)
    tn_rate = tn/(fp+tn)
    if print_results:
        print(f"TRAINING RESULTS: {type(clf).__name__}")
        print(f"Using features: {selected_features}")
        print(f"Depth of {clf.max_depth}")
        print(f"Min Sample Leaf of {clf.min_samples_leaf}")
        print("----------------")
        print(f"Accuracy score on training set is: {accuracy:.2f}")
        print(classification_report(y_train, y_pred))


        print(f"False positive rate: {fp/(fp+tn):.2%}")
        print(f"False negative rate: {fn/(fn+tp):.2%}")
        print(f"True positive rate: {tp/(tp+fn):.2%}")
        print(f"True negative rate: {tn/(fp+tn):.2%}")
        print("----------------")
    
    train_report = {'d':clf.max_depth, 
                    'm':clf.min_samples_leaf,
                    'accuracy':accuracy, 
                    'precision':class_report['1']['precision'], 
                    'recall':class_report['1']['recall'],
                   'fp_rate':fp_rate,
                   'fn_rate':fn_rate,
                   'tp_rate':tp_rate,
                   'tn_rate':tn_rate}
    
    return clf, train_report

def classifier_validate(X_validate, y_validate, clf, print_results=True):
    d = clf.max_depth
    accuracy = clf.score(X_validate, y_validate)


    # Produce y_predictions that come from the X_validate
    y_pred = clf.predict(X_validate)
    
    class_report = classification_report(y_validate, y_pred,output_dict=True)
    tn, fp, fn, tp = confusion_matrix(y_validate, y_pred).ravel()
    
    fp_rate = fp/(fp+tn)
    fn_rate = fn/(fn+tp)
    tp_rate = tp/(tp+fn)
    tn_rate = tn/(fp+tn)
    # Compare actual y values (from validate) to predicted y_values from the model run on X_validate
    if print_results:
        print(f"-----VALIDATE RESULTS: {type(clf).__name__}-----")
        print(f"Using features: {selected_features}")
        print(f"Depth of {clf.max_depth}")
        print(f"Min Sample Leaf of {clf.min_samples_leaf}")
        print(classification_report(y_validate, y_pred))

        print(f'Accuracy on validate set: {accuracy:.2f}')
    validate_report = {'d':clf.max_depth, 
                       'm':clf.min_samples_leaf,
                    'accuracy':accuracy, 
                    'precision':class_report['1']['precision'], 
                    'recall':class_report['1']['recall'],
                   'fp_rate':fp_rate,
                   'fn_rate':fn_rate,
                   'tp_rate':tp_rate,
                   'tn_rate':tn_rate}
    
    return validate_report

# Random Forest Functions
def random_forest_train(X_train, y_train, selected_features, target, d = 10, m=1, print_results = True):
  
    clf = RandomForestClassifier(max_depth=d, min_samples_leaf = m, random_state=123)
    clf = clf.fit(X_train, y_train)
    accuracy = clf.score(X_train, y_train)
    y_pred = clf.predict(X_train)
    class_report = classification_report(y_train, y_pred,output_dict=True)
    
    tn, fp, fn, tp = confusion_matrix(y_train, y_pred).ravel()
        
    fp_rate = fp/(fp+tn)
    fn_rate = fn/(fn+tp)
    tp_rate = tp/(tp+fn)
    tn_rate = tn/(fp+tn)
    if print_results:
        print(f"TRAINING RESULTS: {type(clf).__name__}")
        print(f"Using features: {selected_features}")
        print(f"Depth of {clf.max_depth}")
        print(f"Min Sample Leaf of {clf.min_samples_leaf}")
        print("----------------")
        print(classification_report(y_train, y_pred))


        print(f"False positive rate: {fp/(fp+tn):.2%}")
        print(f"False negative rate: {fn/(fn+tp):.2%}")
        print(f"True positive rate: {tp/(tp+fn):.2%}")
        print(f"True negative rate: {tn/(fp+tn):.2%}")
        print("----------------")
    
    train_report = {'d':clf.max_depth, 
                    'm':clf.min_samples_leaf,
                    'accuracy':accuracy, 
                    'precision':class_report['1']['precision'], 
                    'recall':class_report['1']['recall'],
                   'fp_rate':fp_rate,
                   'fn_rate':fn_rate,
                   'tp_rate':tp_rate,
                   'tn_rate':tn_rate}
    
    return clf, train_report

# KNN Functions
def knn_train(X_train, y_train, selected_features, target, k=1, print_results = True):
  
    clf = KNeighborsClassifier(n_neighbors=k)
    clf = clf.fit(X_train, y_train)
    accuracy = clf.score(X_train, y_train)
    y_pred = clf.predict(X_train)
    class_report = classification_report(y_train, y_pred,output_dict=True)
    
    tn, fp, fn, tp = confusion_matrix(y_train, y_pred).ravel()
        
    fp_rate = fp/(fp+tn)
    fn_rate = fn/(fn+tp)
    tp_rate = tp/(tp+fn)
    tn_rate = tn/(fp+tn)
    if print_results:
        print(f"TRAINING RESULTS: {type(clf).__name__}")
        print(f"Using features: {selected_features}")
        print(f"K of {clf.n_neighbors}")
        print("----------------")
        print(classification_report(y_train, y_pred))


        print(f"False positive rate: {fp/(fp+tn):.2%}")
        print(f"False negative rate: {fn/(fn+tp):.2%}")
        print(f"True positive rate: {tp/(tp+fn):.2%}")
        print(f"True negative rate: {tn/(fp+tn):.2%}")
        print("----------------")
    
    train_report = {'k':clf.n_neighbors, 
                    'accuracy':accuracy, 
                    'precision':class_report['1']['precision'], 
                    'recall':class_report['1']['recall'],
                   'fp_rate':fp_rate,
                   'fn_rate':fn_rate,
                   'tp_rate':tp_rate,
                   'tn_rate':tn_rate}
    
    return clf, train_report

def knn_validate(X_validate, y_validate, clf, print_results=True):
    accuracy = clf.score(X_validate, y_validate)


    # Produce y_predictions that come from the X_validate
    y_pred = clf.predict(X_validate)
    
    class_report = classification_report(y_validate, y_pred,output_dict=True)
    tn, fp, fn, tp = confusion_matrix(y_validate, y_pred).ravel()
    
    fp_rate = fp/(fp+tn)
    fn_rate = fn/(fn+tp)
    tp_rate = tp/(tp+fn)
    tn_rate = tn/(fp+tn)
    # Compare actual y values (from validate) to predicted y_values from the model run on X_validate
    if print_results:
        print(f"-----VALIDATE RESULTS: {type(clf).__name__}-----")
        print(f"Using features: {selected_features}")
        print(f"K of {clf.n_neighbors}")
        print(classification_report(y_validate, y_pred))

        print(f'Accuracy on validate set: {accuracy:.2f}')
    validate_report = {'k':clf.n_neighbors, 
                    'accuracy':accuracy, 
                    'precision':class_report['1']['precision'], 
                    'recall':class_report['1']['recall'],
                   'fp_rate':fp_rate,
                   'fn_rate':fn_rate,
                   'tp_rate':tp_rate,
                   'tn_rate':tn_rate}
    
    return validate_report

# Logistical Regression Functions
def logistic_regression_train(X_train, y_train, selected_features, target, c=1, print_results = True):
  
    clf = LogisticRegression(C=c)
    clf = clf.fit(X_train, y_train)
    accuracy = clf.score(X_train, y_train)
    y_pred = clf.predict(X_train)
    class_report = classification_report(y_train, y_pred,output_dict=True)
    
    tn, fp, fn, tp = confusion_matrix(y_train, y_pred).ravel()
        
    fp_rate = fp/(fp+tn)
    fn_rate = fn/(fn+tp)
    tp_rate = tp/(tp+fn)
    tn_rate = tn/(fp+tn)
    if print_results:
        print(f"TRAINING RESULTS: {type(clf).__name__}")
        print(f"Using features: {selected_features}")
        print(f"C of {clf.C}")
        print("----------------")
        print(classification_report(y_train, y_pred))


        print(f"False positive rate: {fp/(fp+tn):.2%}")
        print(f"False negative rate: {fn/(fn+tp):.2%}")
        print(f"True positive rate: {tp/(tp+fn):.2%}")
        print(f"True negative rate: {tn/(fp+tn):.2%}")
        print("----------------")
    
    train_report = {'c':clf.C, 
                    'accuracy':accuracy, 
                    'precision':class_report['1']['precision'], 
                    'recall':class_report['1']['recall'],
                   'fp_rate':fp_rate,
                   'fn_rate':fn_rate,
                   'tp_rate':tp_rate,
                   'tn_rate':tn_rate}
    
    return clf, train_report

def logisitic_regression_validate(X_validate, y_validate, clf, print_results=True):
    accuracy = clf.score(X_validate, y_validate)

    # Produce y_predictions that come from the X_validate
    y_pred = clf.predict(X_validate)
    
    class_report = classification_report(y_validate, y_pred,output_dict=True)
    tn, fp, fn, tp = confusion_matrix(y_validate, y_pred).ravel()
    
    fp_rate = fp/(fp+tn)
    fn_rate = fn/(fn+tp)
    tp_rate = tp/(tp+fn)
    tn_rate = tn/(fp+tn)
    # Compare actual y values (from validate) to predicted y_values from the model run on X_validate
    if print_results:
        print(f"-----VALIDATE RESULTS: {type(clf).__name__}-----")
        print(f"Using features: {selected_features}")
        print(f"C of {clf.C}")
        print(classification_report(y_validate, y_pred))

        print(f'Accuracy on validate set: {accuracy:.2f}')
    validate_report = {'c':clf.C, 
                    'accuracy':accuracy, 
                    'precision':class_report['1']['precision'], 
                    'recall':class_report['1']['recall'],
                   'fp_rate':fp_rate,
                   'fn_rate':fn_rate,
                   'tp_rate':tp_rate,
                   'tn_rate':tn_rate}
    
    return validate_report

def consolidate_results(train_results_df, validate_results_df, join_on):
    """ Consolidates the results of fitting the models on the train dataset and testing on the validate (or test) set. Takes as arguments the classification report and relevant metrics for both the train and validate (test) sets, as well as the parameter(s) to merge the two results on (usually the hyperparameters tested) in the form of a list. Calculates the difference in performance between train and validate and outputs a dataframe of the combined results to allow for easy plotting with Seaborn."""
    
    combined_df = train_results_df.merge(validate_results_df,on=join_on, suffixes=['_train','_validate'])
    # Calculate difference in accuracy between train and validate sets
    combined_df["accuracy_diff"] = combined_df.accuracy_validate-combined_df.accuracy_train
    combined_df["precision_diff"] = combined_df.precision_validate-combined_df.precision_train
    combined_df["recall_diff"] = combined_df.recall_validate-combined_df.recall_train
    combined_df["accuracy_pct_diff"] = (combined_df.accuracy_validate-combined_df.accuracy_train)/combined_df.accuracy_train

    return combined_df